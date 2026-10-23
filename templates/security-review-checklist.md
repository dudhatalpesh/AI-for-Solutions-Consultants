# AI Security Review Checklist

> **Status: outline.** Structure is ready to use; worked examples are tracked in [docs/11-suggested-first-issues.md](../docs/11-suggested-first-issues.md) (issue #14).

For a customer's AI design or a POC before go-live. Mapped to the OWASP Top 10 for LLM Applications (2025). Mark ✅ / ❌ / N/A with notes.

## Architecture and data
- [ ] Data-flow diagram with trust boundaries exists
- [ ] Data classification for prompts, retrieved content, outputs and logs
- [ ] Data residency and provider terms reviewed (retention, training use, subprocessors)

## LLM01 Prompt injection
- [ ] Input screening; instructions separated from data; retrieved content sanitised
- [ ] Consequential actions require approval regardless of model output

## LLM02 Sensitive information disclosure
- [ ] Retrieval enforces user entitlements
- [ ] Redaction before model calls and logging; output scanning

## LLM03 Supply chain / LLM04 Data and model poisoning
- [ ] Approved models, nodes and packages; pinned versions; provenance checked
- [ ] Ingestion sources controlled and reviewed

## LLM05 Improper output handling
- [ ] Outputs validated against schemas; escaped before rendering; never executed

## LLM06 Excessive agency
- [ ] Minimal tools; least-privilege credentials; approvals; value limits; audit

## LLM07 System prompt leakage
- [ ] No secrets or sensitive logic in prompts

## LLM08 Vector and embedding weaknesses
- [ ] Index write access controlled; per-tenant or per-classification separation

## LLM09 Misinformation
- [ ] Grounding, citations, refusal behaviour, evaluation results

## LLM10 Unbounded consumption
- [ ] Input limits, iteration caps, timeouts, budgets and alerts

## Operations
- [ ] Logging to SIEM (redacted); alerting on guard events and anomalies
- [ ] Red-team results reviewed; critical findings fixed
- [ ] AI incident response runbook

Related: [risk register](risk-register.md) · [AI security playbook](../docs/06-ai-security-playbook.md) · [n8n workflow design review](n8n-workflow-design-review-checklist.md)
