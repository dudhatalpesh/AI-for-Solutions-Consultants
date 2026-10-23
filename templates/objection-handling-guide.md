# Objection-Handling Guide

> **Status: outline.** Structure is ready to use; worked examples are tracked in [docs/11-suggested-first-issues.md](../docs/11-suggested-first-issues.md) (issue #14).

Method: **Acknowledge → Clarify → Respond with evidence → Confirm.**

| Objection | Clarifying question | Response | Evidence to show |
|---|---|---|---|
| "AI makes things up." | "Where would a wrong answer hurt most?" | Grounding, citations, refusal, evaluation, human review | Lab 04 eval results |
| "Our data can't leave the building." | "Which data classes, and which regulations?" | Local models; hybrid routing by classification | Lab 01, hybrid architecture |
| "Agents are too risky." | "What's the worst action you're worried about?" | Least privilege, approvals, audit; start read-only | Lab 07 + Lab 09 |
| "Costs are unpredictable." | "What volume and budget range?" | Measure tokens per transaction; caps and alerts | Lab 12 telemetry |
| "Prompt injection can't be solved." | "Which systems would the AI touch?" | Correct — so limit impact: layered controls, red team | Lab 10 + Lab 11 |
| "We'll wait for the market to settle." | "What would need to be true to start?" | Process, data and governance work is durable; small POC now | Readiness assessment |
| "Low-code isn't enterprise-grade." | "What standards must a platform meet?" | Self-hosting, credentials, RBAC/SSO on paid plans (check), Git, queue mode | n8n reference architectures |
| "We already have Copilot / ChatGPT Enterprise." | "Which business processes does it automate end to end?" | Complementary: process automation, integrations, governed agents | Use-case matrix |

## To be written
- [ ] Persona-specific variants (CIO, CISO, CFO, DPO)
