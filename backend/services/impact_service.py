from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def predict_impact(ticket):

    prompt = f"""
    You are an AI IT operations analyst.

    Based on the incident, predict:

    - Estimated number of employees affected
    - Estimated downtime
    - Business risk level (LOW, MEDIUM, HIGH)

    Ticket: {ticket}

    Respond in this format:

    Employees affected:
    Estimated downtime:
    Business risk:
    """

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )

    return response.choices[0].message.content.strip()