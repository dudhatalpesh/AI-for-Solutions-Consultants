# Module 01 — Customer Conversation Prompts

## Discovery questions

Use these to qualify whether a customer's AI idea is real and viable.

1. "Which process, if it were twice as fast or half as error-prone, would matter most to your business this year?"
2. "Where does the information needed for that process live today, and who owns it?"
3. "What does an error cost you in that process — money, compliance, customer trust?"
4. "Which AI tools are your teams already using, officially or not?"
5. "What data are you **not** allowed to send outside your environment?"
6. "Who has to approve a new AI use case — security, legal, data protection, works council?"
7. "How would you measure success in 90 days?"
8. "What happens today when the answer is uncertain? Who decides?"

## Executive explanation (60 seconds)

> "Large language models are prediction engines for text. They're very good at reading, summarising, classifying and drafting, which is most of what knowledge workers do in processes like support, finance operations and security triage. They are not databases — they can sound confident and be wrong — so we design solutions that ground answers in your own data, check the outputs, and keep a person in the loop where mistakes matter. The value comes from putting AI **inside** a process with controls, not from a chatbot on its own."

## Technical explanation (2 minutes)

> "The model sees text as tokens and generates one token at a time based on everything in its context window — our instructions, the user's input, and any documents we retrieve. Cost and latency scale with tokens. We keep temperature low for structured tasks and force the output into a JSON schema that we validate in the workflow. For knowledge questions we use embeddings to retrieve relevant passages and require citations. We can run models locally for sensitive data or route to an approved cloud model, and everything is orchestrated and logged in n8n."

## Objections and responses

| Objection | Response |
|---|---|
| "It just makes things up." | "Yes, ungrounded models can. We ground answers in your documents, require citations, allow it to say 'I don't know', validate outputs, and measure the error rate in the POC on your own test set." |
| "We can't send our data to OpenAI." | "You don't have to. We can run open models locally inside your boundary, and only use a cloud model where your policy allows it." |
| "AI costs are unpredictable." | "Cost is driven by tokens and model choice. We'll measure tokens per transaction in the POC and size the business case on real numbers, with caps and alerts." |
| "Our people will just paste data into ChatGPT anyway." | "That's shadow AI, and it's a strong reason to provide an approved, governed alternative with logging and data controls." |
| "Let's wait until the technology settles." | "The models will keep changing; the process, data and governance work won't. A small, controlled POC builds that foundation and shows value now." |

## Practice

Record yourself giving the executive explanation. Keep it under 60 seconds, with no unexplained acronyms.
