# n8n Reference Architectures

> **Status: outline.** Diagram and key design points are in place; full narrative is tracked in [docs/11-suggested-first-issues.md](../docs/11-suggested-first-issues.md).

How to deploy and operate n8n for AI workloads, from laptop to production. See also [03 — n8n setup and operations guide](../docs/03-n8n-setup-and-operations-guide.md).

## 1. Lab / POC (this repo)

```mermaid
flowchart LR
  subgraph Host[Single host - Docker Compose]
    N[n8n] --> PG[(Postgres)]
    N --> O[Ollama]
    N --> Q[(Qdrant)]
    N --> MP[Mailpit]
  end
```

## 2. Production — single instance, hardened

```mermaid
flowchart LR
  U[Users / systems] --> RP[Reverse proxy<br/>TLS, SSO, WAF]
  RP --> N[n8n main]
  N --> PG[(Managed Postgres<br/>backups)]
  N --> TR[Task runners<br/>isolated]
  N --> SM[Secrets manager]
  N --> GW[AI gateway] --> M[Models]
  N --> SIEM[(Logs / SIEM)]
```

## 3. Production — queue mode (scale-out)

```mermaid
flowchart LR
  RP[Reverse proxy] --> MAIN[n8n main<br/>UI, API]
  RP --> WHK[n8n webhook processors]
  MAIN --> R[(Redis queue)]
  WHK --> R
  R --> W1[Worker 1]
  R --> W2[Worker 2]
  R --> W3[Worker N]
  W1 --> PG[(Postgres)]
  W2 --> PG
  W3 --> PG
  MAIN --> PG
```

Check the current [n8n scaling docs](https://docs.n8n.io/hosting/scaling/overview/) for queue-mode configuration and supported options.

## Operational checklist

Pinned image versions; staged upgrades with smoke tests; backups (database, encryption key, workflows in Git); execution data retention; an error workflow on every production workflow; monitoring of queue depth, failures and latency; environment separation (dev/test/prod) with workflow promotion via Git or export/import.
