from openai import OpenAI
import chromadb

client = OpenAI()
chroma_client = chromadb.PersistentClient(path="backend/data/embeddings")
collection = chroma_client.get_collection("study_docs")

def query_rag(user_query):
    # Step 1: Embed query
    query_emb = client.embeddings.create(model="text-embedding-3-small", input=user_query).data[0].embedding

    # Step 2: Retrieve top matches
    results = collection.query(query_embeddings=[query_emb], n_results=3)
    retrieved_docs = " ".join([doc for doc in results["documents"][0]])

    # Step 3: Send to LLM
    prompt = f"Use the following notes to answer:\n{retrieved_docs}\n\nQuestion: {user_query}\nAnswer:"
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "system", "content": "You are a helpful study assistant."},
                  {"role": "user", "content": prompt}]
    )
    return completion.choices[0].message.content
