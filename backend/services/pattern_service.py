import json
from collections import Counter

FILE_PATH = "knowledge/incidents.json"

def detect_patterns(ticket_category=None):
    try:
        with open(FILE_PATH, "r") as f:
            incidents = json.load(f)
    except:
        return None

    # filter incidents by category if given
    if ticket_category:
        incidents = [i for i in incidents if i.get("category") == ticket_category]

    tickets = [i["ticket"].lower() for i in incidents]
    counter = Counter()

    for t in tickets:
        if "vpn" in t:
            counter["vpn issue"] += 1
        elif "password" in t:
            counter["password issue"] += 1
        elif "server" in t:
            counter["server issue"] += 1
        elif "laptop" in t or "hang" in t or "freeze" in t:
            counter["laptop issue"] += 1
        else:
            counter[t] += 1

    common = counter.most_common(1)

    if not common:
        return None

    issue, count = common[0]

    if count >= 3:
        return f"⚠ Possible recurring issue detected: '{issue}' occurred {count} times."

    return None