# Module 13 — n8n Lab

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

**Lab (in this module):** build an **AI inventory and approval workflow**:

1. **Form Trigger** (or Webhook) to register a use case: owner, purpose, data classes, model, vendor, autonomy level.
2. **Code**: compute a risk tier from the answers.
3. **Postgres**: insert into an inventory table.
4. **IF** high tier → **Send Email** to the review board → **Wait** for decision → update status.
5. **Schedule Trigger** monthly → query inventory → email a risk summary.

Check current docs for the Form Trigger node's options. Full instructions tracked in [issue #15](../../docs/11-suggested-first-issues.md).
