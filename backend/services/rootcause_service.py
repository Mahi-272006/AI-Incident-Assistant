from groq import Groq
import os

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_root_cause(ticket):

    prompt = f"""
    You are an expert IT operations engineer.

    Analyze the incident and infer the most likely root causes.

    Ticket:
    {ticket}

    Provide:
    - 3 to 5 possible root causes
    - estimated probability for each

    Format:

    Root Causes:
    1.
    2.
    3.

    Probabilities:
    """

    response = client.chat.completions.create(
        messages=[{"role": "user", "content": prompt}],
        model="llama-3.1-8b-instant"
    )

    return response.choices[0].message.content