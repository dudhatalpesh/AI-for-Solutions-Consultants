# Module 09 — Customer Conversation Prompts

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

## Discovery questions

1. Where must AI workloads run: on-prem, private cloud, public cloud?
2. Which teams will consume AI services?
3. How do you handle API gateways and identity today?
4. What are your RPO/RTO expectations for this service?

## Executive explanation (60 seconds)

> We centralise AI access through a gateway so every app gets the same security, logging and cost controls, and we can switch models without rewriting apps. Sensitive data stays on local models by policy.

## Objections and responses

| Objection | Response |
|---|---|
| A gateway adds latency | Milliseconds, versus the seconds a model call takes; the control and visibility are worth it. |
| We'll standardise on one model vendor | Fine for now; a gateway keeps the option to switch as models and prices change. |
