# utils.py
import os
import fitz  # PyMuPDF

def extract_text_from_pdf(file):
    text = ""
    try:
        doc = fitz.open(stream=file.read(), filetype="pdf")
        for page in doc:
            text += page.get_text()
    except Exception as e:
        print(f"Error reading file: {e}")
    return text
