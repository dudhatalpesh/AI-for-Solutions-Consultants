# Reference Architecture — Multi-Agent

> **Status: outline.** Diagram and key design points are in place; full narrative is tracked in [docs/11-suggested-first-issues.md](../docs/11-suggested-first-issues.md).

**Use when:** a task benefits from distinct roles (plan, research, critique, write) and a single agent measurably underperforms.
**Built in:** [Lab 08](../labs/lab-08-n8n-multi-agent-research-assistant/README.md) · [workflow 07](../n8n-workflows/07-multi-agent-orchestration.json)

```mermaid
flowchart TB
  T[Task] --> P[Planner]
  P --> W1[Worker 1]
  P --> W2[Worker 2]
  P --> W3[Worker 3]
  W1 --> AGG[Aggregator<br/>fallbacks]
  W2 --> AGG
  W3 --> AGG
  AGG --> C[Critic]
  C -->|low confidence, once| P
  C --> H{Human review}
  H --> OUT[Writer / output]
```

## Patterns in n8n

| Pattern | n8n implementation |
|---|---|
| Pipeline | Sequential chains or agents connected by main connections |
| Fan-out / fan-in | Code node splits items; Code node aggregates |
| Agent-as-tool | **Call n8n Sub-Workflow Tool** attached to a coordinator AI Agent |
| Human gate | Wait node (webhook or form) or n8n human review for tools |

## Watch-outs

Cost and latency multiply; errors compound; loops need hard limits; accountability needs per-agent logging.
