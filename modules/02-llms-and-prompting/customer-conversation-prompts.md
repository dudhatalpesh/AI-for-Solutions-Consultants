# Module 02 — Customer Conversation Prompts

> **Status: outline.** Structure and key points are in place; full content is tracked in [docs/11-suggested-first-issues.md](../../docs/11-suggested-first-issues.md).

## Discovery questions

1. Who will write and maintain prompts after go-live?
2. How will you know if a prompt change makes things worse?
3. Which outputs must follow a strict format for downstream systems?
4. What tone, brand or compliance rules must outputs follow?

## Executive explanation (60 seconds)

> Prompting is how we instruct the model. Good prompts make results consistent and on-brand, but prompting alone can't give the model knowledge it doesn't have or make it safe to act. We treat prompts like code — versioned, tested against examples, and reviewed.

## Objections and responses

| Objection | Response |
|---|---|
| We'll just hire a prompt engineer | Prompting is a skill your existing team can learn; the bigger wins are process design, grounding and evaluation. |
| Why not fine-tune instead? | Fine-tuning changes style and format well but is costlier to maintain; start with prompting + RAG and fine-tune only when evaluation shows a gap. |
