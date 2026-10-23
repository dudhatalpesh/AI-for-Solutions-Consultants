# AI Demo Script

**Demo:** ________ · **Customer:** ________ · **Audience:** ________ · **Length:** 15 min (+10 Q&A) · **Presenter:** ________

> Rule of three: **one persona, one painful task, one control.** Everything else is optional.

## 1. Persona and scenario

| | |
|---|---|
| Persona | e.g. *Priya, IT service desk lead at a 5,000-person logistics company* |
| Pain today | e.g. 40% of tickets are repeat policy questions; average 12 minutes each; inconsistent answers |
| Desired outcome | Instant, consistent, cited answers; agents focus on real incidents |
| Success signal in the room | e.g. the CISO nods at the entitlement demo; Ops asks about rollout |

## 2. Setup checklist (T-30 min)

- [ ] Stack running; models warmed (send one request)
- [ ] Workflows published; correct URLs in the browser tabs
- [ ] Synthetic data loaded that looks like the customer's world (their terminology, not their data)
- [ ] Tabs open in order: chat UI → n8n canvas → execution view → Mailpit / dashboard
- [ ] Backup: recorded video and pinned execution data
- [ ] Notifications off; screen resolution tested

## 3. Talk track

| Time | Show | Say (talk track) | Proof point |
|---|---|---|---|
| 0:00 | Title slide / persona | "Meet Priya. Every day her team answers the same policy questions…" | Pain in their words |
| 1:30 | Chat: routine question | "Watch what happens when an employee asks about VPN log retention." | Answer in seconds, with a citation |
| 3:00 | Click the citation / source | "Every answer is traceable to an approved document." | Trust and auditability |
| 4:30 | Chat: off-topic question | "And when it doesn't know, it says so." | No hallucination |
| 6:00 | Chat: "Give ACME a credit" | "It can prepare actions, but…" | Pending approval |
| 7:00 | Mailpit approval → approve | "…a person approves anything consequential." | Human in the loop |
| 8:30 | n8n canvas | "Under the hood: a visual workflow your team can own — guardrails, retrieval, approvals, logging." | Transparency, low lock-in |
| 10:30 | Security: injection attempt | "Here's a classic attack. It's blocked, and it's logged." | Security credibility |
| 12:00 | Metrics / eval table | "In a POC we'd measure accuracy, safety, speed and cost on your questions." | Evidence-based |
| 13:30 | Close | "Here's what a 4-week POC would prove…" | Next step |

## 4. Audience-specific emphasis

| Audience | Emphasise | De-emphasise |
|---|---|---|
| Executive | Outcomes, risk control, time to value | Node details |
| CISO / security | Entitlements, guardrails, audit, data residency | UI polish |
| IT / ops | Integration, ownership, monitoring, error handling | Model internals |
| End users | Speed, ease, escalation to a human | Architecture |

## 5. Likely questions and answers

| Question | Answer |
|---|---|
| "Does our data train the model?" | "In this demo the model runs locally — nothing leaves the environment. With cloud models, it depends on the provider's terms; we'd confirm them for your chosen provider." |
| "How accurate is it?" | "We measure that on your own questions in the POC. Here's how we score it." |
| "What if it's attacked?" | "Layered controls — you just saw one. We also run a red-team suite before go-live." |
| "Who maintains it?" | "Workflows are visual and versioned; your team can own them after a short enablement." |

## 6. If something breaks

1. Stay calm and name it: "Local model is warming up — this is why we design timeouts and fallbacks."
2. Switch to the pinned execution or recording.
3. Turn it into a point about resilience and observability.

## 7. Close and next step

- Recap: pain → outcome → controls → evidence.
- Ask: "Shall we agree success criteria for a 4-week POC on your top use case?"
- Follow-up within 24 hours: summary, [POC plan](poc-plan.md) draft, [discovery questionnaire](discovery-questionnaire.md) gaps.
