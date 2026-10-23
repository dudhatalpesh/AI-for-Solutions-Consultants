# Module 04 — Architecture

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

```mermaid
flowchart LR
  subgraph Ingest
    F[Docs] --> L[Loader] --> S[Splitter] --> E1[Embeddings] --> V[(Qdrant)]
  end
  subgraph Query
    Q[Question] --> E2[Embeddings] --> V
    V --> C[Top-k chunks] --> G[LLM with citations] --> A[Answer]
  end
```

## Related reference architectures

- [Enterprise RAG](../../architectures/enterprise-rag.md)
- [Secure AI reference architecture](../../architectures/secure-ai-reference-architecture.md)

## To be written

- [ ] Component-by-component explanation
- [ ] Deployment options (local, cloud, hybrid) and trade-offs
- [ ] Scaling and resilience notes
