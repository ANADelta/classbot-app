# Placeholder for openai_handler.py
# openai_handler.py
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("OPENAI_API_KEY is not set in .env")

client = OpenAI(api_key=openai_api_key)

def query_openai(prompt, model="gpt-3.5-turbo", max_tokens=150):
    try:
        response = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=max_tokens,
            temperature=0.7
        )
        return response.choices[0].message.content.strip()
    except Exception as e:
        return f"⚠️ Error from OpenAI: {str(e)}"