# AI Risk Register

**System:** ________ · **Owner:** ________ · **Version:** ____ · **Last reviewed:** ________ · **Next review:** ________

## Rating scales

**Likelihood (L):** 1 Rare · 2 Unlikely · 3 Possible · 4 Likely · 5 Almost certain
**Impact (I):** 1 Negligible · 2 Minor · 3 Moderate · 4 Major · 5 Severe
**Score = L × I:** 1–4 Low · 5–9 Medium · 10–16 High · 20–25 Critical

Rate inherent risk (before controls) and residual risk (after controls). The risk owner accepts the residual risk in writing.

## Register

| ID | Risk (cause → event → consequence) | Category | OWASP LLM / framework ref | Inherent L | Inherent I | Inherent score | Controls (existing / planned) | Residual L | Residual I | Residual score | Owner | Status | Review date |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R01 | Malicious instructions in a retrieved document → model follows them → wrong or harmful answer | Security | LLM01 | 4 | 4 | 16 High | Context sanitisation; delimiting; output guard; red-team regression | 2 | 4 | 8 Medium | CISO delegate | Open | |
| R02 | Retrieval ignores user permissions → confidential content shown to unauthorised users | Security / privacy | LLM02, LLM08 | 3 | 5 | 15 High | Entitlement filter at retrieval; ACL metadata at ingestion; tests per role | 1 | 5 | 5 Medium | Data owner | Open | |
| R03 | Model states incorrect policy confidently → employee acts on it | Quality | LLM09 | 4 | 3 | 12 High | Grounding + citations; insufficient-context refusal; eval ≥ 85%; feedback loop | 2 | 3 | 6 Medium | Process owner | Open | |
| R04 | Agent tool with broad credential → unintended action (for example a refund) | Security | LLM06 | 3 | 4 | 12 High | Restricted tools; approval workflow; value caps; scoped credentials; audit log | 1 | 4 | 4 Low | App owner | Open | |
| R05 | Prompts and outputs with personal data stored in execution logs → privacy breach / retention violation | Privacy | LLM02 | 4 | 3 | 12 High | Redaction before logging; execution data pruning; access control; DPIA | 2 | 3 | 6 Medium | DPO | Open | |
| R06 | Model output rendered unescaped → script injection in the UI | Security | LLM05 | 3 | 3 | 9 Medium | HTML escaping; schema validation; CSP (Content Security Policy) | 1 | 3 | 3 Low | App owner | Open | |
| R07 | Unbounded inputs or agent loops → cost spike / outage | Operational | LLM10 | 3 | 3 | 9 Medium | Length limits; max iterations; timeouts; budgets and alerts | 1 | 3 | 3 Low | Platform owner | Open | |
| R08 | Unvetted community node or model file → supply-chain compromise | Security | LLM03 | 2 | 5 | 10 High | Approved node/model list; pinned versions; scanning | 1 | 5 | 5 Medium | Platform owner | Open | |
| R09 | Cloud provider changes model or terms → quality drop or compliance gap | Vendor | NIST AI RMF (Manage) | 3 | 3 | 9 Medium | Pinned model versions; eval on change; contract terms; local fallback | 2 | 3 | 6 Medium | Procurement | Open | |
| R10 | Users rely on the AI for decisions outside its scope → harm | Responsible AI | NIST AI RMF (Map) | 3 | 4 | 12 High | Clear scope disclosure; refusal rules; training; human review for high-impact decisions | 2 | 3 | 6 Medium | Business owner | Open | |
| R11 | | | | | | | | | | | | | |

## Risk acceptance

| ID | Residual score | Accepted by (name, role) | Date | Conditions / expiry |
|---|---|---|---|---|
| | | | | |

## Review cadence

- Before POC start, before pilot, before production, and quarterly after go-live.
- Also on any model change, new tool or integration, new data source, or security incident.

Related: [security review checklist](security-review-checklist.md) · [responsible AI checklist](responsible-ai-checklist.md) · [AI security playbook](../docs/06-ai-security-playbook.md)
