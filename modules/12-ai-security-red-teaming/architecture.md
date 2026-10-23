# Module 12 — Architecture

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

```mermaid
flowchart LR
  TC[Test cases] --> H[n8n harness]
  H --> T1[Vulnerable target]
  H --> T2[Hardened target]
  T1 & T2 --> SC[Scorer] --> RPT[Findings report]
```

## Related reference architectures

- [Secure AI reference architecture](../../architectures/secure-ai-reference-architecture.md)

## To be written

- [ ] Component-by-component explanation
- [ ] Deployment options (local, cloud, hybrid) and trade-offs
- [ ] Scaling and resilience notes
