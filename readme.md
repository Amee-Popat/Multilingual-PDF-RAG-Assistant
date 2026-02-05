# 📄 Multilingual PDF RAG Assistant

## 🚀 Project Overview

This project is a Retrieval-Augmented Generation (RAG) system that enables users to upload PDF documents and ask questions about them in English or Hindi.

The assistant supports:

- 📊 Structured Data (Bank Statements)
- 🧾 Semi-Structured Data (Invoices)
- 📜 Unstructured Data (Rent Agreements)

It extracts information, retrieves relevant context using vector embeddings, and generates accurate responses using a local LLM (Mistral via Ollama).

---

## ⭐ Key Highlights

- Strict hallucination-free document question answering
- Works completely offline using local LLM (Ollama + Mistral)
- Handles structured, semi-structured, and unstructured PDFs
- Finance-safe and legal-safe answer generation
- Beginner-friendly yet production-ready RAG architecture

---

## 🎯 Problem Statement

Organizations deal with multiple document formats such as invoices, legal agreements, and financial statements. Extracting information manually is time-consuming and error-prone.

This project builds a smart assistant that:

- Understands structured and unstructured PDFs
- Performs contextual question answering
- Supports multilingual interaction
- Provides optional voice output
- Answers are generated strictly from document content
- If information is missing, the assistant clearly responds with “Not mentioned in the document”
- Prevents logical guessing and numerical hallucinations in financial documents

---

## 🧠 System Architecture

The system follows a Retrieval-Augmented Generation (RAG) pipeline where
relevant document context is retrieved using vector similarity before generating
answers using a local large language model.

User  
⬇  
Streamlit Frontend  
⬇  
FastAPI Backend  
⬇  
PDF Processing (Native Text + OCR)  
⬇  
Text Chunking  
⬇  
Embedding (Sentence Transformers)  
⬇  
ChromaDB Vector Store  
⬇  
LLM (Mistral via Ollama)  
⬇  
Response Generation + Optional TTS  

---

## ✨ Features

- 📂 PDF Upload
- 🔍 Native Text Extraction + OCR fallback
- 🧩 Intelligent Chunking
- 🔎 Semantic Search using ChromaDB
- 🤖 Local LLM (Mistral)
- 🌍 English & Hindi Support
- 🔊 Text-to-Speech Output
- 🧠 Context-Grounded Prompting (Hallucination Reduction)
- 💬 Interactive Streamlit UI
- Reduces human error in financial and legal document analysis
- Improves accessibility with multilingual and audio responses

---

## 🛠 Tech Stack

Backend:
- FastAPI
- ChromaDB
- Sentence Transformers
- pdfplumber
- pytesseract
- Ollama (Mistral)

Frontend:
- Streamlit

AI Models:
- all-MiniLM-L6-v2 (Embeddings)
- Mistral (LLM via Ollama)
- Helsinki-NLP Translation Models
- gTTS (Text-to-Speech)

---

## ▶️ How to Run the Project

1. Create and activate virtual environment  
2. Install dependencies using `requirements.txt`  
3. Start Ollama with Mistral model  
4. Run FastAPI backend  
5. Launch Streamlit frontend  

Refer to the commands in the repository for local execution.

---

## 📸 Screenshots

### Upload Interface

![Upload](assets/upload.png)

### Question Answering (English)

![English QA](assets/chat_en_audio.png)

---

### Question Answering (Hindi)

![Hindi QA](assets/chat_hi_audio.png)


---

## 🧪 Example Use Cases

- Extract account details from bank statements
- Verify invoice totals and tax values
- Understand clauses in rent agreements
- Ask document questions in Hindi or English





