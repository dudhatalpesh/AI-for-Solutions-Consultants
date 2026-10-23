# Module 10 — Customer Conversation Prompts

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

## Discovery questions

1. How will you decide the POC succeeded?
2. Who reviews AI quality after go-live?
3. What latency do users tolerate?
4. How do you allocate AI cost to teams?

## Executive explanation (60 seconds)

> We measure AI like any other service: quality, cost, speed and safety, on a fixed test set and in production. That evidence drives go/no-go and model choices, not anecdotes.

## Objections and responses

| Objection | Response |
|---|---|
| We'll know it works when users like it | User feedback is one signal; it's slow and biased. A golden dataset gives fast, repeatable evidence. |
| Monitoring tools are expensive | The POC uses n8n and Postgres; you can adopt a dedicated LLM observability tool later. |
