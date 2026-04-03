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
```

## Installation and setup

* **Clone the repo**

```bash
git clone https://github.com/adc-eng/pdf-text-extractor.git
cd pdf-text-extractor 
```

* **Sync the environment**

```bash
cd pdf-text-extractor
uv sync
```

This command will automatically download the required Python version, create a .venv, and install all dependencies (pypdf, pdf2image, pytesseract) in editable mode.

## Usage

You can run the extractor directly using uv run. This ensures the command executes within the correct virtual environment context without needing to "activate" the shell.

To extract text from a file and save it to a document, run the following command from the pdf-text-extractor directory:

```bash
uv run pdf-extract <path_to_your_pdf> > output.txt
```

## How it works

This utility employs a multi-stage approach to ensure no text is left behind:

* **Text Layer Extraction** (pypdf): First, it attempts to pull "native" text stored in the PDF metadata. This should be near-instant.

* **PDF to Image** (pdf2image + poppler): If the PDF is a scan or contains images, pdf2image (using the poppler backend) converts the PDF pages into high-resolution images.

* **OCR(Optical Character Recognition)** using pytesseract + tesseract: Finally, it uses the Tesseract OCR engine to "read" the text from those images, allowing you to extract content even from flat image files.

## set up .gitignore
To keep your repository clean, ensure you have a .gitignore file in your root directory containing:
.venv/
__pycache__/
*.pyc
.DS_Store
.python-version


## License
MIT
