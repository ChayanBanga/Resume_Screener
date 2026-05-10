import requests
from dotenv import load_dotenv
import os

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def call_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "phi3.5",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload)
    result = response.json()["response"]
    result = result.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return result

def call_gemini(prompt):
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"
    payload = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    response = requests.post(url, json=payload)
    result = response.json()
    text = result["candidates"][0]["content"]["parts"][0]["text"]
    text = text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return text

def call_llm(prompt):
    try:
        return call_ollama(prompt)
    except:
        return call_gemini(prompt)