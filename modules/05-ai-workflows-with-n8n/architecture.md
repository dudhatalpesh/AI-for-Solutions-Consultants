# Module 05 — Architecture

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

```mermaid
flowchart LR
  IN[Email / ticket] --> CL[Text Classifier]
  CL -->|billing| QB[Billing queue]
  CL -->|technical| QT[Tech queue]
  CL -->|unclear| EX[Exception queue → human]
  QB & QT & EX --> LOG[(Audit log)]
```

## Related reference architectures

- [n8n reference architectures](../../architectures/n8n-reference-architectures.md)

## To be written

- [ ] Component-by-component explanation
- [ ] Deployment options (local, cloud, hybrid) and trade-offs
- [ ] Scaling and resilience notes
