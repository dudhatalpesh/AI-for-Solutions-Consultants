# AI Discovery Questionnaire

**Customer:** ____________ · **Date:** ________ · **SC:** ________ · **Attendees (roles):** ________

How to use:

1. Send sections 1–3 ahead of the call. Cover sections 4–9 live.
2. Don't read it out like a form. Pick the 10–15 questions that matter for this customer.
3. Record answers in the customer's own words. Mark unknowns as **TBD**, with an owner.
4. Never record personal data or confidential details you don't need. Use this template to qualify the opportunity, not to collect data.

---

## 1. Business context

| # | Question | Answer |
|---|---|---|
| 1.1 | What business outcomes matter most this year (revenue, cost, risk, customer experience)? | |
| 1.2 | Which processes cause the most manual effort, delay or errors? | |
| 1.3 | Who owns those processes? Who feels the pain day to day? | |
| 1.4 | What has already been tried, and why didn't it work? | |
| 1.5 | What happens if nothing changes in the next 12 months? | |

## 2. AI use and strategy today

| # | Question | Answer |
|---|---|---|
| 2.1 | Which AI tools are teams using today, official and unofficial ("shadow AI")? | |
| 2.2 | Is there an AI strategy, an AI policy, or an AI council? Who leads it? | |
| 2.3 | Which models or platforms are approved (cloud providers, open models)? | |
| 2.4 | Any AI projects in production? What did you learn from them? | |
| 2.5 | What worries leadership most about AI: risk, cost, accuracy, skills, or vendor lock-in? | |

## 3. Use-case qualification

Fill in one block per candidate use case.

| # | Question | Answer |
|---|---|---|
| 3.1 | Describe the use case in one sentence: who, does what, with what, to achieve what. | |
| 3.2 | Category: conversational AI / document AI / workflow automation / agentic AI | |
| 3.3 | Volume: requests, documents or tickets per day/month | |
| 3.4 | Current handling time and cost per item | |
| 3.5 | Current error rate, and the cost of an error | |
| 3.6 | What does "good" look like? How would you measure it in 90 days? | |
| 3.7 | What autonomy is acceptable: suggest only / act with approval / act autonomously? | |
| 3.8 | Worst-case outcome if the AI is wrong. Who is harmed? | |

## 4. Data

| # | Question | Answer |
|---|---|---|
| 4.1 | Which data sources are needed (systems, file shares, wikis, tickets, email)? | |
| 4.2 | Who owns each source? Is the content current and accurate? | |
| 4.3 | Data formats: structured, PDFs, scans, images, audio? | |
| 4.4 | Classification: public / internal / confidential / regulated? | |
| 4.5 | Does it contain personal data, health data, payment data or trade secrets? | |
| 4.6 | Are permissions different for different users? How are they enforced today? | |
| 4.7 | Residency or sovereignty constraints (country or region)? | |
| 4.8 | Retention rules for prompts, outputs and logs? | |

## 5. Integration and workflow

| # | Question | Answer |
|---|---|---|
| 5.1 | Which systems must the solution read from? Write to? | |
| 5.2 | Are APIs available? Authentication method (OAuth, API key, service account)? | |
| 5.3 | Which collaboration channels do users live in (Teams, Slack, email, portal)? | |
| 5.4 | Existing automation or iPaaS (integration platform) tools: n8n, Power Automate, MuleSoft, other? | |
| 5.5 | Where must a human approve or review? | |
| 5.6 | How are exceptions handled today? | |

## 6. Architecture and deployment

| # | Question | Answer |
|---|---|---|
| 6.1 | Hosting preference: SaaS, customer cloud (which), on-premises, hybrid? | |
| 6.2 | GPU availability or plans for local models? | |
| 6.3 | Identity provider and SSO? | |
| 6.4 | Network constraints: egress restrictions, proxies, SASE/SSE platform? | |
| 6.5 | Observability and SIEM tooling where AI logs should go? | |
| 6.6 | Latency and availability expectations? | |

## 7. Security, risk and compliance

| # | Question | Answer |
|---|---|---|
| 7.1 | Who must approve AI projects (CISO, DPO, legal, risk, works council)? | |
| 7.2 | Applicable regulations and frameworks (e.g. GDPR, HIPAA, PCI DSS, SOC 2, ISO/IEC 27001, ISO/IEC 42001, EU AI Act)? | |
| 7.3 | Requirements for third-party model providers (no training on data, retention, certifications)? | |
| 7.4 | Has the security team assessed prompt injection, data leakage and agent risks before? | |
| 7.5 | Is AI red teaming or security testing required before go-live? | |
| 7.6 | Incident response expectations for AI-related incidents? | |

## 8. People and change

| # | Question | Answer |
|---|---|---|
| 8.1 | Who are the end users, and how comfortable are they with AI? | |
| 8.2 | Who will own and maintain the solution after go-live? | |
| 8.3 | What training or change management is needed? | |
| 8.4 | Any union, works council or HR considerations? | |

## 9. Commercials and next steps

| # | Question | Answer |
|---|---|---|
| 9.1 | Budget status: identified, approved, or to be built from a business case? | |
| 9.2 | Decision process and timeline; who signs? | |
| 9.3 | Appetite for a time-boxed POC (2–6 weeks) with agreed success criteria? | |
| 9.4 | What would stop this project? | |
| 9.5 | Agreed next step, owner and date | |

---

## Qualification summary (fill after the call)

| Dimension | Score 1–5 | Notes |
|---|---|---|
| Business value clarity | | |
| Data readiness | | |
| Integration feasibility | | |
| Risk manageability | | |
| Sponsor and ownership | | |
| **Go / No-go / Explore further** | | |

Next artifacts: [use-case assessment](use-case-assessment.md) → [solution one-pager](solution-design-one-pager.md) → [POC plan](poc-plan.md).
