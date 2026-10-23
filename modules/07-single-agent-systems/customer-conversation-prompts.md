# Module 07 — Customer Conversation Prompts

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

## Discovery questions

1. Which systems would the agent need to read? To write?
2. What is the worst action it could take?
3. Who approves consequential actions?
4. What audit evidence do you need?

## Executive explanation (60 seconds)

> An agent is an assistant that can use tools. We give it the smallest set of tools it needs, make it ask permission before anything consequential, and log every action — so you get speed without losing control.

## Objections and responses

| Objection | Response |
|---|---|
| Agents are too risky | Unconstrained ones are. We design least privilege, approvals and audit from the start, and start read-only. |
| Can't a script do this? | Often yes — and then we use a workflow. Agents earn their place when inputs are varied and the path isn't known in advance. |
