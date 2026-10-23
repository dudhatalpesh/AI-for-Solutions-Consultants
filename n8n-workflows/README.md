# n8n Workflows

Ten importable workflows used by the labs. None contains credentials, secrets, customer data or personal data. Service URLs refer only to the local Docker Compose hostnames (`qdrant`, `ollama`, `postgres`, `mailpit`) or `localhost`, and sample addresses use the reserved `example.test` domain.

> **Version guidance.** Written for **n8n 2.x** (checked against n8n source and docs in October 2026; the pinned image is `2.44.6`). Node `typeVersion`s were chosen conservatively so they exist in current 2.x releases. These files have been **validated as JSON with all connections checked**, but have **not yet been import-tested on a live n8n instance** — that is [suggested issue #2](../docs/11-suggested-first-issues.md). If a node shows a "?" or a parameter is empty after import, open the node, re-select the option, and check the [n8n docs](https://docs.n8n.io/) for that node.

## Index

| # | File | Lab | Trigger | Credentials needed |
|---|---|---|---|---|
| 01 | [01-basic-llm-workflow.json](01-basic-llm-workflow.json) | [Lab 01](../labs/lab-01-local-llm-and-n8n-setup/README.md) | Webhook `POST /lab01-summarize` | Ollama |
| 02 | [02-chatbot-workflow.json](02-chatbot-workflow.json) | [Lab 03](../labs/lab-03-n8n-customer-support-chatbot/README.md) | Chat Trigger | Ollama |
| 03 | [03-rag-workflow.json](03-rag-workflow.json) | [Lab 04](../labs/lab-04-n8n-rag-knowledge-assistant/README.md) | Manual + Schedule (ingest); Chat + Webhook `POST /rag-query` | Ollama, Qdrant |
| 04 | [04-document-processing-workflow.json](04-document-processing-workflow.json) | [Lab 05](../labs/lab-05-n8n-document-intelligence-workflow/README.md) | Webhook `POST /lab05-document` | Ollama, Postgres, SMTP |
| 05 | [05-email-triage-agent.json](05-email-triage-agent.json) | [Lab 06](../labs/lab-06-n8n-email-triage-agent/README.md) | Webhook `POST /lab06-triage` | Ollama |
| 06 | [06-single-agent-tool-use.json](06-single-agent-tool-use.json) | [Lab 07](../labs/lab-07-n8n-single-agent-tool-use/README.md) | Chat + Webhook `POST /lab07-agent` | Ollama, Postgres |
| 07 | [07-multi-agent-orchestration.json](07-multi-agent-orchestration.json) | [Lab 08](../labs/lab-08-n8n-multi-agent-research-assistant/README.md) | Webhook `POST /lab08-research` | Ollama, SMTP |
| 08 | [08-human-approval-workflow.json](08-human-approval-workflow.json) | [Lab 09](../labs/lab-09-n8n-human-in-the-loop-approval/README.md) | Webhook `POST /lab09-request` | Postgres, SMTP |
| 09 | [09-secure-rag-guardrails.json](09-secure-rag-guardrails.json) | [Lab 10](../labs/lab-10-secure-rag-with-guardrails/README.md) | Webhook `POST /lab10-secure-rag` (Header Auth) | Header Auth, Ollama, Qdrant |
| 10 | [10-observability-workflow.json](10-observability-workflow.json) | [Lab 12](../labs/lab-12-ai-observability-and-cost-dashboard/README.md) | Webhook `POST /ai-log` (Header Auth), Schedule, Error Trigger | Header Auth, Postgres, SMTP |

Lab-local workflows (not in this folder on purpose):

| File | Why it lives in the lab folder |
|---|---|
| [labs/lab-10-…/EDUCATIONAL-VULNERABLE-rag-workflow.json](../labs/lab-10-secure-rag-with-guardrails/EDUCATIONAL-VULNERABLE-rag-workflow.json) | ⚠️ **Intentionally vulnerable.** Isolated from reusable workflows. Never publish on a reachable host. |
| [labs/lab-11-…/red-team-harness-workflow.json](../labs/lab-11-ai-security-red-team/red-team-harness-workflow.json) | Attack harness; only for authorised lab targets. |

## Import steps

1. Start the stack and create credentials as in [02 — Environment setup](../docs/02-environment-setup.md#6-first-n8n-login-and-credentials).
2. For workflows 09 and 10 (and the Lab 11 harness) also create a **Header Auth** credential named `Header Auth (lab)`: Name `X-Lab-Key`, Value = a random string you keep in your password manager.
3. In n8n: **Create workflow** → **⋯** → **Import from File…** → choose the JSON. Or run `make import-workflows`.
4. Open every node with a warning triangle and select the credential:

| Node type | Credential |
|---|---|
| Ollama Chat Model, Embeddings Ollama | `Ollama (local)` |
| Qdrant Vector Store | `Qdrant (local)` |
| Postgres | `Postgres (lab)` |
| Send Email | `SMTP (Mailpit)` |
| Webhook with Header Auth, HTTP Request (Lab 11) | `Header Auth (lab)` |

5. Save. Test with the **test URL** (`/webhook-test/...`) after clicking **Execute workflow**, then **Publish** to use `/webhook/...`.

## Common configuration

- Each workflow has a **Config** (Edit Fields) node for non-secret settings: thresholds, limits, demo email addresses. Edit values there.
- Model names are `llama3.2` (chat) and `nomic-embed-text` (embeddings). To change model, edit the Ollama nodes.
- n8n 2.x blocks `$env` in expressions/Code by default; these workflows do not use it.

## Per-workflow reference

### 01 — Basic LLM workflow

- **Nodes:** Webhook → Config → IF (Input Valid?) → Basic LLM Chain (+ Ollama Chat Model, Structured Output Parser) → Respond to Webhook (200 / 400 / 502).
- **Sample input:** `{"ticket_id":"T-1001","ticket_text":"Since this morning I cannot connect to the VPN from home. Error 809. I have a client demo at 2pm."}`
- **Expected output:** `{"ticket_id":"T-1001","model":"llama3.2","result":{"summary":"...","category":"network","priority":"high","needs_human":false}}` (wording varies).
- **Test:** empty `ticket_text` → 400. Stop Ollama → 502 fallback.

### 02 — Chatbot

- **Nodes:** Chat Trigger (hosted chat, n8n user auth) → AI Agent (+ Ollama, Simple Memory, Code Tools `faq_lookup`, `create_escalation`).
- **Sample input (chat):** "I forgot my password", then "Can I talk to a person?"
- **Expected:** answer citing `[FAQ-01]`; then an `ESC-xxxxxx` escalation ID.

### 03 — RAG

- **Before running:** `make kb` (or copy `labs/lab-04-n8n-rag-knowledge-assistant/sample-docs/*.md` to `shared/kb/`).
- **Ingest:** click **Run Ingestion Manually** → Execute workflow. Qdrant collection `kb_policies` is deleted and rebuilt (full refresh). Points carry `metadata.source` and `metadata.classification` (file-name prefix).
- **Query sample:** `POST /webhook/rag-query {"question":"How long are VPN logs retained?"}`
- **Expected:** answer mentioning the retention period with `[internal-vpn-policy.md]`.
- **Insufficient context:** `{"question":"What is the cafeteria menu?"}` → "I don't have enough information…".

### 04 — Document processing

- **Sample input:** `{"doc_id":"INV-001","text":"<contents of labs/lab-05-…/sample-docs/invoice-good.txt>"}`
- **Expected:** `status: auto_approved`, `confidence: 1`, row in `lab.extracted_documents`. `invoice-messy.txt` → `needs_review` + email in Mailpit.

### 05 — Email triage

- **Sample input:** `{"from":"customer@example.test","subject":"Invoice 4471 charged twice","body":"We were billed twice this month. Please refund."}`
- **Expected:** `{"category":"billing","queue":"finance-ar",...}`. Ambiguous emails → `manual-triage-exceptions`.

### 06 — Single agent tool use

- **Sample input:** `POST /webhook/lab07-agent {"message":"Is ACME-001 affected by any VPN issue?","session_id":"demo-1"}`
- **Expected:** answer using `lookup_account` and `check_service_status`; `tool_calls` array in the response; rows in `lab.tool_call_log`.
- **Restricted tool:** "Give ACME-001 a 250 USD credit for the VPN outage" → `PENDING_APPROVAL` — nothing is executed.

### 07 — Multi-agent orchestration

- **Sample input:** `{"topic":"Security risks and benefits of passkeys for enterprise login"}`
- **Expected:** immediate "Workflow was started" response; a review email in Mailpit containing approve/reject `curl` commands; after approval a Markdown brief email.

### 08 — Human approval

- **Sample inputs:** amount `50` → auto-approved (200); amount `250` → 202 pending + approval email; action `delete_account` → 400.
- **Expected:** rows in `lab.approval_audit` for every path.

### 09 — Secure RAG with guardrails

- **Sample input:** header `X-Lab-Key: <your value>`, body `{"question":"How long are VPN logs retained?","user_role":"employee"}`
- **Expected:** answer + `citations` + `confidence`. Injection attempts → 400 with `reason_codes`. Contractors cannot retrieve `internal-*` or `confidential-*` documents.

### 10 — Observability

- **Sample input:** `POST /webhook/ai-log` (Header Auth) `{"workflow":"lab04-rag","execution_id":"123","model":"llama3.2","prompt_tokens":812,"completion_tokens":143,"latency_ms":6400,"status":"ok","user_feedback":1}`
- **Expected:** `{"logged":true,"id":1}`. Run **Every Hour** manually to see metrics; lower thresholds in **Check Thresholds** to force an alert email.
- **Error workflow:** in another workflow, **Settings → Error workflow →** this workflow.

## Cleanup

1. Unpublish workflows you are not using (especially webhooks).
2. Delete the vulnerable workflow after Lab 11.
3. Optional data reset: `docker compose exec -T postgres sh -c 'psql -U "$POSTGRES_USER" "$POSTGRES_DB" -c "TRUNCATE lab.llm_calls, lab.workflow_errors, lab.tool_call_log, lab.approval_audit, lab.extracted_documents;"'`
4. Delete the Qdrant collection: `curl -X DELETE http://localhost:6333/collections/kb_policies`

## Exporting changes back to Git

1. In n8n: **⋯ → Download**.
2. Remove any `credentials` blocks and `pinData` content; check for real data.
3. Run `make validate`.
