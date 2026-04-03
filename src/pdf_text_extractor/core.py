from pypdf import PdfReader
from pdf2image import convert_from_path
import pytesseract


def extract_text_from_pdf(pdf_path: str):
    text_pages = []
    reader = PdfReader(pdf_path)

    for i, page in enumerate(reader.pages):
        text = page.extract_text()

        if text and text.strip():
            text_pages.append(text)
        else:
            images = convert_from_path(pdf_path, first_page=i+1, last_page=i+1)
            if images:
                ocr_text = pytesseract.image_to_string(images[0])
                text_pages.append(ocr_text)
            else:
                text_pages.append("")

    return text_pages
