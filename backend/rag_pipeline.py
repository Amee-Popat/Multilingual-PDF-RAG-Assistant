import requests
from backend.embeddings import generate_embeddings

def call_ollama(prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "mistral",
            "prompt": prompt,
            "stream": False,
            "options": {
                "temperature": 0.0
            }
        }
    )
    return response.json()["response"]


def generate_answer(collection, question, language):

    # 🔍 Embed the question
    question_embedding = generate_embeddings([question])[0]

    # 🔎 Retrieve relevant chunks
    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=3
    )

    docs = results.get("documents", [[]])[0]
    context = "\n\n".join(docs)

    if language == "hindi":
        instruction = """
आप एक सख्त दस्तावेज़ प्रश्न-उत्तर सहायक हैं।
केवल दस्तावेज़ में स्पष्ट रूप से लिखी गई जानकारी का उपयोग करें।
खुद से कोई गणना न करें।
Opening balance को credit न मानें।
यदि कुल राशि स्पष्ट रूप से नहीं दी गई है, तो केवल दिए गए credit amount को लिखें।
उत्तर छोटा और तथ्यात्मक रखें।
केवल हिंदी में उत्तर दें।
"""


    else:
        instruction = """
You are a strict document question-answering assistant.
Answer ONLY using explicitly stated facts from the context.
Do NOT perform calculations unless the result is explicitly written in the document.
Do NOT include opening balance when asked about credits.
If aggregation is required and not explicitly stated, answer with the exact amounts listed.
Keep the answer short and factual.
Respond in English only.
"""


    prompt = f"""
{instruction}

Context:
{context}

Question:
{question}

Answer:
"""

    return call_ollama(prompt).strip()
