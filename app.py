import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from jd_matcher import match_resume_to_jd
from question_generator import generate_questions
from suggestions import get_suggestions

st.set_page_config(page_title="AI Hiring Platform", layout="wide")

st.title("🚀 AI-Powered Hiring Intelligence Platform")

uploaded_files = st.file_uploader(
    "📄 Upload Multiple Resumes", type=["pdf"], accept_multiple_files=True
)

jd_text = st.text_area("📄 Paste Job Description")

if uploaded_files and jd_text:

    results = []

    for file in uploaded_files:
        text = extract_text_from_pdf(file)
        skills = extract_skills(text)

        score, missing = match_resume_to_jd(text, jd_text)

        results.append({
            "name": file.name,
            "score": score,
            "skills": skills,
            "missing": missing,
            "text": text
        })

    # 🔥 SORT (RANKING)
    results = sorted(results, key=lambda x: x["score"], reverse=True)

    st.subheader("🏆 Candidate Ranking")

    for i, res in enumerate(results, 1):
        st.markdown(f"### {i}. {res['name']} - {res['score']}%")

        col1, col2 = st.columns(2)

        with col1:
            st.write("💡 Skills:")
            for skill in res["skills"]:
                st.success(skill)

        with col2:
            if res["missing"]:
                st.write("❌ Missing:")
                for m in res["missing"]:
                    st.error(m)

        # Suggestions
        suggestions = get_suggestions(res["skills"], res["text"])
        if suggestions:
            st.write("💡 Suggestions:")
            for s in suggestions:
                st.warning(s)

        # Questions
        st.write("🎯 Interview Questions:")
        questions = generate_questions(res["skills"])
        for q in questions:
            st.info(q)

        st.markdown("---")