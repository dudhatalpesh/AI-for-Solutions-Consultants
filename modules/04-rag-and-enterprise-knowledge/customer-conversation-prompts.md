# Module 04 — Customer Conversation Prompts

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

## Discovery questions

1. Which repositories hold the source content, and how often does it change?
2. Are documents permissioned differently for different users?
3. What happens today when someone gets a wrong policy answer?
4. Which formats: PDFs, wiki pages, tickets, spreadsheets?
5. Who owns content quality?

## Executive explanation (60 seconds)

> RAG lets the assistant answer from your own documents, with citations, without retraining a model. Quality depends mostly on your content and retrieval design, so the POC focuses on a representative set of questions and measures how often answers are correct and properly sourced.

## Objections and responses

| Objection | Response |
|---|---|
| Why not just use a bigger context window? | Cost, latency and accuracy degrade with huge contexts, and you still need permissions and freshness. Retrieval sends only what's relevant. |
| Our documents are a mess | That's common. The POC starts with one well-owned collection and shows the value of cleaning up the rest. |
