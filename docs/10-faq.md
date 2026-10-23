# 10 — FAQ

> **Status: starter.** Add questions from learners and customers.

## About the program

**Do I need to code?**
Not for the core n8n labs. Python labs are recommended for depth (evaluation, security testing, custom tools) and use copy-paste-ready scripts.

**Why n8n?**
It combines hundreds of built-in integrations, a visual builder, an AI Agent node and approval/error handling in one self-hostable tool. That mirrors what customers actually need: AI inside business processes, not AI in isolation. See [04 — Tool selection guide](04-tool-selection-guide.md).

**Can I use cloud models instead of Ollama?**
Yes, swap the chat model sub-node. Use synthetic data only and follow your organisation's AI policy.

**My laptop is slow. What can I do?**
Use `llama3.2` (3B), close other apps, or run Ollama natively for GPU access (Apple Silicon). Pin node data in n8n to avoid repeated model calls while building.

## Customer questions you will hear

**"Will our data be used to train the model?"**
Local models: no, data stays in your environment. Cloud providers: depends on the product and contract — check the provider's current data usage terms and enterprise options.

**"How do we stop hallucinations?"**
You reduce them: ground answers in retrieved sources, require citations, allow "I don't know", validate outputs, and measure on an evaluation set. You do not eliminate them, so keep humans in the loop for high-impact decisions.

**"Is prompt injection solved?"**
No. Design so a successful injection has limited impact: least-privilege tools, approvals, output validation and monitoring. See [06 — AI security playbook](06-ai-security-playbook.md).

**"What will it cost in production?"**
It depends on volume, model choice and architecture. The POC should measure tokens and cost per transaction so the business case uses real numbers. See [Lab 12](../labs/lab-12-ai-observability-and-cost-dashboard/README.md).
