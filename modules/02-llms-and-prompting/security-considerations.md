# Module 02 — Security Considerations

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

| Risk | Control |
|---|---|
| System prompt leakage (OWASP LLM07) | Never put secrets or sensitive logic in prompts; assume prompts can be extracted |
| Prompt injection via user input | Delimit user input; validate output; least-privilege downstream actions |
| Prompt templates edited without review | Version prompts in Git; review like code |

See also the [AI security playbook](../../docs/06-ai-security-playbook.md).
