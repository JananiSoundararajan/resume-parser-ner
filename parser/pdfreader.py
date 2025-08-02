import fitz  # PyMuPDF

def extract_text_from_pdf(pdf_file):
    # If pdf_file is a file-like object (e.g., from Streamlit), use .read() and open with bytes
    if hasattr(pdf_file, "read"):
        doc = fitz.open(stream=pdf_file.read(), filetype="pdf")
    else:
        doc = fitz.open(pdf_file)
    text = ""
    for page in doc:
        text += page.get_text()
    return text