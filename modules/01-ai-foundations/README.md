# Module 01 — AI Foundations

**Phase 1 · Week 1 (standard) · ~5–6 hours · Beginner**

## Why this matters for SCs

Every AI conversation with a customer eventually hits the same questions: *How does it actually work? Why did it make that up? What will it cost? Where does our data go?* If you cannot answer these in plain language, you lose the technical evaluator and the executive at the same time.

This module gives you working LLM literacy — tokens, embeddings, context windows, temperature, cost, latency and hallucination — and you will see each one with your own eyes on a local model running in n8n.

## What you will do

1. Learn the core concepts in [concepts.md](concepts.md).
2. Stand up n8n + Ollama locally and build your first LLM workflow with structured output and error handling ([n8n-lab.md](n8n-lab.md) → [Lab 01](../../labs/lab-01-local-llm-and-n8n-setup/README.md)).
3. Measure tokens, latency and embedding similarity in Python ([python-lab.md](python-lab.md)).
4. Practise explaining AI to a CIO and a CISO ([customer-conversation-prompts.md](customer-conversation-prompts.md)).

## Business use cases introduced

| Category | Example | Why it fits LLMs |
|---|---|---|
| Conversational AI | IT helpdesk assistant | Natural-language Q&A over known content |
| Document AI | Invoice and contract extraction | Turns unstructured text into structured fields |
| Workflow automation | Ticket triage and routing | Classification and summarisation inside a process |
| Agentic AI | Research assistant that uses tools | Multi-step tasks with decisions between steps |

## Files in this module

| File | Purpose |
|---|---|
| [learning-objectives.md](learning-objectives.md) | What you will be able to do |
| [concepts.md](concepts.md) | Core concepts |
| [n8n-lab.md](n8n-lab.md) | n8n hands-on |
| [python-lab.md](python-lab.md) | Python hands-on |
| [architecture.md](architecture.md) | How an LLM app fits together |
| [security-considerations.md](security-considerations.md) | First security and governance points |
| [troubleshooting.md](troubleshooting.md) | Failure modes and fixes |
| [customer-conversation-prompts.md](customer-conversation-prompts.md) | Discovery, exec explanation, objections |
| [knowledge-check.md](knowledge-check.md) | Self-test |
| [resources.md](resources.md) | Further reading |
| [progress-checklist.md](progress-checklist.md) | Track completion |

## Prerequisites

- [Environment setup](../../docs/02-environment-setup.md) done.
- Comfort with Docker and a terminal.

## Next module

[Module 02 — LLMs and prompting](../02-llms-and-prompting/README.md).
