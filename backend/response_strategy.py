import os
import requests
from backend.memory_manager import save_message

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def generate_response_llm(user_message: str) -> str:
    if not GROQ_API_KEY:
        return "⚠️ GROQ_API_KEY not set."

    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama3-8b-8192",
        "messages": [
            {"role": "user", "content": user_message}
        ],
        "temperature": 0.7
    }

    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"]

    except Exception as e:
        print("Groq error:", e)
        reply = "I'm here with you. Tell me more."

    save_message("user", user_message)
    save_message("assistant", reply)

    return reply
