from PIL import Image
import pytesseract
import re
import os
from pdf2image import convert_from_path

# Set Tesseract OCR path (Windows)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set Poppler path (change based on your PC)
POPPLER_PATH = r"C:\poppler\bin"


def extract_health_metrics(filepath):
    ext = os.path.splitext(filepath)[1].lower()

    if ext == '.pdf':
        # Convert PDF to image (first page only)
        images = convert_from_path(filepath, poppler_path=POPPLER_PATH)
        img = images[0]  # first page
    else:
        img = Image.open(filepath)

    text = pytesseract.image_to_string(img)

    print("OCR Output:\n", text)

    bp_match = re.search(
        r"(BP|Blood Pressure)[^\d]*(\d+)", text, re.IGNORECASE)
    sugar_match = re.search(r"(Sugar|Glucose)[^\d]*(\d+)", text, re.IGNORECASE)
    chol_match = re.search(r"(Cholesterol)[^\d]*(\d+)", text, re.IGNORECASE)

    return {
        "bp": int(bp_match.group(2)) if bp_match else None,
        "sugar": int(sugar_match.group(2)) if sugar_match else None,
        "cholesterol": int(chol_match.group(2)) if chol_match else None
    }
