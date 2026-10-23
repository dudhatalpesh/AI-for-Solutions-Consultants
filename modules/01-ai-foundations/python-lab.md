# Module 01 — Python Lab: See Tokens, Latency and Embeddings

**Time:** 30–45 minutes · **Difficulty:** Beginner · **Tools:** Python 3.11+ (Open source, Local), Ollama (Open source, Local), httpx

## Objective

Measure three things you will talk about with customers: token counts, latency, and semantic similarity.

## Prerequisites

- Stack running (`docker compose up -d`) with `llama3.2` and `nomic-embed-text` pulled.
- Virtual env with `pip install -r requirements.txt`.

## Step 1 — Tokens and latency

Ollama's `/api/generate` endpoint returns token counts (`prompt_eval_count`, `eval_count`) and durations in nanoseconds. See the [Ollama API docs](https://github.com/ollama/ollama/blob/main/docs/api.md).

Save as `tokens_latency.py` anywhere (for example in your own scratch folder):

```python
"""Measure tokens and latency for a few prompts on a local Ollama model."""
import os
import time

import httpx

OLLAMA = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_CHAT_MODEL", "llama3.2")

PROMPTS = {
    "short": "Define zero trust in one sentence.",
    "medium": "Explain zero trust to a CFO in 150 words.",
    "long_answer": "Write a detailed 600-word explanation of zero trust architecture.",
}

for name, prompt in PROMPTS.items():
    start = time.perf_counter()
    r = httpx.post(
        f"{OLLAMA}/api/generate",
        json={"model": MODEL, "prompt": prompt, "stream": False, "options": {"temperature": 0.2}},
        timeout=300,
    )
    r.raise_for_status()
    data = r.json()
    wall = time.perf_counter() - start
    out_tokens = data.get("eval_count", 0)
    gen_seconds = data.get("eval_duration", 1) / 1e9
    print(
        f"{name:12s} in={data.get('prompt_eval_count', 0):4d} tok  "
        f"out={out_tokens:4d} tok  wall={wall:6.1f}s  "
        f"speed={out_tokens / gen_seconds:5.1f} tok/s"
    )
```

Run:

```bash
python tokens_latency.py
```

**Expected:** output tokens and wall time grow together; `long_answer` is much slower than `short`. Exact numbers depend on your hardware.

**Discuss:** if a cloud model charged per output token, which prompt costs most? How would you shorten it?

## Step 2 — Embedding similarity

Ollama's `/api/embed` endpoint returns `embeddings` (a list of vectors).

Save as `similarity.py`:

```python
"""Show that embeddings capture meaning, not keywords."""
import math
import os

import httpx

OLLAMA = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
MODEL = os.getenv("OLLAMA_EMBED_MODEL", "nomic-embed-text")

texts = [
    "I can't log in to my laptop",
    "Please reset my password",
    "What is the cafeteria menu today?",
    "Our VPN keeps disconnecting",
]

r = httpx.post(f"{OLLAMA}/api/embed", json={"model": MODEL, "input": texts}, timeout=120)
r.raise_for_status()
vecs = r.json()["embeddings"]
print(f"Vector dimension: {len(vecs[0])}")


def cos(a, b):
    dot = sum(x * y for x, y in zip(a, b))
    return dot / (math.sqrt(sum(x * x for x in a)) * math.sqrt(sum(y * y for y in b)))


query = 0
for i, t in enumerate(texts):
    print(f"{cos(vecs[query], vecs[i]):.3f}  {t}")
```

**Expected:** "Please reset my password" scores clearly higher against "I can't log in to my laptop" than the cafeteria sentence does, even though they share no keywords. The dimension printed is the vector size your Qdrant collection must match.

## Validation

- [ ] Step 1 prints three rows with token counts and timings.
- [ ] Step 2 prints the vector dimension and a similarity ranking that makes sense.

## Stretch goals

1. Run Step 1 with `llama3.1:8b` (if you have RAM) and compare speed.
2. Add a fifth sentence in another language and see where it ranks.
3. Plot similarity as a heatmap in JupyterLab.

## Customer talking point

> "Tokens are the unit of cost and speed. In the POC we will measure tokens per transaction so the business case uses real numbers, not vendor averages."
