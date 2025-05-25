import os
from dotenv import load_dotenv
from openai import OpenAI
import requests
import json

load_dotenv()

client = OpenAI(api_key = os.getenv("OPENAI_API_KEY"))

prompt = 'Un perro viendo el atardecer'
quality = 'standard'

response = client.images.generate(
    model = 'dall-e-3',
    prompt = prompt,
    quality = quality,
    n = 1
)

print(response.data[0].url)