# Module 02 — Concepts

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

## Key concepts to cover

- System vs user prompts
- Zero-shot and few-shot prompting
- Asking for reasoning vs asking for answers (and cost/latency impact)
- Delimiters and separating instructions from data
- Structured output: JSON schemas and output parsers
- Prompt templates and variables in n8n expressions
- Model selection: size, context window, tool support
- When to use RAG, tools or fine-tuning instead of more prompting

## Failure modes

- Prompt works on one example, fails on others (no test set)
- Instructions overridden by input text (injection)
- Over-long prompts raising cost and latency
- Format drift breaking downstream parsing

## To be written

- [ ] Plain-English explanation of each concept with an SC-relevant example
- [ ] One comparison table and one Mermaid diagram per major concept
- [ ] Acronyms expanded on first use
