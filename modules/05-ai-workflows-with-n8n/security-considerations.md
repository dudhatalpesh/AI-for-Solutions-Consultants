# Module 05 — Security Considerations

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

| Risk | Control |
|---|---|
| Email content contains injection | Classifier outputs a fixed label set; no free-form actions |
| Over-privileged integration credentials | Scope credentials per workflow; read-only where possible |
| Approval link forgery | Use n8n resume URLs (unguessable), authenticate approvers in production |

See also the [AI security playbook](../../docs/06-ai-security-playbook.md).
