"""Lab 05: turn a document into text (OCR for images, text extraction for PDFs) and post it to n8n.

Usage:
    python labs/lab-05-n8n-document-intelligence-workflow/ocr_to_text.py sample-docs/invoice-good.txt
    python labs/lab-05-n8n-document-intelligence-workflow/ocr_to_text.py scan.png --post
    python labs/lab-05-n8n-document-intelligence-workflow/ocr_to_text.py invoice.pdf --post --url http://localhost:5678/webhook-test/lab05-document

- .txt  -> read as-is
- .pdf  -> text layer via pypdf (scanned PDFs without a text layer need OCR: convert pages to images first)
- .png/.jpg/.jpeg/.tif -> OCR via pytesseract (requires the Tesseract binary on PATH)
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path

import httpx

DEFAULT_URL = os.getenv("N8N_BASE_URL", "http://localhost:5678") + "/webhook/lab05-document"


def to_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".txt":
        return path.read_text(encoding="utf-8")
    if suffix == ".pdf":
        from pypdf import PdfReader

        return "\n".join((page.extract_text() or "") for page in PdfReader(str(path)).pages)
    if suffix in {".png", ".jpg", ".jpeg", ".tif", ".tiff"}:
        import pytesseract
        from PIL import Image

        return pytesseract.image_to_string(Image.open(path))
    raise SystemExit(f"Unsupported file type: {suffix}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--post", action="store_true", help="send the text to the n8n workflow")
    ap.add_argument("--url", default=DEFAULT_URL)
    args = ap.parse_args()

    path = Path(args.file)
    if not path.exists():
        path = Path(__file__).parent / args.file
    text = to_text(path)
    print(f"--- extracted {len(text)} characters from {path.name} ---\n{text[:800]}\n")

    if args.post:
        r = httpx.post(args.url, json={"doc_id": path.stem.upper(), "text": text}, timeout=300)
        print(f"HTTP {r.status_code}")
        try:
            print(json.dumps(r.json(), indent=2))
        except ValueError:
            print(r.text)


if __name__ == "__main__":
    main()
