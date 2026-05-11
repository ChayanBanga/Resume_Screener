import requests
import os

try:
    import streamlit as st
    GEMINI_API_KEY = st.secrets.get("GEMINI_API_KEY", "")
    GROQ_API_KEY = st.secrets.get("GROQ_API_KEY", "")
except:
    from dotenv import load_dotenv
    load_dotenv()
    GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
    GROQ_API_KEY = os.getenv("GROQ_API_KEY", "")

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
    if "error" in result:
        raise Exception(f"Gemini error: {result['error']['message']}")
    text = result["candidates"][0]["content"]["parts"][0]["text"]
    text = text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return text

def call_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "llama3-8b-8192",
        "messages": [{"role": "user", "content": prompt}]
    }
    response = requests.post(url, headers=headers, json=payload)
    result = response.json()
    text = result["choices"][0]["message"]["content"]
    text = text.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return text

def call_llm(prompt):
    try:
        return call_ollama(prompt)
    except:
        try:
            return call_gemini(prompt)
        except:
            return call_groq(prompt)
