import argparse
from .core import extract_text_from_pdf


def main():
    parser = argparse.ArgumentParser(description="Extract text from PDF")
    parser.add_argument("file", help="Path to PDF file")
    parser.add_argument("--flat", action="store_true", help="Return all text as one block")

    args = parser.parse_args()

    pages = extract_text_from_pdf(args.file)

    if args.flat:
        print("\n".join(pages))
    else:
        for i, text in enumerate(pages):
            print(f"\n--- Page {i+1} ---\n{text}")
