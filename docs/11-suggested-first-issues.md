# 11 — Suggested First 15 GitHub Issues

A backlog to build this repo out incrementally. **These are not yet created on GitHub.** Create them when you are ready (see the command at the end).

Labels used: `content`, `lab`, `n8n-workflow`, `python`, `security`, `template`, `infra`, `good first issue`.

| # | Title | Labels | Depends on |
|---|---|---|---|
| 1 | Smoke-test docker-compose stack on Windows, macOS and Linux | infra | — |
| 2 | Import-test all 10 n8n workflows on current n8n stable and fix version drift | n8n-workflow | 1 |
| 3 | Complete Module 02 — LLMs and prompting (all 12 files) | content | — |
| 4 | Complete Lab 02 — prompt engineering playground (Streamlit + n8n) | lab, python | 3 |
| 5 | Complete Module 03 — Conversational AI | content | — |
| 6 | Complete Module 04 — RAG + Python RAG eval notebook | content, python | — |
| 7 | Complete Module 05 + Lab 06 — email triage with IMAP option and exception queue | content, lab | 2 |
| 8 | Complete Module 06 — Document intelligence (OCR options, PDF path) | content | — |
| 9 | Complete Modules 07–08 — agents, with LangGraph/CrewAI comparison | content, python | — |
| 10 | Complete Module 09 — FastAPI RAG service, AI gateway workflow, model routing | content, python, n8n-workflow | 2 |
| 11 | Complete Module 10 + Lab 12 — golden-dataset eval workflow and metrics summary | content, lab | 2 |
| 12 | Write full Consultant Playbook prose with a worked example | content, template | — |
| 13 | Write full AI Security Playbook prose + OWASP-to-control mapping table | content, security | — |
| 14 | Complete Demo and POC guide + remaining templates (one-pager, exec briefing, ROI/TCO, QBR) | content, template | 12 |
| 15 | Complete Modules 11–13 and capstone rubric; add CI link-check for anchors | content, security, infra | 13 |

## Issue details

### 1. Smoke-test docker-compose stack on Windows, macOS and Linux
- **Goal:** confirm `docker compose up -d` works from a clean clone on all three OSes.
- **Acceptance:** n8n `/healthz` OK; both Ollama models pulled; Qdrant and Mailpit reachable; lab schema exists; notes added to [02 — Environment setup](02-environment-setup.md).

### 2. Import-test all 10 n8n workflows
- **Goal:** each JSON imports cleanly into the pinned n8n version; node versions and parameters current.
- **Acceptance:** each workflow runs with its sample input and produces the expected output in [n8n-workflows/README.md](../n8n-workflows/README.md); tested version recorded.

### 3. Complete Module 02 — LLMs and prompting
- **Acceptance:** all 12 files full (no outline markers); prompt pattern library; knowledge check with answers.

### 4. Complete Lab 02 — prompt engineering playground
- **Acceptance:** Streamlit app compares prompts/temperatures side by side on local models; optional n8n webhook backend; full lab template sections.

### 5. Complete Module 03 — Conversational AI
- **Acceptance:** concepts (memory, grounding, escalation), architecture diagrams, conversation test plan, discovery questions.

### 6. Complete Module 04 — RAG
- **Acceptance:** chunking strategy guidance, access-controlled retrieval pattern, Jupyter notebook comparing chunk sizes on the Lab 04 eval set.

### 7. Complete Module 05 + Lab 06 — email triage
- **Acceptance:** Lab 06 full lab template; optional Email Trigger (IMAP) variant with Mailpit; retries, exception queue, error workflow.

### 8. Complete Module 06 — Document intelligence
- **Acceptance:** OCR options compared (Tesseract, cloud OCR — labelled), PDF text vs scanned path, redaction guidance.

### 9. Complete Modules 07–08 — agents
- **Acceptance:** failure-mode catalogue, agent design checklist, Python LangGraph or CrewAI equivalent of Lab 08 (APIs verified against current docs).

### 10. Complete Module 09 — architecture and deployment
- **Acceptance:** FastAPI RAG service with Dockerfile added to compose (profile), n8n AI gateway workflow with local/cloud routing, backup/restore drill.

### 11. Complete Module 10 + Lab 12 — observability
- **Acceptance:** golden-dataset evaluation workflow; metrics SQL; alert thresholds; Lab 12 full lab template.

### 12. Consultant Playbook prose
- **Acceptance:** each section of [05](05-consultant-playbook.md) in full prose with a worked example.

### 13. AI Security Playbook prose
- **Acceptance:** each section of [06](06-ai-security-playbook.md) in full; control mapping table; incident runbook.

### 14. Demo/POC guide + remaining templates
- **Acceptance:** [07](07-demo-and-poc-guide.md) complete; all outline templates complete.

### 15. Modules 11–13, capstone rubric, CI anchors
- **Acceptance:** modules complete; capstone scoring rubric; `scripts/validate_repo.py` also checks heading anchors.

## Creating these on GitHub

After you approve, they can be created with the GitHub CLI, for example:

```bash
gh issue create --repo dudhatalpesh/AI-for-Solutions-Consultants --title "Smoke-test docker-compose stack on Windows, macOS and Linux" --label infra --body "See docs/11-suggested-first-issues.md#1-smoke-test-docker-compose-stack-on-windows-macos-and-linux"
```

Labels must exist first (`gh label create infra`, etc.).
