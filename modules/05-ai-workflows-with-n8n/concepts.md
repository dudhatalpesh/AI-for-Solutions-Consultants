# Module 05 — Concepts

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

## Key concepts to cover

- Deterministic steps vs model decisions
- Idempotency and duplicate handling
- Retries and backoff; error outputs; Error Trigger workflows
- Exception queues and human review
- Integrations: email, calendar, ticketing, CRM, Sheets, Slack, Teams, Drive, SharePoint (free/sample access where feasible)
- Audit logging

## Failure modes

- Misclassification sends items to the wrong queue
- Duplicate processing on retries
- Silent failures without alerts
- Approvals that never time out

## To be written

- [ ] Plain-English explanation of each concept with an SC-relevant example
- [ ] One comparison table and one Mermaid diagram per major concept
- [ ] Acronyms expanded on first use
