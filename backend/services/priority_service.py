from groq import Groq
import os
load_dotenv()  # load .env variables

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def detect_priority(ticket):

    prompt = f"""
    You are an IT incident management AI.

    Determine the priority level of the following ticket.

    Ticket: {ticket}

    Respond with only one word:
    HIGH, MEDIUM, or LOW.

    Rules:
    - HIGH: system outage, server down, many users affected
    - MEDIUM: functionality issue affecting a user
    - LOW: minor inconvenience or request
    """

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )

    return response.choices[0].message.content.strip()