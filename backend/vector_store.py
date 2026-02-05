import chromadb
from chromadb.config import Settings

client = chromadb.Client(
    Settings(
        persist_directory="chroma_db",
        is_persistent=True,
        anonymized_telemetry=False
    )
)

def create_collection(collection_name):
    return client.get_or_create_collection(name=collection_name)

def store_embeddings(collection, chunks, embeddings):
    ids = [f"id_{i}" for i in range(len(chunks))]
    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )

def query_collection(collection, query_embedding):
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=5
    )
    return results["documents"][0]
