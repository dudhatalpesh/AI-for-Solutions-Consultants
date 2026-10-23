# 09 — Glossary

> **Status: starter.** Add terms as modules are completed (keep alphabetical).

| Term | Plain-English definition |
|---|---|
| **Agent** | An LLM-driven program that decides which tools to call, in what order, to reach a goal. |
| **AI gateway** | A control point between apps and models that handles access, routing, logging, policy and cost. |
| **Chunking** | Splitting documents into smaller pieces before embedding them for retrieval. |
| **Citation (grounding)** | Showing which source passage supports an answer. |
| **Context window** | The maximum number of tokens a model can consider at once (prompt + retrieved text + answer). |
| **DLP** | Data loss prevention: controls that detect and stop sensitive data leaving where it should stay. |
| **DPIA** | Data Protection Impact Assessment: a privacy risk assessment required by GDPR for high-risk processing. |
| **Embedding** | A list of numbers representing the meaning of text, so similar meanings are close together. |
| **Evaluation (eval)** | Systematic testing of AI output quality, safety, cost and latency against a fixed dataset. |
| **Excessive agency** | An AI system with more tools, permissions or autonomy than it needs (OWASP LLM06). |
| **Golden dataset** | A curated set of inputs with expected outputs, used for repeatable evaluation. |
| **Guardrail** | A check on input, retrieval, tool use or output that blocks or modifies unsafe behaviour. |
| **Hallucination** | A fluent, confident answer that is wrong or unsupported by sources. |
| **HITL** | Human in the loop: a person reviews or approves before the system acts. |
| **Indirect prompt injection** | Malicious instructions hidden in content the model reads (documents, emails, web pages). |
| **LLM** | Large language model: a model trained on large text corpora to predict and generate text. |
| **MCP** | Model Context Protocol: an open protocol for connecting models/agents to tools and data. n8n has MCP client and server nodes. |
| **n8n** | Workflow automation platform used here for orchestration, integrations and AI agents. |
| **OCR** | Optical character recognition: converting images of text into machine-readable text. |
| **Ollama** | Tool for running open models locally with a simple API. |
| **OWASP** | Open Worldwide Application Security Project; publishes the Top 10 for LLM Applications. |
| **PII** | Personally identifiable information. |
| **POC** | Proof of concept: a time-boxed build to prove value and feasibility against agreed criteria. |
| **Prompt injection** | Input crafted to override the system's instructions (OWASP LLM01). |
| **RAG** | Retrieval-augmented generation: retrieve relevant documents, then have the model answer from them. |
| **Red teaming** | Adversarial testing to find failures before attackers or users do. |
| **SASE** | Secure Access Service Edge: converged network and security delivered from the cloud. |
| **Shadow AI** | Use of AI tools without organisational approval or oversight. |
| **System prompt** | Instructions set by the application that frame the model's behaviour. |
| **Temperature** | A setting controlling randomness; lower is more deterministic. |
| **Token** | A unit of text (roughly ¾ of an English word) that models read and generate; used for limits and pricing. |
| **Tool calling** | A model returning a structured request to run a function/API, which the app executes. |
| **Vector database** | A database optimised for storing embeddings and finding nearest neighbours (for example Qdrant). |
