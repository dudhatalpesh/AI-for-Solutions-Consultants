# Module 03 — Concepts

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

## Key concepts to cover

- Intents, scope and persona
- Conversation memory: window memory vs durable memory, session keys
- Grounding with FAQ tools vs full RAG
- Escalation design and handover payloads
- Conversation testing: ambiguous, out-of-scope, adversarial
- Channels: web chat, Slack, Teams (check current n8n trigger nodes)

## Failure modes

- Bot answers out-of-scope questions confidently
- Memory mixes users when session keys are wrong
- No graceful escalation; users stuck in loops
- Tone or policy violations

## To be written

- [ ] Plain-English explanation of each concept with an SC-relevant example
- [ ] One comparison table and one Mermaid diagram per major concept
- [ ] Acronyms expanded on first use
