from fastapi import FastAPI, UploadFile, File, Form
from typing import List
from db import init_weaviate
from contextlib import asynccontextmanager
import uuid
import os

from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from PyPDF2 import PdfReader

# -------------------------
# Lifespan: Startup/Shutdown
# -------------------------
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.client = init_weaviate()
    # Load embedding model (open-source)
    app.state.embedder = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-mpnet-base-v2"
    )
    yield
    app.state.client.close()

app = FastAPI(lifespan=lifespan)

# -------------------------
# Utils
# -------------------------
def extract_text_from_pdf(file: UploadFile):
    """Extract text from PDF, page by page"""
    pdf_reader = PdfReader(file.file)
    pages = []
    for i, page in enumerate(pdf_reader.pages):
        text = page.extract_text()
        if text:
            pages.append((i + 1, text))  # (page_no, text)
    return pages


def chunk_text(text: str, chunk_size=800, chunk_overlap=100):
    """Split long text into smaller chunks"""
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len
    )
    return splitter.split_text(text)

# -------------------------
# Routes
# -------------------------
@app.get("/")
def hello():
    return {"message": "Hello World lol"}

@app.get("/check")
def check_weaviate():
    return {"weaviate_ready": app.state.client.is_ready()}

@app.post("/upload_policies/")
async def upload_policies(
    company_id: str = Form(...),
    files: List[UploadFile] = File(...)
):
    """
    Upload multiple PDFs for a company, 
    chunk them, embed, and store in Weaviate tenant space
    """
    client = app.state.client
    embedder = app.state.embedder

    stored_chunks = []

    for file in files:
        pdf_name = file.filename
        pages = extract_text_from_pdf(file)

        for page_no, page_text in pages:
            # Split into chunks
            chunks = chunk_text(page_text)

            for chunk in chunks:
                # Generate embedding
                vector = embedder.embed_query(chunk)

                # Prepare object
                obj = {
                    "text": chunk,
                    "page_no": page_no,
                    "pdf_name": pdf_name
                }

                # Push to Weaviate with tenant (company_id)
                client.data_object.create(
                    data_object=obj,
                    class_name="PolicyDocument",
                    tenant=company_id,
                    uuid=str(uuid.uuid4()),
                    vector=vector
                )

                stored_chunks.append(obj)

    return {
        "status": "success",
        "company_id": company_id,
        "chunks_stored": len(stored_chunks)
    }

