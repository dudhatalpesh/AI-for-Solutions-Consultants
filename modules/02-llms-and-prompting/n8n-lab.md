# Module 02 — n8n Lab

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

Build a prompt playground workflow: a **Webhook** receives `prompt_variant`, `input` and `temperature`; a **Switch** selects one of several prompt templates held in a **Config** node; a **Basic LLM Chain** with **Ollama Chat Model** runs it; results (variant, latency, output) are returned and optionally logged to Postgres.

Full lab: [Lab 02](../../labs/lab-02-prompt-engineering-playground/README.md). Reuse [workflow 01](../../n8n-workflows/01-basic-llm-workflow.json) as a starting point.
