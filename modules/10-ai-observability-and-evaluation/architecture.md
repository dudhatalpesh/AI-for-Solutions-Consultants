# Module 10 — Architecture

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

```mermaid
flowchart LR
  WF[AI workflows] -->|POST /ai-log| LG[Log workflow] --> DB[(lab.llm_calls)]
  SCH[Schedule hourly] --> AGG[Aggregate metrics] --> TH{Threshold?}
  TH -->|breach| AL[Alert email]
  ERR[Error Trigger] --> DB2[(lab.workflow_errors)]
```

## Related reference architectures

- [AI gateway](../../architectures/ai-gateway.md)
- [Secure AI reference architecture](../../architectures/secure-ai-reference-architecture.md)

## To be written

- [ ] Component-by-component explanation
- [ ] Deployment options (local, cloud, hybrid) and trade-offs
- [ ] Scaling and resilience notes
