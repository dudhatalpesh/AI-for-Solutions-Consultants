# Module 08 — Customer Conversation Prompts

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

## Discovery questions

1. What does a good output look like, and who signs it off?
2. How long does this task take a person today?
3. What sources are allowed?
4. What's the tolerance for cost per run?

## Executive explanation (60 seconds)

> Multi-agent designs split a complex task into roles — plan, research, review, write — like a small team. We use them only where they measurably beat a simpler design, with a human approving the final output.

## Objections and responses

| Objection | Response |
|---|---|
| More agents means better results | Not automatically. Each hand-off adds cost and error. We test single vs multi-agent on the same evaluation set. |
| This is too slow | Parallelise research and use smaller models for simple roles. |
