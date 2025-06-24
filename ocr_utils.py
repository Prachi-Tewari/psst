# File: ocr_utils.py

import pytesseract
import re
from datetime import datetime
import cv2

# Highlighted input: No API key needed here, just make sure Tesseract is installed

def extract_dob_and_age(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    text = pytesseract.image_to_string(gray)

    # You can test regex based on your Aadhar sample
    dob_match = re.search(r"(\\d{2}/\\d{2}/\\d{4})", text)
    if dob_match:
        dob_str = dob_match.group(1)
        dob = datetime.strptime(dob_str, "%d/%m/%Y").date()
        age = (datetime.now().date() - dob).days // 365
        return dob, age, age >= 18
    return None, None, None
