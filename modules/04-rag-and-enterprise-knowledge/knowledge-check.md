# Module 04 — Knowledge Check

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

## Questions

1. List the RAG ingestion steps.
2. Why must ingest and query use the same embedding model?
3. How do you enforce document permissions in RAG?
4. What is an insufficient-context guardrail?

## Answers

1. Load, chunk, embed, store (with metadata).
2. Vectors from different models are not comparable and dimensions may differ.
3. Store access metadata and filter retrieval by the user's entitlements.
4. The assistant declines to answer when retrieved context does not support an answer.
