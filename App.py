import streamlit as st
from Parser import extract_resume_text, extract_jd_text
from prompt import prompt_extract_skills, prompt_compare
from llm_router2 import call_llm
import json

st.title("Resume Screener")

mode = st.selectbox("Select Mode", ["user", "hr"])

resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
jd_image = st.file_uploader("Upload Job Description (Image)", type=["png", "jpg", "jpeg"])

if st.button("Analyze"):
    if resume_file and jd_image:
        with st.spinner("Analyzing..."):
            # save uploaded files temporarily
            with open("temp_resume.pdf", "wb") as f:
                f.write(resume_file.read())
            with open("temp_jd.jpg", "wb") as f:
                f.write(jd_image.read())

            # extract text
            resume_text = extract_resume_text("temp_resume.pdf")
            jd_text = extract_jd_text("temp_jd.jpg")

            # extract skills from both
            resume_skills = call_llm(prompt_extract_skills(resume_text))
            jd_skills = call_llm(prompt_extract_skills(jd_text))

            # compare
            final_result = call_llm(prompt_compare(resume_skills, jd_skills, mode))
            
            print("=== RAW FINAL RESULT ===")

            print(final_result)
            # result = json.loads(final_result)
            try:
                result = json.loads(final_result)
            except json.JSONDecodeError:
                st.error("LLM returned malformed JSON. Try again.")
                st.code(final_result)
                st.stop()
            

            # display
            st.subheader("Result")
            st.metric("Score", f"{result['score']}/100")
            st.success(f"Verdict: {result['verdict']}")
            st.write(f"**Reasoning:** {result['reasoning']}")

            st.subheader("Matched Skills")
            for skill in result['matched_skills']:
                st.success(skill)

            st.subheader("Missing Skills")
            for skill in result['missing_skills']:
                st.error(skill)

            st.subheader("Recommendations")
            for rec in result['recommendations']:
                st.info(rec)    # display result
    else:
        st.warning("Please upload both files")
