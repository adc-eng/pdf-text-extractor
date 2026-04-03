# PDF Text Extractor

A high-performance, **privacy-focused** Python utility for extracting text from any PDF—including scanned documents—completely on your local machine.

## Why use this?

While cloud services (like Google Docs or online converters) offer PDF-to-text features, they often require you to upload your files to their servers. 

* **Privacy First:** This tool runs 100% locally. Your data never leaves your Mac. This is essential for sensitive documents, school records, or private research.
* **Hybrid Extraction:** It intelligently handles both digital PDFs (text-based) and scanned PDFs (image-based) using OCR.
* **Developer Friendly:** Built with `uv` for lightning-fast setup and reproducible environments without the headache of manual virtual environment management.

---

## Prerequisites (macOS)

This tool relies on system-level libraries for image processing and OCR that cannot be installed via Python's `uv`. You must install these using [Homebrew](https://brew.sh/):

```bash
brew install tesseract
brew install poppler
