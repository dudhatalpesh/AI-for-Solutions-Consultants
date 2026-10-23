# Module 09 — n8n Lab

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

**Lab (in this module):** build an **AI gateway workflow**:

1. **Webhook** `POST /ai-gateway` with Header Auth credential.
2. **Code**: validate request, classify data sensitivity (keyword/regex rules), estimate tokens.
3. **Switch**: `restricted` → Ollama (local); `general` → optional cloud model (disabled by default).
4. **Basic LLM Chain** per route.
5. **Postgres**: log caller, route, model, tokens, latency, estimated cost (reuse `lab.llm_calls`).
6. **Respond to Webhook**.

Second part: call a FastAPI RAG service from n8n with **HTTP Request**. Full instructions tracked in [issue #10](../../docs/11-suggested-first-issues.md).
