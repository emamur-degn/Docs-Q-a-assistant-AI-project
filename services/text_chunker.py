def split_into_chunks(text, filename, page, chunk_size=900, overlap=150):
    """Split document text into overlapping chunks."""
    clean_text = " ".join(text.split())
    chunks = []

    if not clean_text:
        return chunks

    start = 0
    while start < len(clean_text):
        end = min(start + chunk_size, len(clean_text))
        chunk_text = clean_text[start:end].strip()

        if chunk_text:
            chunks.append({
                "filename": filename,
                "page": page,
                "text": chunk_text
            })

        if end == len(clean_text):
            break
        start = max(0, end - overlap)

    return chunks
