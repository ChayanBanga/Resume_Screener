import requests

def call_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    payload = {
        "model": "phi3.5",
        "prompt": prompt,
        "stream": False
    }
    response = requests.post(url, json=payload) 
    result =  response.json()["response"]
    result = result.strip().removeprefix("```json").removeprefix("```").removesuffix("```").strip()
    return result

from Parser import extract_resume_text, extract_jd_text
from prompt import prompt_extract_skills, prompt_compare

if __name__ == "__main__":
    # Step 1 - extract skills from resume
    resume_text = extract_resume_text(r"C:\Users\asus\Downloads\Chayan_Banga_Resume (1).pdf")
    resume_prompt = prompt_extract_skills(resume_text)
    resume_skills = call_ollama(resume_prompt)
    print("=== RESUME SKILLS ===")
    print(resume_skills)

    # Step 2 - extract skills from JD image
    jd_text = extract_jd_text(r"C:\Users\asus\Downloads\WhatsApp Image 2026-05-10 at 12.42.44 PM.jpeg")
    jd_prompt = prompt_extract_skills(jd_text)
    jd_skills = call_ollama(jd_prompt)
    print("=== JD SKILLS ===")
    print(jd_skills)

    # Step 3 - compare
    compare_prompt = prompt_compare(resume_skills, jd_skills, mode="user")
    result = call_ollama(compare_prompt)
    print("=== FINAL RESULT ===")
    print(result)