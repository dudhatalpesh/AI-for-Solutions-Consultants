# Module 01 — Knowledge Check

Answer without notes, then check the answers below. Aim for 8/10.

## Questions

1. Roughly how many English words are 1,000 tokens?
2. Name three things that tokens drive.
3. What does an embedding represent, and what does it enable?
4. What happens when your prompt plus retrieved documents exceed the context window?
5. Which temperature range would you use for extracting invoice fields, and why?
6. Give three techniques that reduce hallucination.
7. A customer says they need an AI that "reads incoming contracts and fills in our CLM system". Which use-case category is this?
8. In n8n, which node forces a model's output into a JSON schema?
9. Why does the Lab 01 workflow use the Ollama URL `http://ollama:11434` rather than `http://localhost:11434`?
10. Name two places in a basic n8n LLM workflow where sensitive data could be stored or leaked.

## Answers

1. About 750 words (≈ ¾ word per token; varies by language and model).
2. Cost, context-window limits, latency.
3. The meaning of text as a vector of numbers; it enables semantic search and RAG.
4. Input is truncated (often silently) or the request fails; the model may miss key information.
5. 0–0.2: you want consistent, conservative output that matches a schema.
6. Any three: grounding with RAG and citations; permission to say "I don't know"; schema validation; low temperature; human review; evaluation on a test set.
7. Document AI (extraction to structured fields), likely with workflow automation for the CLM (contract lifecycle management) update.
8. **Structured Output Parser** (attached to a Basic LLM Chain or AI Agent).
9. Inside the Docker network, `localhost` is the n8n container itself; `ollama` is the Ollama container's hostname.
10. Any two: n8n execution history; the model provider (if cloud); logs; downstream systems that receive the output.

Score below 8? Re-read [concepts.md](concepts.md) sections 2–6.
