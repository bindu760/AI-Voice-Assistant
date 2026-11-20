
import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

MODEL = "openai/gpt-oss-120b"


def get_ai_response(user_text):

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": "You are a friendly voice assistant. Give clear, helpful and concise answers."
            },
            {
                "role": "user",
                "content": user_text
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content
