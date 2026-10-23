# Module 07 — Architecture

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

```mermaid
flowchart LR
  U[Request] --> AG[AI Agent]
  AG -.-> M[Model]
  AG -.-> T1[lookup_account]
  AG -.-> T2[check_service_status]
  AG -.-> T3[request_credit — restricted]
  T3 --> HR[Human approval]
  AG --> LOG[(Tool-call log)]
```

## Related reference architectures

- [Single agent](../../architectures/single-agent.md)

## To be written

- [ ] Component-by-component explanation
- [ ] Deployment options (local, cloud, hybrid) and trade-offs
- [ ] Scaling and resilience notes
