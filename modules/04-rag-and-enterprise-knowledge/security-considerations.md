# Module 04 — Security Considerations

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

| Risk | Control |
|---|---|
| Retrieval bypasses document permissions | Store ACL metadata; filter at query time by user entitlement |
| Indirect prompt injection in documents | Sanitise content; treat retrieved text as data; output validation |
| Vector and embedding weaknesses (OWASP LLM08) | Control who can write to the index; audit ingestion sources |

See also the [AI security playbook](../../docs/06-ai-security-playbook.md).
