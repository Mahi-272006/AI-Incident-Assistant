from groq import Groq
import os

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def generate_solution(ticket, context):

    
    prompt = f"""
You are an IT support expert.

Incident:
{ticket}

Relevant knowledge base solution:
{context}

Generate clear troubleshooting steps ONLY related to the incident.

Rules:
- Do not mention unrelated technologies.
- Use numbered steps.
- Be concise and practical.
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