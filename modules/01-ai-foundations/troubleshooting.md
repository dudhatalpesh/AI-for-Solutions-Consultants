# Module 01 — Troubleshooting

| # | Symptom | Likely cause | Fix |
|---|---|---|---|
| 1 | `curl localhost:11434/api/tags` shows no models | `ollama-init` did not finish | `docker compose logs ollama-init`; rerun `docker compose exec ollama ollama pull llama3.2` |
| 2 | n8n Ollama credential test fails | Base URL uses `localhost` | Use `http://ollama:11434` inside n8n |
| 3 | Webhook returns 404 | Test vs production URL | Click **Execute workflow** and use `/webhook-test/...`, or publish and use `/webhook/...` |
| 4 | "Failed to parse" from Structured Output Parser | Model output not valid JSON for the schema | Lower temperature; keep schema small; turn on **Auto-Fix Format** in the parser (costs an extra model call) |
| 5 | Request takes > 60 s or times out | CPU-only, first model load, large input | Send a warm-up request; shorten input; check `docker stats` for memory pressure |
| 6 | 502 fallback every time | Ollama container stopped or model missing | `docker compose ps`; restart Ollama; check model name in the Ollama Chat Model node |
| 7 | Python `ConnectError` | Wrong URL or stack not running | Use `http://localhost:11434` from your laptop |
| 8 | Different answers on each run | Temperature > 0 and normal model variation | Set temperature 0–0.2 for structured tasks; validate outputs rather than expecting identical text |
| 9 | Embedding dimension mismatch later in Module 04 | Different embedding model than the collection was created with | Use the same model for ingest and query; re-create collection if you change it |

Still stuck? See the [global troubleshooting guide](../../docs/08-troubleshooting-guide.md).
