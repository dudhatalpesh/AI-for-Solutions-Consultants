"""Repository validation: JSON/JSONL parse, n8n workflow structure, relative Markdown links, secret patterns.

Usage: python scripts/validate_repo.py   (exit code 1 on any problem)
Standard library only.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", "shared", "__pycache__"}
problems: list[str] = []


def files(pattern: str):
    for p in ROOT.rglob(pattern):
        if not any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            yield p


def rel(p: Path) -> str:
    return p.relative_to(ROOT).as_posix()


# 1. JSON and n8n workflow structure
for p in files("*.json"):
    try:
        data = json.loads(p.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        problems.append(f"{rel(p)}: invalid JSON ({e})")
        continue
    if isinstance(data, dict) and "nodes" in data and "connections" in data:
        names = [n.get("name") for n in data["nodes"]]
        if len(names) != len(set(names)):
            problems.append(f"{rel(p)}: duplicate node names")
        for n in data["nodes"]:
            if "credentials" in n:
                problems.append(f"{rel(p)}: node '{n['name']}' contains a credentials block")
            for key in ("type", "typeVersion", "position", "parameters"):
                if key not in n:
                    problems.append(f"{rel(p)}: node '{n.get('name')}' missing '{key}'")
        connected = set()
        for src, outputs in data["connections"].items():
            connected.add(src)
            if src not in names:
                problems.append(f"{rel(p)}: connection from unknown node '{src}'")
            for conns in outputs.values():
                for branch in conns:
                    for c in branch or []:
                        connected.add(c["node"])
                        if c["node"] not in names:
                            problems.append(f"{rel(p)}: connection to unknown node '{c['node']}'")
        for n in data["nodes"]:
            if n["type"] != "n8n-nodes-base.stickyNote" and n["name"] not in connected:
                problems.append(f"{rel(p)}: node '{n['name']}' is not connected")
        if "VULNERABLE" in json.dumps(data) and "EDUCATIONAL" not in data.get("name", ""):
            problems.append(f"{rel(p)}: vulnerable content must be named EDUCATIONAL-VULNERABLE")

for p in files("*.jsonl"):
    for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                json.loads(line)
            except json.JSONDecodeError as e:
                problems.append(f"{rel(p)}:{i}: invalid JSONL ({e})")

# 2. Relative links in Markdown resolve
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
for p in files("*.md"):
    text = p.read_text(encoding="utf-8")
    text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignore code blocks
    for target in LINK.findall(text):
        if target.startswith(("http://", "https://", "mailto:", "#")):
            continue
        path = target.split("#", 1)[0]
        if not path:
            continue
        if not (p.parent / path).resolve().exists():
            problems.append(f"{rel(p)}: broken link -> {target}")

# 3. Secret-like patterns (allow the documented fake canary and placeholders)
SECRET = re.compile(
    r"(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|gho_[A-Za-z0-9]{30,}|AKIA[0-9A-Z]{16}|xox[baprs]-[A-Za-z0-9-]{10,}"
    r"|-----BEGIN (RSA |OPENSSH |EC )?PRIVATE KEY-----)"
)
for pattern in ("*.md", "*.json", "*.jsonl", "*.py", "*.yml", "*.yaml", "*.sql", ".env*", "Makefile"):
    for p in files(pattern):
        if p.name == "validate_repo.py":
            continue
        for m in SECRET.finditer(p.read_text(encoding="utf-8", errors="ignore")):
            if "BEGIN" in m.group(0) and p.suffix in {".py", ".json", ".md"}:
                continue  # detection regexes and docs mention the header text
            problems.append(f"{rel(p)}: possible secret '{m.group(0)[:12]}...'")

# 4. .env must never be committed
if (ROOT / ".env").exists():
    tracked_hint = "(make sure it is git-ignored)"
    print(f"note: .env exists locally {tracked_hint}")

if problems:
    print("\n".join(problems))
    print(f"\n{len(problems)} problem(s) found.")
    sys.exit(1)
print("Repository validation passed.")
