from groq import Groq
from dotenv import load_dotenv
import os
load_dotenv()  # load .env variables

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def detect_priority(ticket):

    t = ticket.lower()

    # HIGH
    if "server" in t or "database" in t:
        return "HIGH"

    if "cannot login" in t or "password" in t:
        return "HIGH"

    if "authentication" in t:
        return "HIGH"

    if "cannot send email" in t:
        return "HIGH"

    # MEDIUM
    if "vpn" in t or "wifi" in t or "network" in t:
        return "MEDIUM"

    if "slow" in t or "install" in t:
        return "MEDIUM"

    if "battery" in t or "overheating" in t:
        return "MEDIUM"

    # LOW
    if "printer" in t:
        return "LOW"

    if "mouse" in t or "keyboard" in t:
        return "LOW"

    if "monitor" in t or "camera" in t:
        return "LOW"

    return "LOW"

    # LLM fallback
    prompt = f"""
Determine priority for this IT ticket.

LOW → single user
MEDIUM → multiple users
HIGH → system outage

Ticket: {ticket}

Return only: LOW, MEDIUM, HIGH
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()