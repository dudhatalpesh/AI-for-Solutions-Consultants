# AI for Solutions Consultants

**Go from "AI-aware technologist" to "AI solutions advisor" in 12 weeks (or 4, accelerated).**

A hands-on enablement program for customer-facing technical people. You will discover AI requirements, design architectures, build working demos with **n8n** and local models, run proofs of concept (POCs), assess AI security risk, troubleshoot implementations, and explain business value to engineers and executives.

> ⚠️ **Things change fast.** Tools, APIs, models, n8n node behaviour and pricing change frequently. Everything here was checked against public docs in October 2026 (n8n 2.x). Always confirm against current vendor docs before you quote anything to a customer.

---

## Who this is for

Solutions Consultants (SCs), Sales Engineers (SEs), Solution Architects and cybersecurity consultants who **already know** enterprise IT, cloud, networking, cybersecurity, SASE (Secure Access Service Edge), identity, zero trust, discovery, demos, POCs and executive communication.

You **do not yet need to know** large language model (LLM) internals, prompting, retrieval-augmented generation (RAG), agents, AI orchestration, AI security, or AI observability and evaluation. That is what this program teaches.

## What you will be able to do

1. Explain AI in business and technical terms.
2. Qualify use cases: conversational AI, document AI, workflow automation and agentic AI.
3. Build demos with n8n and open-source or freemium tools.
4. Design RAG, chatbot, copilot, document-processing, single-agent and multi-agent architectures.
5. Deploy and troubleshoot n8n workflows.
6. Evaluate quality, cost, latency, reliability and safety.
7. Identify AI security risks and recommend controls.
8. Produce consultant artifacts: discovery questionnaires, architecture one-pagers, POC plans, risk registers, demo scripts and executive briefings.
9. Advise on responsible AI, governance, privacy, compliance and secure deployment.

---

## Quick start (about 20 minutes, plus model download)

Prerequisites: Docker Desktop (or Docker Engine + Compose), Git, 16 GB RAM recommended, ~15 GB free disk. Full details: [docs/02-environment-setup.md](docs/02-environment-setup.md).

```bash
git clone https://github.com/dudhatalpesh/AI-for-Solutions-Consultants.git
cd AI-for-Solutions-Consultants
cp .env.example .env          # PowerShell: Copy-Item .env.example .env
# Edit .env: replace every CHANGE_ME value
docker compose up -d
docker compose logs -f ollama-init   # wait until both models are pulled
```

Then open:

| Service | URL | Purpose |
|---|---|---|
| n8n | http://localhost:5678 | Workflow and agent orchestration (create the owner account on first visit) |
| Ollama API | http://localhost:11434 | Local models |
| Qdrant dashboard | http://localhost:6333/dashboard | Vector database |
| Mailpit | http://localhost:8025 | Local fake email inbox for approvals and alerts |

Next: [Lab 01 — Local LLM and n8n setup](labs/lab-01-local-llm-and-n8n-setup/README.md).

---

## The n8n-centred tool stack

n8n is the primary orchestration platform in every module. Python covers custom tools, APIs, evaluation and advanced security labs.

