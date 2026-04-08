from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_solution(ticket, context):

    
    prompt = f"""
Ticket: {ticket}

If the provided knowledge base information is relevant, use it.
If it is not relevant, ignore it and generate your own troubleshooting steps.

Knowledge base information:
{context}

Provide clear troubleshooting steps.
"""

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama-3.1-8b-instant",
    )

    return chat_completion.choices[0].message.content