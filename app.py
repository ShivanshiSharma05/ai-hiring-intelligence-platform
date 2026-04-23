import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from question_generator import generate_questions
from score_calculator import calculate_score
from jd_matcher import match_resume_to_jd
from suggestions import get_suggestions

st.set_page_config(page_title="AI Hiring Platform", layout="wide")

st.title("🚀 AI-Powered Hiring Intelligence Platform")

uploaded_files = st.file_uploader("📄 Upload Multiple Resumes", type=["pdf"], accept_multiple_files=True)
jd_text = st.text_area("📄 Paste Job Description")

if uploaded_files:

    candidates = []

    for file in uploaded_files:

        text = extract_text_from_pdf(file)
        skills = extract_skills(text)

        score = calculate_score(skills, text)

        if jd_text:
            match_score, missing = match_resume_to_jd(text, jd_text)
        else:
            match_score, missing = 0, []

        candidates.append({
            "name": file.name,
            "score": score,
            "match": match_score,
            "skills": skills,
            "missing": missing,
            "questions": generate_questions(skills),
            "suggestions": get_suggestions(skills, text)
        })

    # Ranking
    candidates = sorted(candidates, key=lambda x: x["match"], reverse=True)

    st.header("🏆 Candidate Ranking")

    for i, c in enumerate(candidates):

        if i == 0:
            st.success(f"🥇 TOP CANDIDATE: {c['name']} ({c['match']}%)")

        else:
            st.info(f"{i+1}. {c['name']} ({c['match']}%)")

        st.write("💡 Skills:", ", ".join(c["skills"]))

        if c["missing"]:
            st.write("❌ Missing Skills:", ", ".join(c["missing"]))

        if c["suggestions"]:
            st.write("💡 Suggestions:")
            for s in c["suggestions"]:
                st.warning(s)

        st.write("🎯 Interview Questions:")
        for q in c["questions"]:
            st.write("-", q)

        st.divider()