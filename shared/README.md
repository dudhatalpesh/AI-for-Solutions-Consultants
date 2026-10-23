# shared/

This folder is bind-mounted into the n8n container at `/data/shared`.
n8n is configured (`N8N_RESTRICT_FILE_ACCESS_TO=/data/shared`) so file nodes can only read and write here.

Everything in this folder except this README is git-ignored. Labs copy sample data here, for example:

```bash
make kb    # copies labs/lab-04-n8n-rag-knowledge-assistant/sample-docs/ to shared/kb/
```

Do not put real customer data or personal data here.
