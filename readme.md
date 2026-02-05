# 📄 Multilingual RAG-Based Intelligent Document Assistant

## 🚀 Project Overview

This project is a Retrieval-Augmented Generation (RAG) system that enables users to upload PDF documents and ask questions about them in English or Hindi.

The assistant supports:

- 📊 Structured Data (Bank Statements)
- 🧾 Semi-Structured Data (Invoices)
- 📜 Unstructured Data (Rent Agreements)

It extracts information, retrieves relevant context using vector embeddings, and generates accurate responses using a local LLM (Mistral via Ollama).

---

## 🎯 Problem Statement

Organizations deal with multiple document formats such as invoices, legal agreements, and financial statements. Extracting information manually is time-consuming and error-prone.

This project builds a smart assistant that:

- Understands structured and unstructured PDFs
- Performs contextual question answering
- Supports multilingual interaction
- Provides optional voice output

---

## 🧠 System Architecture

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

## 📸 Screenshots

### Upload Interface
![Upload](assets\upload.png)

### Question Answering in english & hindi with audio
![Chat](assets/chat_en_audio.png)
![Chat](assets/chat_hi_audio.png)




