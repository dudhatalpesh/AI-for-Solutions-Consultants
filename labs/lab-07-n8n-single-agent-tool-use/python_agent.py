"""Lab 07: a minimal tool-calling agent loop in Python with the Ollama client.

Mirrors the n8n workflow so you can see what the AI Agent node does under the hood.
Requires: pip install ollama  (Ollama Python client; tool calling supported in recent versions — check its README)

Usage:
    python labs/lab-07-n8n-single-agent-tool-use/python_agent.py "Is ACME-001 affected by any VPN issue?"
"""
from __future__ import annotations

import json
import os
import sys

from ollama import Client

MODEL = os.getenv("OLLAMA_CHAT_MODEL", "llama3.2")
client = Client(host=os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"))

ACCOUNTS = {
    "ACME-001": {"name": "Acme Corp (demo)", "plan": "Enterprise", "owner_team": "Team Blue", "open_tickets": 2},
    "GLOBEX-002": {"name": "Globex (demo)", "plan": "Business", "owner_team": "Team Green", "open_tickets": 0},
}
STATUS = {
    "vpn": {"status": "degraded", "note": "Intermittent disconnects in EU region since 08:10 UTC (INC-4471)"},
    "email": {"status": "operational", "note": ""},
}


def lookup_account(account_id: str) -> str:
    """Look up a customer account by ID (format ABCDE-123). Returns plan, owner team and open tickets."""
    return json.dumps(ACCOUNTS.get(account_id.strip().upper(), "NOT_FOUND"))


def check_service_status(service: str) -> str:
    """Get the current status of a service: vpn or email."""
    return json.dumps(STATUS.get(service.strip().lower(), "NOT_FOUND"))


def request_service_credit(account_id: str, amount_usd: float, reason: str) -> str:
    """RESTRICTED. Create a service-credit REQUEST that a human must approve. Never issues the credit."""
    if amount_usd <= 0 or amount_usd > 5000:
        return "REJECTED: amount must be between 0 and 5000 USD."
    return f"PENDING_APPROVAL: request for {amount_usd} USD on {account_id} created ({reason})."


TOOLS = {f.__name__: f for f in (lookup_account, check_service_status, request_service_credit)}
SYSTEM = ("You are an account operations assistant (demo data). Use tools for facts. Never claim a credit was issued; "
          "say it is pending approval. If a tool returns NOT_FOUND, say so.")
MAX_ITERATIONS = 6


def run(question: str) -> str:
    messages = [{"role": "system", "content": SYSTEM}, {"role": "user", "content": question}]
    for _ in range(MAX_ITERATIONS):
        response = client.chat(model=MODEL, messages=messages, tools=list(TOOLS.values()), options={"temperature": 0.1})
        msg = response.message
        messages.append(msg)
        if not msg.tool_calls:
            return msg.content
        for call in msg.tool_calls:
            fn = TOOLS.get(call.function.name)
            args = call.function.arguments or {}
            result = fn(**args) if fn else f"Unknown tool {call.function.name}"
            print(f"  tool call: {call.function.name}({args}) -> {result[:100]}")
            messages.append({"role": "tool", "content": result, "tool_name": call.function.name})
    return "Stopped: max iterations reached."


if __name__ == "__main__":
    q = " ".join(sys.argv[1:]) or "Is ACME-001 affected by any VPN issue?"
    print(f"Q: {q}")
    print(f"A: {run(q)}")
