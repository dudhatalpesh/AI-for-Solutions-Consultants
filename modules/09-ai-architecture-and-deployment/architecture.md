# Module 09 — Architecture

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

```mermaid
flowchart LR
  APPS[Apps / workflows] --> GW[n8n AI gateway]
  GW --> POL{Policy: data class}
  POL -->|restricted| LOC[Ollama local]
  POL -->|general| CLD[Approved cloud model]
  GW --> LOG[(Usage + cost log)]
  GW --> RAG[FastAPI RAG service] --> QD[(Qdrant)]
```

## Related reference architectures

- [AI gateway](../../architectures/ai-gateway.md)
- [Hybrid cloud/local AI](../../architectures/hybrid-cloud-local-ai.md)
- [n8n reference architectures](../../architectures/n8n-reference-architectures.md)

## To be written

- [ ] Component-by-component explanation
- [ ] Deployment options (local, cloud, hybrid) and trade-offs
- [ ] Scaling and resilience notes
