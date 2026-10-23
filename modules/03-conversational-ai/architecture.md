# Module 03 — Architecture

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

```mermaid
flowchart LR
  U[User] --> CT[Chat Trigger]
  CT --> AG[AI Agent]
  AG -.-> M[Ollama Chat Model]
  AG -.-> MEM[Simple Memory]
  AG -.-> T1[FAQ tool]
  AG -.-> T2[Escalation tool]
  T2 --> Q[(Human queue)]
```

## Related reference architectures

- [Conversational AI](../../architectures/conversational-ai.md)

## To be written

- [ ] Component-by-component explanation
- [ ] Deployment options (local, cloud, hybrid) and trade-offs
- [ ] Scaling and resilience notes
