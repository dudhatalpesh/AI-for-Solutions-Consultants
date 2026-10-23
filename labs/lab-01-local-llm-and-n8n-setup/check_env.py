"""Lab 01 environment check: n8n, Ollama (models + a short generation) and Qdrant.

Usage (from the repo root, virtual env active):
    python labs/lab-01-local-llm-and-n8n-setup/check_env.py
"""
from __future__ import annotations

import os
import sys
import time

import httpx

N8N = os.getenv("N8N_BASE_URL", "http://localhost:5678")
OLLAMA = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
QDRANT = os.getenv("QDRANT_URL", "http://localhost:6333")
CHAT_MODEL = os.getenv("OLLAMA_CHAT_MODEL", "llama3.2")
EMBED_MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

failures = 0


def report(ok: bool, name: str, detail: str) -> None:
    global failures
    if not ok:
        failures += 1
    print(f"[{'OK' if ok else 'FAIL':4}] {name:17s} {detail}")


def check_n8n() -> None:
    try:
        r = httpx.get(f"{N8N}/healthz", timeout=10)
        report(r.status_code == 200, "n8n health", f"{N8N}/healthz -> {r.status_code}")
    except httpx.HTTPError as e:
        report(False, "n8n health", f"{e!r} (is the stack running? docker compose ps)")


def check_ollama() -> None:
    try:
        tags = httpx.get(f"{OLLAMA}/api/tags", timeout=10).json()
        names = {m["name"].split(":")[0] for m in tags.get("models", [])}
        missing = {CHAT_MODEL, EMBED_MODEL} - names
        detail = ", ".join(sorted(names)) or "none"
        if missing:
            detail += f" | missing: {', '.join(sorted(missing))}"
        report(not missing, "Ollama models", detail)
        if CHAT_MODEL in names:
            start = time.perf_counter()
            r = httpx.post(
                f"{OLLAMA}/api/generate",
                json={"model": CHAT_MODEL, "prompt": "Reply with the single word: ready", "stream": False},
                timeout=300,
            ).json()
            secs = time.perf_counter() - start
            report(True, "Ollama generate", f"{r.get('eval_count', '?')} tokens in {secs:.1f} s -> {r.get('response', '').strip()[:40]!r}")
    except httpx.HTTPError as e:
        report(False, "Ollama", repr(e))


def check_qdrant() -> None:
    try:
        r = httpx.get(f"{QDRANT}/collections", timeout=10)
        report(r.status_code == 200, "Qdrant", f"{QDRANT}/collections -> {r.status_code}")
    except httpx.HTTPError as e:
        report(False, "Qdrant", repr(e))


if __name__ == "__main__":
    check_n8n()
    check_ollama()
    check_qdrant()
    print("\nAll checks passed." if failures == 0 else f"\n{failures} check(s) failed. See docs/02-environment-setup.md section 10.")
    sys.exit(1 if failures else 0)
