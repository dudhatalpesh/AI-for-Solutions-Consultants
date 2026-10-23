# Contributing

Thanks for improving this program. It is built incrementally; see [docs/11-suggested-first-issues.md](docs/11-suggested-first-issues.md) for the backlog.

## Ground rules

1. **No fabrication.** Do not invent APIs, n8n node names or parameters, package versions, prices or product capabilities. Link the doc you verified against. If unsure, write "check current docs".
2. **No secrets or real data.** Credentials go in `.env` (from `.env.example`) or n8n credentials. Use synthetic data only.
3. **Label every tool** you add: Open source / Freemium / Local / Cloud / Optional / Beginner-friendly / Advanced.
4. **Isolate vulnerable content.** Anything intentionally insecure lives in a lab folder, is named `EDUCATIONAL-VULNERABLE`, and carries the standard warning block.
5. **Plain, direct English.** Short paragraphs, numbered steps, tables, copy-paste-ready commands. Expand every acronym on first use. Add a Mermaid diagram for each architecture or workflow.

## Content standards

| Item | Must include |
|---|---|
| Module | The 12 standard files (see [docs/01-how-to-use-this-repo.md](docs/01-how-to-use-this-repo.md)) |
| Lab | Objective, time, difficulty, prerequisites, tools, diagrams, node-by-node build, sample I/O, validation, security, cost, errors, stretch goals, cleanup, customer demo |
| n8n workflow | Clear name, no hardcoded secrets or customer data, documented in [n8n-workflows/README.md](n8n-workflows/README.md) |

## Workflow for changes

1. Open an issue with the matching template.
2. Branch: `content/<short-name>` or `lab/<lab-number>-<short-name>`.
3. Run `make validate` (JSON parses, internal links resolve, no secret patterns).
4. For n8n changes: export from n8n, then remove `credentials` IDs, `pinData` and any instance-specific IDs before committing.
5. Open a pull request and describe how you tested it, including the n8n version.
