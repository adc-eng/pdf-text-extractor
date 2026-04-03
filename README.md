# PDF Text Extractor (OCR-Enhanced)

A Python utility designed for extracting structured text from both digital and scanned PDF documents. Built with a focus on modern development ergonomics and reproducible environments.

## Architecture & Tooling

* **Environment Management**: uv (Rust-based Python bundler) for sub-millisecond dependency resolution.

* **OCR Engine**: Tesseract OCR (via pytesseract) for processing image-based PDF layers.

* **PDF Parsing**: pypdf for efficient extraction of text-based metadata and content.

* **Runtime**: Python 3.9+ (compatible with Intel and Apple Silicon macOS).

## Prerequisites

Ensure you have the following system dependencies installed (via Homebrew on macOS):

```bash
brew install tesseract
brew install uv
```


## Quick Start

This project uses uv to manage its virtual environment and dependencies automatically. No manual pip install or venv activation is required.

Clone the repository:

```bash
git clone git@github.com:adc-eng/pdf-text-extractor.git
cd pdf-text-extractor
```


Run extraction:

```bash
uv run pdf-extract path/to/document.pdf > output.txt
```


Local Development

To sync the environment for local development or testing:

```bash
cd pdf-text-extractor
uv sync
```


## License

MIT License - see LICENSE for details.
