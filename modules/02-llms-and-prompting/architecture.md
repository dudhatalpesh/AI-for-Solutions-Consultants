# Module 02 — Architecture

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

```mermaid
flowchart LR
  U[Streamlit UI or curl] --> WH[n8n Webhook]
  WH --> SW{Switch: prompt variant}
  SW --> CH[Basic LLM Chain]
  CH -.-> M[Ollama Chat Model]
  CH --> R[Respond + log latency]
```

## Related reference architectures

- [Conversational AI](../../architectures/conversational-ai.md)
- [AI gateway](../../architectures/ai-gateway.md)

## To be written

- [ ] Component-by-component explanation
- [ ] Deployment options (local, cloud, hybrid) and trade-offs
- [ ] Scaling and resilience notes
