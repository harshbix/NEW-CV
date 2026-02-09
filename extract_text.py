from pypdf import PdfReader
import os

pdf_path = "CV ANNA MARGARETH NJAU (1).pdf"

if os.path.exists(pdf_path):
    try:
        reader = PdfReader(pdf_path)
        print("--- START TEXT EXTRACTION ---")
        for page in reader.pages:
            print(page.extract_text())
        print("--- END TEXT EXTRACTION ---")
    except Exception as e:
        print(f"Error reading PDF: {e}")
else:
    print(f"File not found: {pdf_path}")
