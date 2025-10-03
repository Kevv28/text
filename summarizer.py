import os
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
GROQ_API_KEY =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
def summarize_text(text: str) -> str:
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": "llama-3.1-8b-instant",  # Lightweight, fast model
        "messages": [
            {"role": "system", "content": "You are a text summarizer that summarizes content in 3 clear sentences."},
            {"role": "user", "content": text}
        ],
        "temperature": 0.5,
        "max_tokens": 200
    }
    
    response = requests.post(url, headers=headers, json=data)
    result = response.json()
    
    try:
        return result["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {str(e)}\nResponse: {result}"
