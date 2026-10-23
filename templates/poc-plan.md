# AI Proof of Concept (POC) Plan

**Customer:** ________ · **Use case:** ________ · **Version:** 0.1 · **Date:** ________
**Customer sponsor:** ________ · **Customer technical lead:** ________ · **Vendor/partner SC:** ________

> A POC proves value and feasibility against criteria agreed **before** building. It is not a pilot and not production. Keep it to 2–6 weeks.

## 1. Objective

One or two sentences: *"Prove that [solution] can [outcome] for [users] with [quality/safety level], using [data], within [constraints]."*

## 2. Scope

| In scope | Out of scope |
|---|---|
| e.g. IT policy Q&A for 50 pilot users | HR and legal content |
| e.g. 200 documents from the policy library | Real-time sync with SharePoint |
| e.g. local model (Ollama) + n8n orchestration | Production deployment, SSO integration |

## 3. Success criteria (agreed and signed)

| # | Dimension | Metric | How measured | Target | Must / Should |
|---|---|---|---|---|---|
| S1 | Quality | Correct answers on golden set | Eval run on ≥ 50 questions | ≥ 85% | Must |
| S2 | Grounding | Answers with valid citation | Eval run | ≥ 95% | Must |
| S3 | Safety | Critical red-team cases blocked | Red-team suite (Lab 11 method) | 100% | Must |
| S4 | Safety | Correct refusal on out-of-scope questions | Eval run | ≥ 90% | Should |
| S5 | Latency | p95 response time | Telemetry | < 8 s | Should |
| S6 | Cost | Estimated cost per query at production volume | Telemetry × pricing | < [current manual cost] | Should |
| S7 | Adoption | Pilot users rating answers useful | In-app feedback | ≥ 70% positive | Should |

Decision rule: **all Must** criteria met → recommend proceeding to pilot.

## 4. Solution approach

- Architecture diagram (attach or link; see [reference architectures](../architectures/enterprise-rag.md)).
- Components and hosting (for example n8n, Ollama, Qdrant on customer VM).
- Data flow and trust boundaries.
- Security controls in place for the POC.

## 5. Data

| Source | Owner | Classification | Volume | Access method | Approved by |
|---|---|---|---|---|---|
| | | | | | |

Rules: minimum data necessary; synthetic or de-identified where possible; data deleted at POC end (date: ____).

## 6. Evaluation plan

1. Golden dataset: ___ questions/documents with expected answers, created by ___ (customer SMEs) by ___.
2. Red-team suite: categories and number of cases.
3. Baseline: current process metrics (time, error rate, cost) measured by ___.
4. Runs: baseline at end of week 2; final at week 4; results shared in a readout.

## 7. Timeline

| Week | Activities | Milestone |
|---|---|---|
| 0 | Kick-off, access, success criteria sign-off | Criteria signed |
| 1 | Environment, data ingestion, first workflow | First answer end to end |
| 2 | Iterate prompts/retrieval; build eval set; first eval | Baseline eval |
| 3 | Guardrails, red team, telemetry, user pilot | Security results |
| 4 | Final eval, cost model, readout, business case | Go/no-go readout |

## 8. Roles and RACI

R = Responsible, A = Accountable, C = Consulted, I = Informed.

| Activity | Customer sponsor | Customer tech lead | Customer security | SC / partner |
|---|---|---|---|---|
| Success criteria | A | C | C | R |
| Data access | I | A/R | C | C |
| Build | I | C | I | A/R |
| Security review | I | C | A/R | R |
| Eval dataset | C | A | I | R |
| Readout | A | C | C | R |

## 9. Risks and mitigations

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Data access delayed | M | H | Start with synthetic data; escalate by day 3 | Tech lead |
| Golden set not ready | M | H | SC drafts; SMEs review | Sponsor |
| Local model quality insufficient | M | M | Compare with approved cloud model on same eval set | SC |
| Scope creep | H | M | Change requests go to the sponsor; defer to pilot | Sponsor |

Log ongoing risks in the [risk register](risk-register.md).

## 10. Exit and next steps

- Readout deliverables: results vs criteria, architecture, risk register, cost model, recommendation.
- If successful: pilot plan (users, duration, production controls such as SSO, monitoring and support).
- If not: lessons learned, alternative approaches.
- Clean-up: delete POC data and credentials by ____.

**Sign-off:** Customer sponsor ________ Date ____ · SC ________ Date ____
