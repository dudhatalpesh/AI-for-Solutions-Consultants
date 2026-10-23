"""Lab 04: evaluate the RAG workflow against a small golden dataset.

Usage (workflow 03 published):
    python labs/lab-04-n8n-rag-knowledge-assistant/eval_rag.py
    python labs/lab-04-n8n-rag-knowledge-assistant/eval_rag.py --url http://localhost:5678/webhook-test/rag-query

Scores per question:
  keyword_ok  - all expected keywords appear in the answer (case-insensitive)
  source_ok   - the expected source file is cited (answerable questions only)
  refusal_ok  - unanswerable questions get the insufficient-context message
"""
from __future__ import annotations

import argparse
import csv
import json
import os
import statistics
import time
from pathlib import Path

import httpx

HERE = Path(__file__).parent
DEFAULT_URL = os.getenv("N8N_BASE_URL", "http://localhost:5678") + "/webhook/rag-query"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--url", default=DEFAULT_URL)
    ap.add_argument("--eval", default=str(HERE / "eval-set.jsonl"))
    ap.add_argument("--out", default="rag-eval-results.csv")
    args = ap.parse_args()

    cases = [json.loads(line) for line in Path(args.eval).read_text(encoding="utf-8").splitlines() if line.strip()]
    rows, latencies = [], []
    for c in cases:
        start = time.perf_counter()
        try:
            r = httpx.post(args.url, json={"question": c["question"]}, timeout=300)
            answer = r.json().get("answer", "") if r.status_code == 200 else f"HTTP {r.status_code}"
        except (httpx.HTTPError, ValueError) as e:
            answer = f"ERROR {e!r}"
        secs = time.perf_counter() - start
        latencies.append(secs)
        low = answer.lower()
        keyword_ok = all(k.lower() in low for k in c["expected_keywords"])
        if c["type"] == "answerable":
            source_ok = c["expected_source"].lower() in low
            refusal_ok = "enough information" not in low
        else:
            source_ok = True
            refusal_ok = "enough information" in low
        passed = keyword_ok and source_ok and refusal_ok
        rows.append({"id": c["id"], "type": c["type"], "pass": passed, "keyword_ok": keyword_ok,
                     "source_ok": source_ok, "refusal_ok": refusal_ok, "latency_s": round(secs, 1),
                     "answer": answer[:300].replace("\n", " ")})
        print(f"{c['id']} {'PASS' if passed else 'FAIL'}  {secs:5.1f}s  {answer[:90]!r}")

    with open(args.out, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0]))
        w.writeheader()
        w.writerows(rows)

    passed = sum(r["pass"] for r in rows)
    p95 = sorted(latencies)[max(0, int(round(0.95 * len(latencies))) - 1)]
    print(f"\nPassed {passed}/{len(rows)} ({passed / len(rows):.0%}) | median {statistics.median(latencies):.1f}s | p95 {p95:.1f}s")
    print(f"Details written to {args.out}")


if __name__ == "__main__":
    main()
