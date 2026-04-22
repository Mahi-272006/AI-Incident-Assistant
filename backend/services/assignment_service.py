from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def assign_team(ticket, category):

    # -------- RULE-BASED MAPPING -------- #

    mapping = {
        "Network Issue": "Network Operations",
        "Authentication Issue": "IT Security",
        "Server Issue": "Server Operations",
        "Hardware Issue": "IT Support",
        "Printer Issue": "IT Support",
        "Email Issue": "IT Support",
        "OS Issue": "IT Support",
        "Software Issue": "IT Support",
        "General IT Issue": "IT Support"
    }

    if category in mapping:
        return mapping[category]

    # -------- LLM FALLBACK -------- #

    prompt = f"""
You are an IT incident routing system.

Based on the ticket and category, assign the most appropriate team.

Ticket: {ticket}
Category: {category}

Choose one of these teams:
- Network Operations
- IT Support
- Security Team
- Infrastructure Team
- Application Support

Respond with only the team name.
"""

    try:
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant"
        )

        return response.choices[0].message.content.strip()

    except Exception:
        return "IT Support"