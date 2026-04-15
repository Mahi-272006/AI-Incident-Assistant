import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))


def normalize_category(result):

    r = result.lower()

    if "vpn" in r or "wifi" in r or "network" in r:
        return "Network Issue"

    if "password" in r or "login" in r or "authentication" in r:
        return "Authentication Issue"

    if "outlook" in r or "email" in r:
        return "Email Issue"

    if "server" in r or "database" in r:
        return "Server Issue"

    if "printer" in r:
        return "Printer Issue"

    if "hardware" in r or "keyboard" in r or "mouse" in r or "battery" in r or "monitor" in r or "camera" in r:
        return "Hardware Issue"

    if "windows" in r or "os" in r or "update" in r:
        return "OS Issue"

    if "software" in r or "application" in r or "install" in r:
        return "Software Issue"

    return "General IT Issue"



def classify_ticket(ticket):

    prompt = f"""
Classify the IT incident ticket into one category.

Categories:
Network Issue
Hardware Issue
Software Issue
Server Issue
Authentication Issue
Email Issue
OS Issue
Printer Issue
General IT Issue

Ticket: {ticket}

Return only the category name.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )

    raw_result = response.choices[0].message.content.strip()

    return normalize_category(raw_result)