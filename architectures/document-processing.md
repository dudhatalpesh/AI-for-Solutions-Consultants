# Reference Architecture — Document Processing

> **Status: outline.** Diagram and key design points are in place; full narrative is tracked in [docs/11-suggested-first-issues.md](../docs/11-suggested-first-issues.md).

**Use when:** turning invoices, contracts, forms or reports into structured data.
**Built in:** [Lab 05](../labs/lab-05-n8n-document-intelligence-workflow/README.md) · [workflow 04](../n8n-workflows/04-document-processing-workflow.json)

```mermaid
flowchart LR
  IN[Inbound: email, upload,<br/>SFTP, scanner] --> CL[Classify document type]
  CL --> TXT[Text: PDF layer or OCR]
  TXT --> RED[Redact / minimise]
  RED --> EXT[Extract to JSON schema]
  EXT --> VAL[Validate rules +<br/>confidence]
  VAL -->|high| SYS[(ERP / DB)]
  VAL -->|low| HQ[Human review queue]
  HQ --> SYS
  VAL --> AUD[(Audit log)]
```

## Controls

File type and size limits; malware scanning on upload; redaction before the model and before storage; deterministic validation; value thresholds for human approval; parameterised writes; audit trail.
