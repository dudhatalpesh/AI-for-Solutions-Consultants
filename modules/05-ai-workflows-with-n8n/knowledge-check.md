# Module 05 — Knowledge Check

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

## Questions

1. When do you prefer a workflow over an agent?
2. What does an Error Trigger workflow do?
3. How does the Wait node resume on approval?

## Answers

1. When steps are known and predictable.
2. Runs when another workflow fails, for logging and alerting.
3. Via a call to the execution's resume URL (On Webhook Call).
