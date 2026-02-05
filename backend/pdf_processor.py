import pdfplumber
from pdf2image import convert_from_path
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(file_path):
    text = ""

    with pdfplumber.open(file_path) as pdf:
        for page in pdf.pages:

            # Better layout-aware extraction
            page_text = page.extract_text(x_tolerance=2, y_tolerance=2) or ""
            text += page_text + "\n"

            # Explicit table extraction
            tables = page.extract_tables()
            for table in tables:
                for row in table:
                    row_text = " | ".join(cell.strip() if cell else "" for cell in row)
                    text += row_text + "\n"

    # OCR fallback (only if almost empty)
    if len(text.strip()) < 100:
        images = convert_from_path(file_path)
        for img in images:
            text += pytesseract.image_to_string(img)

    return text.strip()
