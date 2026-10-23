# Reference Architecture — Hybrid Cloud / Local AI

> **Status: outline.** Diagram and key design points are in place; full narrative is tracked in [docs/11-suggested-first-issues.md](../docs/11-suggested-first-issues.md).

**Use when:** some data must stay on-premises or in-region while other workloads benefit from frontier cloud models.

```mermaid
flowchart LR
  subgraph OnPrem[Customer environment]
    APP[Apps + n8n] --> CLS[Classify request<br/>data sensitivity]
    CLS -->|restricted / regulated| LOC[Local models<br/>Ollama / GPU servers]
    KB[(Local vector DB)] --> APP
  end
  CLS -->|general / public| GWY[Egress via AI gateway<br/>DLP, logging]
  GWY --> CLD[Cloud model APIs<br/>approved providers and regions]
```

## Routing policy example

| Data class | Allowed models | Logging |
|---|---|---|
| Public | Local or approved cloud | Standard |
| Internal | Local, or cloud with enterprise terms (no training on data, defined retention — verify with the provider) | Redacted |
| Confidential / regulated | Local only | Redacted, restricted access |

## Trade-offs

Quality vs control; GPU capital cost vs per-token operating cost; operational burden of local models; latency; vendor lock-in. Decide with the same evaluation set run on both routes.
