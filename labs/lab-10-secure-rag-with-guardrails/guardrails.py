"""Lab 10: reference guardrail functions (Python mirror of the n8n Code nodes in workflow 09).

These are heuristics for teaching. They reduce risk; they do not eliminate it.
Run the tests:  python -m pytest -q labs/lab-10-secure-rag-with-guardrails
"""
from __future__ import annotations

import html
import re
import unicodedata
from dataclasses import dataclass, field

ENTITLEMENTS = {
    "contractor": ["public"],
    "employee": ["public", "internal"],
    "security": ["public", "internal", "confidential"],
}

INJECTION_PATTERNS = [
    re.compile(r"ignore (all |any )?(previous|prior|above) (instructions|rules)", re.I),
    re.compile(r"disregard (the )?(system|previous) (prompt|instructions)", re.I),
    re.compile(r"(reveal|print|show|repeat).{0,30}(system prompt|instructions|hidden|secret|api key|password)", re.I),
    re.compile(r"you are now|act as (an? )?(unfiltered|dan|developer mode)", re.I),
    re.compile(r"<\s*script|javascript:", re.I),
]
SUSPICIOUS_CONTEXT = re.compile(
    r"(ignore (all |any )?(previous|prior) instructions|system prompt|you must now|AI assistant:|do not tell the user|send .* to http)",
    re.I,
)
SECRET_PATTERN = re.compile(
    r"(CANARY-[A-Z0-9-]+|api[_-]?key\s*[:=]|password\s*[:=]|BEGIN (RSA|OPENSSH) PRIVATE KEY|sk-[A-Za-z0-9]{16,})", re.I
)
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
CARD = re.compile(r"\b(?:\d[ -]?){13,19}\b")
ZERO_WIDTH = re.compile("[​-‍﻿]")


@dataclass
class InputDecision:
    blocked: bool
    reasons: list[str] = field(default_factory=list)
    safe_question: str = ""
    allowed_classes: list[str] = field(default_factory=list)


def input_guard(question: str, user_role: str, max_chars: int = 500) -> InputDecision:
    role = (user_role or "contractor").lower()
    allowed = ENTITLEMENTS.get(role, ENTITLEMENTS["contractor"])
    q = ZERO_WIDTH.sub("", unicodedata.normalize("NFKC", question or "")).strip()
    reasons = []
    if not q:
        reasons.append("empty_question")
    if len(q) > max_chars:
        reasons.append("too_long")
    if any(p.search(q) for p in INJECTION_PATTERNS):
        reasons.append("possible_prompt_injection")
    q = CARD.sub("[NUMBER_REDACTED]", EMAIL.sub("[EMAIL_REDACTED]", q))
    return InputDecision(bool(reasons), reasons, q[:max_chars], allowed)


def filter_context(chunks: list[dict], allowed_classes: list[str], min_score: float = 0.45) -> tuple[list[dict], list[str]]:
    """chunks: [{'text', 'source', 'classification', 'score'}] -> (kept, quarantined_sources)."""
    kept, quarantined = [], []
    for c in chunks:
        if c.get("classification") not in allowed_classes:
            continue  # entitlement filter (Qdrant does this server-side in the n8n workflow)
        if SUSPICIOUS_CONTEXT.search(c.get("text", "")):
            quarantined.append(c.get("source", "unknown"))
            continue
        if c.get("score", 0) < min_score:
            continue
        kept.append(c)
    return kept, quarantined


@dataclass
class OutputDecision:
    blocked: bool
    issues: list[str]
    answer: str
    citations: list[str]


def output_guard(answer: str, citations: list[str], retrieved_sources: list[str]) -> OutputDecision:
    issues = []
    valid = [c for c in citations if c in retrieved_sources]
    if len(valid) != len(citations):
        issues.append("invented_citation_removed")
    secret = bool(SECRET_PATTERN.search(answer or ""))
    if secret:
        issues.append("secret_pattern")
    text = html.escape(EMAIL.sub("[EMAIL_REDACTED]", answer or ""), quote=True)
    uncited = not valid and "enough information" not in text.lower()
    if uncited:
        issues.append("uncited_answer")
    return OutputDecision(secret or uncited, issues, text[:2000], valid)
