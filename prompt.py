def prompt_extract_skills(text):
    return f"""
You are a Text cleaner.
Rules:
- Extract every technical skill, tool, framework, and technology mentioned
- Do not summarize or group skills together
- Each skill should be a separate item in the list
- return output in Json format only.
- No Explanation.
- Extract all the skills from the text.
- Return in Json Format only
- {{"Skills": ["skill_1","skill_2","skill_3"]}}
- Extract all the skills and append in the list above.
- no irrelevance text except the job related text or skills only 
Text:
{text}
"""

def prompt_compare(resume_skills, jd_skills, mode):
    return f"""
You are an expert technical recruiter and career coach.

You are given two lists of skills:
1. Candidate Skills extracted from their resume
2. Required Skills extracted from a Job Description

Candidate Skills:
{resume_skills}

Job Required Skills:
{jd_skills}

Mode: {mode}

Rules:
- Extract ALL skills mentioned anywhere in the text including in project descriptions, work experience, and profile summary
- Do not miss any skill even if mentioned only once
- Include synonyms e.g. "Hugging Face Transformers" and "HuggingFace" are the same skill
- Do NOT add any text, notes or explanations after the closing }}
- Do NOT add comments inside the JSON using // or #
- If semantic_matches is empty, just return {{}}
- Compare both skill lists carefully
- matched_skills: skills that appear in both lists (including semantic matches)
- missing_skills: skills in JD that candidate completely lacks
- semantic_matches: skills that mean the same thing but are worded differently e.g. "RAG pipelines" matches "GenAI pipelines expertise"
- score: calculate as (number of matched_skills / total JD required skills) * 100, round to nearest 10
- if mode is "hr": verdict must be one of "Shortlist" / "Reject" / "Maybe", recommendations must be interview questions to probe weak areas
- if mode is "user": verdict must be one of "Strong Fit" / "Partial Fit" / "Weak Fit", recommendations must be specific things to learn or add to resume
- reasoning: 2-3 lines explaining the score and verdict
- Respond ONLY in valid JSON. No text outside the JSON block.

Return ONLY this JSON:
{{
    "matched_skills": [],
    "missing_skills": [],
    "semantic_matches": {{}},
    "score": 0,
    "verdict": "",
    "reasoning": "",
    "recommendations": []
}}
"""

chat_3 = '''


'''
