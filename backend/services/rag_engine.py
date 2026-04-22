from sentence_transformers import SentenceTransformer, util
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

with open("knowledge/incidents.json") as f:
    incidents = json.load(f)

doc_embeddings = model.encode(documents)

index = faiss.IndexFlatL2(len(doc_embeddings[0]))
index.add(np.array(doc_embeddings))



def get_similar_solution(ticket):

    ticket_embedding = model.encode(ticket)

    best_score = 0
    best_solution = None

    for incident in incidents:
        emb = model.encode(incident["ticket"])
        score = util.cos_sim(ticket_embedding, emb)

        if score > best_score:
            best_score = score
            best_solution = incident["solution"]

    return best_solution

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