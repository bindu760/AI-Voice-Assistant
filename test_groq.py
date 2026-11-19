
import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables from .env
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")
model = os.getenv("GROQ_MODEL")

if not api_key:
    raise ValueError("GROQ_API_KEY is missing in .env file")

# Create Groq client
client = Groq(api_key=api_key)

# Send a test message
response = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "Hello! Introduce yourself in one sentence."
        }
    ]
)

# Print AI response
print("Groq AI Response:")
print(response.choices[0].message.content)
