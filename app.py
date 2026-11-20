import streamlit as st
from services.document_loader import load_uploaded_files
from services.text_chunker import split_into_chunks
from services.search_engine import search_chunks
from services.citations import format_citation

st.set_page_config(page_title="Docs Q&A Assistant", page_icon="📚", layout="wide")
st.title("📚 Docs Q&A Assistant")
st.write("Upload PDF or TXT files, then ask questions about their contents.")

uploads = st.file_uploader(
    "Upload your documents",
    type=["pdf", "txt"],
    accept_multiple_files=True
)

if "chunks" not in st.session_state:
    st.session_state.chunks = []

if uploads:
    documents = load_uploaded_files(uploads)
    chunks = []
    for doc in documents:
        chunks.extend(split_into_chunks(
            text=doc["text"],
            filename=doc["filename"],
            page=doc["page"]
        ))
    st.session_state.chunks = chunks
    st.success(f"Loaded {len(documents)} document page(s) and created {len(chunks)} text chunks.")

question = st.text_input("Ask a question", placeholder="Example: What is the company's leave policy?")

if st.button("Search documents", type="primary"):
    if not st.session_state.chunks:
        st.warning("Please upload at least one PDF or TXT file first.")
    elif not question.strip():
        st.warning("Please enter a question.")
    else:
        results = search_chunks(question, st.session_state.chunks, top_k=5)
        if not results:
            st.info("No matching text was found. Try different keywords.")
        else:
            st.subheader("Relevant information")
            st.caption("This starter version finds relevant passages. It does not generate answers with an external AI model.")
            for result in results:
                with st.container(border=True):
                    st.write(result["text"])
                    st.caption(format_citation(result))
