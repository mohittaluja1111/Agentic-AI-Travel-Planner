from openai import OpenAI
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get API key securely
api_key = os.getenv("OPENROUTER_API_KEY")

# OpenRouter client
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Test request
response = client.chat.completions.create(
    model="openai/gpt-3.5-turbo",
    messages=[
        {
            "role": "user",
            "content": "Hello, tell me about AI travel planners."
        }
    ]
)

# Print response
print(response.choices[0].message.content)