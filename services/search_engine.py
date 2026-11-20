import re
from collections import Counter


def tokenize(text):
    return re.findall(r"[a-zA-Z0-9_]+", text.lower())


def search_chunks(question, chunks, top_k=5):
    """Simple keyword relevance search; no API key required."""
    query_terms = set(tokenize(question))
    if not query_terms:
        return []

    scored = []
    for chunk in chunks:
        words = tokenize(chunk["text"])
        counts = Counter(words)
        score = sum(counts[term] for term in query_terms)
        if score:
            item = dict(chunk)
            item["score"] = score
            scored.append(item)

    scored.sort(key=lambda item: item["score"], reverse=True)
    return scored[:top_k]
