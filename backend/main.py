from fastapi import FastAPI, UploadFile, File
import shutil
import os
from backend.pdf_processor import extract_text_from_pdf
from backend.chunking import chunk_text
from backend.embeddings import generate_embeddings
from backend.vector_store import create_collection, store_embeddings
from backend.rag_pipeline import generate_answer
from backend.tts import generate_audio

app = FastAPI()

os.makedirs("uploads", exist_ok=True)

@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    path = f"uploads/{file.filename}"

    with open(path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    text = extract_text_from_pdf(path)
    chunks = chunk_text(text)
    embeddings = generate_embeddings(chunks)

    clean_name = file.filename.replace(" ", "_").replace(".pdf", "")
    collection = create_collection(clean_name)

    store_embeddings(collection, chunks, embeddings)

    return {"message": "File processed successfully", "collection": clean_name}


@app.post("/ask/")
async def ask_question(collection_name: str, question: str, language: str, audio: bool):

    collection = create_collection(collection_name)
    answer = generate_answer(collection, question, language)

    audio_path = None
    if audio:
        audio_path = generate_audio(answer, language)

    return {
        "answer": answer,
        "audio": audio_path
    }
