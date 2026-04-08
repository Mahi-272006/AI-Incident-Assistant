from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def assign_team(ticket, category):

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

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )

    return response.choices[0].message.content.strip()