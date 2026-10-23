# AI Red-Team Findings Report — <System name>

**Classification:** Confidential · **Version:** 0.1 · **Date:** YYYY-MM-DD · **Tester:** <name> · **Authorised by:** <name>

## 1. Executive summary

- Scope tested and dates.
- Overall risk rating: Critical / High / Medium / Low.
- Top three findings in one line each, with business impact.
- Headline recommendation.

## 2. Scope and method

| Item | Detail |
|---|---|
| Target(s) | e.g. `lab10-secure-rag` workflow, n8n 2.x, model `llama3.2` |
| Out of scope | e.g. infrastructure, identity provider |
| Approach | Threat model → automated cases (n8n harness, Python runner) → manual exploration |
| Test cases | `attack-cases.jsonl` (10 cases) + manual cases |
| Repeats | Each case run N times; fail if any run fails |

## 3. Threat model summary

Attach the data-flow diagram with trust boundaries and the STRIDE + OWASP LLM mapping.

## 4. Severity definitions

| Severity | Definition |
|---|---|
| Critical | Exploitable remotely, leads to sensitive-data exposure or unauthorised action at scale |
| High | Sensitive data exposure, system prompt or secret leakage, or unauthorised action in specific conditions |
| Medium | Policy bypass or unsafe output with limited impact or requiring user interaction |
| Low | Minor issue, defence-in-depth gap |
| Info | Observation, no direct risk |

## 5. Results overview

| ID | Category | OWASP | Severity | Vulnerable target | Hardened target |
|---|---|---|---|---|---|
| RT-01 | Direct injection | LLM01 | High | FAIL | PASS |
| … | | | | | |

## 6. Findings

### F-01 <Title>

| | |
|---|---|
| Severity | High |
| OWASP | LLM01 |
| Affected component | e.g. Sanitise Context node |
| Status | Open / Fixed / Accepted |

**Description:** what is wrong.
**Reproduction:** exact request(s), role, number of attempts, success rate.
**Evidence:** response excerpt (redacted), execution ID.
**Impact:** business consequence.
**Recommendation:** specific control(s).
**Retest result:** date, outcome.

## 7. Residual risk and acceptance

| Risk | Residual rating | Owner | Accepted until |
|---|---|---|---|

## 8. Appendix

- Full results CSV
- Tool versions (n8n, model, harness commit)
