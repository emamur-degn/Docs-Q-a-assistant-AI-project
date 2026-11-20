# Docs Q&A Assistant

A beginner-friendly Python project that lets users upload PDF/TXT documents and search for relevant passages with source citations.

## Features
- Upload multiple PDF and TXT files
- Extract text from PDFs
- Split text into overlapping chunks
- Search for relevant passages using simple keyword matching
- Show the source filename and page number
- No paid API key required

> This is a normal starter project, not a full generative-AI/RAG system yet. It retrieves matching passages but does not write AI-generated answers.

## Project structure

```text
docs_qa_assistant/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── data/
│   └── documents/
└── services/
    ├── __init__.py
    ├── document_loader.py
    ├── text_chunker.py
    ├── search_engine.py
    └── citations.py
```

## Setup (Windows PowerShell)

1. Extract the ZIP file.
2. Open the extracted project folder in VS Code.
3. Create a virtual environment:

   ```powershell
   python -m venv venv
   ```

4. Activate it:

   ```powershell
   .\\venv\\Scripts\\Activate.ps1
   ```

5. Install packages:

   ```powershell
   pip install -r requirements.txt
   ```

6. Run the app:

   ```powershell
   streamlit run app.py
   ```

7. Open the local address shown in the terminal (usually http://localhost:8501).

## How to use
1. Upload one or more PDF or TXT files.
2. Enter a question using words that appear in the documents.
3. Click **Search documents**.
4. Review the matching passages and their source citations.

## Next improvements
- Add semantic embeddings
- Connect a vector database such as Qdrant
- Add an LLM to generate answers grounded in retrieved passages
- Add login and document permissions
