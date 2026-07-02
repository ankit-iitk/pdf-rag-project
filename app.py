import os
import streamlit as st

from dotenv import load_dotenv

from src.loader import load_documents
from src.chunker import create_chunks
from src.embeddings import EmbeddingModel
from src.retriever import Retriever
from src.rag import RAG

load_dotenv()

st.set_page_config(
    page_title="PDF RAG Assistant",
    page_icon="📄",
    layout="wide"
)

st.title("📄 PDF RAG Assistant")

uploaded_files = st.file_uploader(
    "Upload PDF files",
    type=["pdf"],
    accept_multiple_files=True
)

if uploaded_files:

    documents = load_documents(uploaded_files)

    chunks = create_chunks(documents)

    embedding_model = EmbeddingModel()

    embeddings = embedding_model.create_embeddings(chunks)

    index = embedding_model.create_faiss_index(embeddings)

    retriever = Retriever(
        index=index,
        chunks=chunks,
        embedding_model=embedding_model
    )

    rag = RAG()

    st.success("Documents Indexed Successfully!")

    question = st.text_input(
        "Ask a question"
    )

    if question:

        retrieved_chunks = retriever.search(question)

        answer = rag.generate_answer(
            question,
            retrieved_chunks
        )

        st.subheader("Answer")

        st.write(answer)

        st.subheader("Sources")

        for chunk in retrieved_chunks:

            st.markdown(
                f"""
**File:** {chunk['file']}

**Page:** {chunk['page']}

{chunk['text'][:300]}...
"""
            )