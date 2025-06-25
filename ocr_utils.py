# File: ocr_utils.py

import pytesseract
import re
from datetime import datetime
import cv2

import shutil
tesseract_path = shutil.which("tesseract")
if tesseract_path:
    pytesseract.pytesseract.tesseract_cmd = tesseract_path
else:
    raise EnvironmentError("Tesseract not found. Make sure it's installed in the system.")


def extract_dob_and_age(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray, lang="eng+hin")
    print("OCR TEXT OUTPUT:\n", text)

    # Try to find DOB using multiple patterns
    date_patterns = [
        r"DOB[:\s]*([0-9]{2}[-/][0-9]{2}[-/][0-9]{4})",
        r"जन्म[:\s\S]*?([0-9]{2}[-/][0-9]{2}[-/][0-9]{4})",
        r"([0-9]{2}[-/][0-9]{2}[-/][0-9]{4})"
    ]

    for pattern in date_patterns:
        match = re.search(pattern, text, flags=re.IGNORECASE)
        if match:
            dob_str = match.group(1)
            for fmt in ["%d/%m/%Y", "%d-%m-%Y"]:
                try:
                    dob = datetime.strptime(dob_str, fmt).date()
                    age = (datetime.now().date() - dob).days // 365
                    return dob, age, age >= 18
                except ValueError:
                    continue
    return None, None, None
