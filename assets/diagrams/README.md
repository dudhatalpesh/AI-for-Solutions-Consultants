# assets/diagrams

Exported diagram images (PNG/SVG) for slides and offline use.

- Source of truth: the Mermaid diagrams inside the Markdown files (they render on GitHub).
- Export with the [Mermaid CLI](https://github.com/mermaid-js/mermaid-cli) (Open source, Local), for example:
  `npx -p @mermaid-js/mermaid-cli mmdc -i input.mmd -o output.svg`
- Name files `<area>-<topic>.svg`, e.g. `arch-secure-ai-reference.svg`.
