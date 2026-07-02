# 📄 PDF RAG Assistant

A Retrieval-Augmented Generation (RAG) application that allows users to upload PDF documents and ask questions in natural language.

## Features

- Upload multiple PDF documents
- Extract text using pdfplumber
- Custom text chunking
- Semantic search using Sentence Transformers
- FAISS Vector Database
- Llama 3.3 via Groq API
- Streamlit interface

## Tech Stack

- Python
- Streamlit
- Sentence Transformers
- FAISS
- Groq API
- pdfplumber

## Installation

```bash
pip install -r requirements.txt
streamlit run app.py