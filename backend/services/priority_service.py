from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def detect_priority(ticket):

    t = ticket.lower()

    # -------- RULE-BASED LOGIC -------- #

    # HIGH
    if "server" in t or "database" in t:
        return "HIGH"

    if "cannot login" in t or "password" in t or "authentication" in t:
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

    # -------- LLM FALLBACK -------- #

    prompt = f"""
Determine priority for this IT ticket.

Rules:
LOW → single user issue
MEDIUM → affects multiple users
HIGH → system outage or critical issue

Ticket: {ticket}

Return only one word: LOW, MEDIUM, or HIGH.
"""

    try:
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}]
        )

        result = response.choices[0].message.content.strip().upper()

        if result in ["LOW", "MEDIUM", "HIGH"]:
            return result

    except Exception:
        pass

    # Final fallback (safety)
    return "LOW"