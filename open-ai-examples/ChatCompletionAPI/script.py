import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model = "gpt-4",
    messages = [
        {
            "role": "system",
            "content": "Te llamas ChatVision, presentate como tal"
        },
        {
            "role": "user",
            "content": "Hola, como estas?"
        }
    ],
    max_tokens=100,
    temperature=0.7
)

print(response.choices[0].message.content)