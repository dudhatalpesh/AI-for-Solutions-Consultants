# Module 04 — Concepts

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

## Key concepts to cover

- Chunking strategies and overlap
- Embedding models and vector dimensions
- Similarity search, topK and score thresholds
- Metadata and filtering (source, date, classification, access)
- Citations and grounding prompts
- Freshness: scheduled re-ingestion, deletions
- Evaluation: retrieval hit rate, answer correctness, faithfulness

## Failure modes

- Relevant document never retrieved (bad chunking/embeddings)
- Model ignores context and answers from memory
- Stale or deleted content still answered
- Users see content they are not entitled to

## To be written

- [ ] Plain-English explanation of each concept with an SC-relevant example
- [ ] One comparison table and one Mermaid diagram per major concept
- [ ] Acronyms expanded on first use
