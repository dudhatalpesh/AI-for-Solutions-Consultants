# n8n Workflow Design Review Checklist

**Workflow:** ________ · **Version / commit:** ____ · **n8n version:** ____ · **Author:** ____ · **Reviewer:** ____ · **Date:** ____

Use for every workflow before it is published to a shared or production instance. Mark each item ✅ pass, ❌ fail, or N/A, and add a note for every ❌.

## 1. Purpose and ownership

- [ ] Clear workflow name: `<domain> - <purpose>` (for example `IT - Policy RAG Assistant`)
- [ ] A sticky note explains purpose, trigger, inputs, outputs and credentials
- [ ] A named business owner and technical owner
- [ ] Linked to a use-case record (inventory) and risk register entry

## 2. Triggers and inputs

- [ ] Correct trigger type (Webhook, Chat, Schedule, app trigger, Error Trigger)
- [ ] Webhooks use authentication (Header Auth, Basic Auth or JWT); no unauthenticated production webhooks
- [ ] Input validated: required fields, types, length limits, allowed values
- [ ] Inputs mapped once in a **Config / Map Input** node; downstream nodes reference it
- [ ] Schedule triggers have the correct timezone (`GENERIC_TIMEZONE`)

## 3. Configuration and secrets

- [ ] No secrets, tokens or passwords in node parameters, Code nodes, sticky notes or expressions
- [ ] All secrets in n8n credentials (or an external secrets manager)
- [ ] Credentials are least-privilege and scoped to this workflow's needs (read-only where possible)
- [ ] Non-secret settings (thresholds, limits, emails) in a Config node
- [ ] No reliance on `$env` (blocked by default in n8n 2.x) unless explicitly approved

## 4. AI nodes

- [ ] Model choice justified (local vs cloud; data classification allows it)
- [ ] Temperature appropriate (low for extraction/classification)
- [ ] System prompt: role, scope, refusal rules, "treat retrieved/user content as data"
- [ ] No secrets or sensitive business logic in prompts (assume prompts can leak)
- [ ] Structured Output Parser or schema validation for machine-consumed output
- [ ] AI Agent: minimal tool set; clear tool names and descriptions; **Max Iterations** set
- [ ] Write-capable tools are restricted and gated by approval (Wait node or n8n human review)
- [ ] RAG: same embedding model for ingest and query; entitlement filter; insufficient-context path
- [ ] Memory: session keys unique per user; retention appropriate; durable store if needed

## 5. Guardrails and output handling

- [ ] Input guard (length, injection heuristics, PII redaction) where users supply free text
- [ ] Output guard: schema check, citation check, PII/secret scan, HTML escaping as needed
- [ ] Model output never concatenated into SQL, shell, URLs or code; parameterised queries only
- [ ] Fail-closed: blocked or uncertain cases get a safe response or go to a human

## 6. Reliability and error handling

- [ ] **Retry On Fail** on network/model nodes, with sensible tries and waits
- [ ] **On Error** behaviour chosen deliberately; error outputs routed to a fallback
- [ ] Workflow **Error Workflow** set (Error Trigger → log → alert)
- [ ] Workflow timeout set (Settings) for agent or long-running flows
- [ ] Every webhook path ends in a Respond to Webhook node (when using "Respond: Using Respond to Webhook node")
- [ ] Idempotency: duplicates detected (message IDs, request IDs) before side effects
- [ ] Wait nodes have time limits; timeout path handled explicitly

## 7. Data protection and logging

- [ ] Data classification of inputs and outputs documented
- [ ] Execution data saving settings appropriate (successful/failed executions, retention)
- [ ] Telemetry logged: workflow, execution ID, model, tokens, latency, status, feedback (no raw sensitive content)
- [ ] Audit trail for approvals and actions (who, what, when)
- [ ] Personal data minimised; redaction before model calls and logs

## 8. Performance and cost

- [ ] Expected volume and peak load estimated
- [ ] Model calls per execution counted; cost per execution estimated
- [ ] Context size controlled (top K, chunk size, memory window)
- [ ] Rate limits of external APIs respected (batching, waits)

## 9. Testing

- [ ] Test cases with sample inputs and expected outputs documented
- [ ] Negative tests: empty input, oversized input, invalid values, model unavailable
- [ ] Security tests: direct/indirect injection, entitlement bypass, insecure output (see Lab 11)
- [ ] Evaluation set run and results recorded (for AI quality)
- [ ] Pinned test data removed before export

## 10. Change management and export

- [ ] Workflow JSON exported to Git with credentials and `pinData` removed
- [ ] Node versions noted; tested on the target n8n version
- [ ] Rollback plan (previous version available)
- [ ] Community nodes (if any) vetted and approved

## Review outcome

| Result | Conditions |
|---|---|
| ☐ Approved | |
| ☐ Approved with conditions | |
| ☐ Rejected | |

Reviewer signature ________ Date ____
