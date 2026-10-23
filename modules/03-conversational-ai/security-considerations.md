# Module 03 — Security Considerations

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

| Risk | Control |
|---|---|
| Users share PII in chat | Warn users; redact before logging; retention limits |
| Public chat endpoint abuse | Authentication, rate limiting, input length limits |
| Memory leakage between sessions | Unique, unguessable session IDs; durable memory access control |

See also the [AI security playbook](../../docs/06-ai-security-playbook.md).
