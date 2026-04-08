from sentence_transformers import SentenceTransformer
import numpy as np
import faiss
import json

model = SentenceTransformer("all-MiniLM-L6-v2")

documents = [
"VPN connection issue can be solved by restarting the VPN client",
"Password reset issues can be solved by resetting via admin portal",
"Email sync issues can be fixed by clearing Outlook cache",
"Laptop hanging issues can be caused by high CPU usage or insufficient RAM",
"Laptop freezing can be resolved by updating drivers and scanning for malware",
"System performance issues may require closing background applications"
]

doc_embeddings = model.encode(documents)

index = faiss.IndexFlatL2(len(doc_embeddings[0]))
index.add(np.array(doc_embeddings))

def get_similar_solution(query):

    query_vector = model.encode([query])

    D, I = index.search(np.array(query_vector), k=1)

    distance = D[0][0]
    idx = I[0][0]

    THRESHOLD = 0.6

    if distance > THRESHOLD:
        return "No relevant knowledge base article found."

    return documents[idx]

def get_similar_tickets(query, k=3):
    query_vector = model.encode([query])
    D, I = index.search(np.array(query_vector), k=k)

    results = []
    for idx in I[0]:
        results.append(documents[idx])

    return results

def load_learned_incidents():

    try:
        with open("knowledge/incidents.json", "r") as f:
            data = json.load(f)
            return [item["ticket"] + " : " + item["solution"] for item in data]
    except:
        return []