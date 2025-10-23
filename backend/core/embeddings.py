import chromadb
from openai import OpenAI
from core.utils import chunk_text

client = OpenAI()
chroma_client = chromadb.PersistentClient(path="backend/data/embeddings")
collection = chroma_client.get_or_create_collection("study_docs")

def create_embeddings(text, filename):
    chunks = chunk_text(text)
    for i, chunk in enumerate(chunks):
        emb = client.embeddings.create(model="text-embedding-3-small", input=chunk).data[0].embedding
        collection.add(
            documents=[chunk],
            embeddings=[emb],
            metadatas=[{"source": filename}],
            ids=[f"{filename}_{i}"]
        )
    return "Embeddings stored successfully"