| Layer | Default tool | Labels | Alternatives |
|---|---|---|---|
| Orchestration | [n8n](https://docs.n8n.io/) (self-hosted) | Open source (fair-code licence), Local, Beginner-friendly | n8n Cloud (Freemium trial, Cloud) |
| Local models | [Ollama](https://ollama.com/) | Open source, Local, Beginner-friendly | LM Studio (Freemium, Local) |
| Open models and embeddings | [Hugging Face](https://huggingface.co/) | Freemium, Cloud/Local | — |
| Vector database | [Qdrant](https://qdrant.tech/) | Open source, Local | Chroma, FAISS (Open source, Local) |
| Database / logs | PostgreSQL | Open source, Local | Google Sheets (Freemium, Cloud, Optional) |
| Custom code | Python 3.11+, FastAPI | Open source, Local | — |
| UIs | Streamlit, Gradio | Open source, Local, Beginner-friendly | — |
| Experiments | JupyterLab | Open source, Local | — |
| Advanced agents | LangGraph, CrewAI | Open source, Advanced, Optional | LangChain, LlamaIndex (concepts) |
| Email testing | Mailpit | Open source, Local | — |

Why these choices, and when to swap: [docs/04-tool-selection-guide.md](docs/04-tool-selection-guide.md).

---

## Learning paths

Full detail: [docs/00-learning-path.md](docs/00-learning-path.md).

| Phase | Topic | Module | Hands-on lab | 12-week | 4-week |
|---|---|---|---|---|---|
| 1 | AI foundations and LLM literacy | [01](modules/01-ai-foundations/README.md), [02](modules/02-llms-and-prompting/README.md) | [Lab 01](labs/lab-01-local-llm-and-n8n-setup/README.md), [Lab 02](labs/lab-02-prompt-engineering-playground/README.md) | Wk 1–2 | Wk 1 |
| 2 | Conversational AI | [03](modules/03-conversational-ai/README.md) | [Lab 03](labs/lab-03-n8n-customer-support-chatbot/README.md) | Wk 3 | Wk 1 |
| 3 | RAG and enterprise knowledge | [04](modules/04-rag-and-enterprise-knowledge/README.md) | [Lab 04](labs/lab-04-n8n-rag-knowledge-assistant/README.md) | Wk 4 | Wk 1 |
| 4 | AI workflows with n8n | [05](modules/05-ai-workflows-with-n8n/README.md) | [Lab 06](labs/lab-06-n8n-email-triage-agent/README.md), [Lab 09](labs/lab-09-n8n-human-in-the-loop-approval/README.md) | Wk 5 | Wk 2 |
| 5 | Document intelligence | [06](modules/06-document-intelligence/README.md) | [Lab 05](labs/lab-05-n8n-document-intelligence-workflow/README.md) | Wk 6 | Wk 2 |
| 6 | Single-agent systems | [07](modules/07-single-agent-systems/README.md) | [Lab 07](labs/lab-07-n8n-single-agent-tool-use/README.md) | Wk 7 | Wk 2 |
| 7 | Multi-agent systems | [08](modules/08-multi-agent-systems/README.md) | [Lab 08](labs/lab-08-n8n-multi-agent-research-assistant/README.md) | Wk 8 | Wk 2 |
| 8 | Architecture and deployment | [09](modules/09-ai-architecture-and-deployment/README.md) | Module n8n lab (AI gateway) | Wk 9 | Wk 3 |
| 9 | Observability and evaluation | [10](modules/10-ai-observability-and-evaluation/README.md) | [Lab 12](labs/lab-12-ai-observability-and-cost-dashboard/README.md) | Wk 9 | Wk 3 |
| 10 | AI security fundamentals | [11](modules/11-ai-security-fundamentals/README.md) | [Lab 10](labs/lab-10-secure-rag-with-guardrails/README.md) | Wk 10 | Wk 3 |
| 11 | AI red teaming | [12](modules/12-ai-security-red-teaming/README.md) | [Lab 11](labs/lab-11-ai-security-red-team/README.md) | Wk 11 | Wk 3 |
| 12 | Governance, responsible AI, compliance | [13](modules/13-governance-responsible-ai-and-compliance/README.md) | Module n8n lab (AI inventory) | Wk 11 | Wk 3 |
| 13 | Capstone | [14](modules/14-capstone-secure-enterprise-ai-advisor/README.md) | [Lab 13](labs/lab-13-capstone-secure-ai-advisor/README.md) | Wk 12 | Wk 4 |

---

## Repository map

```
AI-for-Solutions-Consultants/
├── README.md                 ← you are here
├── CONTRIBUTING.md  CODE_OF_CONDUCT.md  LICENSE
├── .gitignore  .env.example  requirements.txt  docker-compose.yml  Makefile
├── db/init/                  Postgres schema for lab logging tables
├── shared/                   Bind-mounted into n8n as /data/shared (git-ignored contents)
├── scripts/                  Repo validation (JSON, links, secret patterns)
├── docs/                     Program guides and playbooks (00–11)
├── modules/                  14 modules × 12 standard files
├── labs/                     13 hands-on labs (README + code + sample data)
├── n8n-workflows/            10 importable n8n workflow JSON files + README
├── architectures/            Reference architectures with Mermaid diagrams
├── templates/                Consultant artifacts (discovery, POC, risk, demo, ...)
├── assets/                   diagrams/ and images/
└── .github/                  Issue templates and CI validation workflow
```

---

## Indexes

### Program docs

| # | Doc | Status |
|---|---|---|
| 00 | [Learning path](docs/00-learning-path.md) | Complete |
| 01 | [How to use this repo](docs/01-how-to-use-this-repo.md) | Complete |
| 02 | [Environment setup](docs/02-environment-setup.md) | Complete |
| 03 | [n8n setup and operations guide](docs/03-n8n-setup-and-operations-guide.md) | Complete |
| 04 | [Tool selection guide](docs/04-tool-selection-guide.md) | Complete |
| 05 | [Consultant playbook](docs/05-consultant-playbook.md) | Outline |
| 06 | [AI security playbook](docs/06-ai-security-playbook.md) | Outline |
| 07 | [Demo and POC guide](docs/07-demo-and-poc-guide.md) | Outline |
| 08 | [Troubleshooting guide](docs/08-troubleshooting-guide.md) | Outline |
| 09 | [Glossary](docs/09-glossary.md) | Starter |
| 10 | [FAQ](docs/10-faq.md) | Starter |
| 11 | [Suggested first 15 GitHub issues](docs/11-suggested-first-issues.md) | Complete |

### Modules

| # | Module | Status |
|---|---|---|
| 01 | [AI foundations](modules/01-ai-foundations/README.md) | Complete |
| 02 | [LLMs and prompting](modules/02-llms-and-prompting/README.md) | Outline |
| 03 | [Conversational AI](modules/03-conversational-ai/README.md) | Outline |
| 04 | [RAG and enterprise knowledge](modules/04-rag-and-enterprise-knowledge/README.md) | Outline |
| 05 | [AI workflows with n8n](modules/05-ai-workflows-with-n8n/README.md) | Outline |
| 06 | [Document intelligence](modules/06-document-intelligence/README.md) | Outline |
| 07 | [Single-agent systems](modules/07-single-agent-systems/README.md) | Outline |
| 08 | [Multi-agent systems](modules/08-multi-agent-systems/README.md) | Outline |
| 09 | [AI architecture and deployment](modules/09-ai-architecture-and-deployment/README.md) | Outline |
| 10 | [AI observability and evaluation](modules/10-ai-observability-and-evaluation/README.md) | Outline |
| 11 | [AI security fundamentals](modules/11-ai-security-fundamentals/README.md) | Outline |
| 12 | [AI security red teaming](modules/12-ai-security-red-teaming/README.md) | Outline |
| 13 | [Governance, responsible AI and compliance](modules/13-governance-responsible-ai-and-compliance/README.md) | Outline |
| 14 | [Capstone: Secure enterprise AI advisor](modules/14-capstone-secure-enterprise-ai-advisor/README.md) | Spec complete |

### Labs

| # | Lab | Workflow | Status |
|---|---|---|---|
| 01 | [Local LLM and n8n setup](labs/lab-01-local-llm-and-n8n-setup/README.md) | [01](n8n-workflows/01-basic-llm-workflow.json) | Complete |
| 02 | [Prompt engineering playground](labs/lab-02-prompt-engineering-playground/README.md) | — | Outline + starter app |
| 03 | [Customer support chatbot](labs/lab-03-n8n-customer-support-chatbot/README.md) | [02](n8n-workflows/02-chatbot-workflow.json) | Complete |
| 04 | [RAG knowledge assistant](labs/lab-04-n8n-rag-knowledge-assistant/README.md) | [03](n8n-workflows/03-rag-workflow.json) | Complete |
| 05 | [Document intelligence workflow](labs/lab-05-n8n-document-intelligence-workflow/README.md) | [04](n8n-workflows/04-document-processing-workflow.json) | Complete |
| 06 | [Email triage agent](labs/lab-06-n8n-email-triage-agent/README.md) | [05](n8n-workflows/05-email-triage-agent.json) | Outline (workflow ready) |
| 07 | [Single agent tool use](labs/lab-07-n8n-single-agent-tool-use/README.md) | [06](n8n-workflows/06-single-agent-tool-use.json) | Complete |
| 08 | [Multi-agent research assistant](labs/lab-08-n8n-multi-agent-research-assistant/README.md) | [07](n8n-workflows/07-multi-agent-orchestration.json) | Complete |
| 09 | [Human-in-the-loop approval](labs/lab-09-n8n-human-in-the-loop-approval/README.md) | [08](n8n-workflows/08-human-approval-workflow.json) | Complete |
| 10 | [Secure RAG with guardrails](labs/lab-10-secure-rag-with-guardrails/README.md) | [09](n8n-workflows/09-secure-rag-guardrails.json) | Complete |
| 11 | [AI security red team](labs/lab-11-ai-security-red-team/README.md) | Lab-local harness | Complete |
| 12 | [Observability and cost dashboard](labs/lab-12-ai-observability-and-cost-dashboard/README.md) | [10](n8n-workflows/10-observability-workflow.json) | Outline (workflow ready) |
| 13 | [Capstone: Secure AI advisor](labs/lab-13-capstone-secure-ai-advisor/README.md) | Built by you | Spec complete |

### n8n workflows

See [n8n-workflows/README.md](n8n-workflows/README.md) for import steps, credentials, sample inputs and expected outputs.

### Reference architectures

[Conversational AI](architectures/conversational-ai.md) · [Enterprise RAG](architectures/enterprise-rag.md) · [Document processing](architectures/document-processing.md) · [Single agent](architectures/single-agent.md) · [Multi-agent](architectures/multi-agent.md) · [AI gateway](architectures/ai-gateway.md) · [Secure AI reference architecture](architectures/secure-ai-reference-architecture.md) · [Hybrid cloud/local AI](architectures/hybrid-cloud-local-ai.md) · [n8n reference architectures](architectures/n8n-reference-architectures.md)

### Consultant templates

| Template | Status |
|---|---|
| [Discovery questionnaire](templates/discovery-questionnaire.md) | Complete |
| [POC plan](templates/poc-plan.md) | Complete |
| [Risk register](templates/risk-register.md) | Complete |
| [Demo script](templates/demo-script.md) | Complete |
| [n8n workflow design review checklist](templates/n8n-workflow-design-review-checklist.md) | Complete |
| [Use-case assessment and prioritisation matrix](templates/use-case-assessment.md) | Outline |
| [AI readiness assessment](templates/ai-readiness-assessment.md) | Outline |
| [Solution design one-pager](templates/solution-design-one-pager.md) | Outline |
| [Security review checklist](templates/security-review-checklist.md) | Outline |
| [Responsible AI checklist](templates/responsible-ai-checklist.md) | Outline |
| [Executive briefing](templates/executive-briefing.md) | Outline |
| [ROI / TCO outline](templates/roi-tco-outline.md) | Outline |
| [Objection-handling guide](templates/objection-handling-guide.md) | Outline |
| [Customer QBR AI update](templates/customer-qbr-ai-update.md) | Outline |

---

## Tracking your progress

1. Each module has a `progress-checklist.md`. Tick items as you go.
2. Open a **Learning progress** issue (template in `.github/ISSUE_TEMPLATE/`) per module to keep notes and evidence (screenshots, exported workflows, artifacts).
3. Keep your own fork private if it contains notes about real customers. Better: never write real customer details down here at all.

## Contributing and licence

Contributions welcome — read [CONTRIBUTING.md](CONTRIBUTING.md) and the [Code of Conduct](CODE_OF_CONDUCT.md). Licensed under the [MIT License](LICENSE).

## Disclaimer

This is educational material. It is not legal, compliance or security certification advice. Red-team and intentionally vulnerable labs must run only on your own isolated local stack. Product names belong to their owners. Tools, APIs, models, n8n node behaviour and pricing change frequently — verify before you rely on anything here.
