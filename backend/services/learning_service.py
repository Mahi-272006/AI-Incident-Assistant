import json

FILE_PATH = "knowledge/incidents.json"

def save_incident(ticket, solution):

    try:
        with open(FILE_PATH, "r") as f:
            data = json.load(f)
    except:
        data = []

    data.append({
        "ticket": ticket,
        "solution": solution
    })

    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)