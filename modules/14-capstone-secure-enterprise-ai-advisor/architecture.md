# Module 14 — Architecture

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

```mermaid
flowchart LR
  U[User] --> GW[Input guard] --> RT{Router}
  RT --> RAG[RAG Q&A]
  RT --> AG[Agent + tools]
  RT --> MA[Multi-agent report]
  AG --> HITL[Approval]
  RAG & AG & MA --> OG[Output guard] --> A[Answer]
  GW & RAG & AG & MA & OG --> LOG[(Telemetry)]
```

## Related reference architectures

- [Secure AI reference architecture](../../architectures/secure-ai-reference-architecture.md)
- [n8n reference architectures](../../architectures/n8n-reference-architectures.md)

## To be written

- [ ] Component-by-component explanation
- [ ] Deployment options (local, cloud, hybrid) and trade-offs
- [ ] Scaling and resilience notes
