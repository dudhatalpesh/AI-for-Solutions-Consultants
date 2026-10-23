# Module 09 — Troubleshooting

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

| Symptom | Fix |
|---|---|
| Restore fails to decrypt credentials | Use the original N8N_ENCRYPTION_KEY |
| FastAPI unreachable from n8n | Use the Compose service name, not localhost |
| Queue mode jobs stuck | Check Redis and worker logs (see n8n scaling docs) |

See also the [global troubleshooting guide](../../docs/08-troubleshooting-guide.md).
