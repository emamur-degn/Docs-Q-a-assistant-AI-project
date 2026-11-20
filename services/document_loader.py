from io import BytesIO
from pypdf import PdfReader


def load_uploaded_files(uploaded_files):
    """Extract text from uploaded PDF and TXT files."""
    documents = []

    for uploaded in uploaded_files:
        filename = uploaded.name
        content = uploaded.getvalue()

        if filename.lower().endswith(".pdf"):
            reader = PdfReader(BytesIO(content))
            for page_number, page in enumerate(reader.pages, start=1):
                text = page.extract_text() or ""
                if text.strip():
                    documents.append({
                        "filename": filename,
                        "page": page_number,
                        "text": text
                    })
        elif filename.lower().endswith(".txt"):
            text = content.decode("utf-8", errors="ignore")
            if text.strip():
                documents.append({
                    "filename": filename,
                    "page": 1,
                    "text": text
                })

    return documents
