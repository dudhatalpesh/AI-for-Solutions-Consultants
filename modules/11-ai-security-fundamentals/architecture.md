# Module 11 — Architecture

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

```mermaid
flowchart LR
  U[User] --> IG[Input guard] --> RET[Retrieval + entitlement filter]
  RET --> SAN[Sanitise context] --> LLM[Model] --> OG[Output guard] --> A[Answer]
  IG -->|blocked| REF[Refusal + log]
  OG -->|blocked| REF
```

## Related reference architectures

- [Secure AI reference architecture](../../architectures/secure-ai-reference-architecture.md)
- [Enterprise RAG](../../architectures/enterprise-rag.md)

## To be written

- [ ] Component-by-component explanation
- [ ] Deployment options (local, cloud, hybrid) and trade-offs
- [ ] Scaling and resilience notes
