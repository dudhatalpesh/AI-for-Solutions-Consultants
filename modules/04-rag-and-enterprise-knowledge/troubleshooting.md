# Module 04 — Troubleshooting

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

| Symptom | Fix |
|---|---|
| Qdrant collection empty | Run ingestion; check Read/Write Files path is under /data/shared |
| Dimension mismatch | Same embedding model for ingest and query; re-create collection |
| Answers lack citations | Strengthen system prompt; include source metadata in chunks |

See also the [global troubleshooting guide](../../docs/08-troubleshooting-guide.md).
