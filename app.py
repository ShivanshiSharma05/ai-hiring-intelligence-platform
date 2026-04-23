import streamlit as st
from resume_parser import extract_text_from_pdf
from skill_extractor import extract_skills
from question_generator import generate_questions
from score_calculator import calculate_score
from jd_matcher import match_resume_to_jd
from suggestions import get_suggestions

# -------------------------------
# PAGE CONFIG
# -------------------------------
st.set_page_config(page_title="AI Hiring Platform", layout="wide")

st.title("🚀 AI-Powered Hiring Intelligence Platform")

# -------------------------------
# INPUTS (WITH UNIQUE KEYS)
# -------------------------------
uploaded_files = st.file_uploader(
    "📄 Upload Multiple Resumes",
    type=["pdf"],
    accept_multiple_files=True,
    key="resume_uploader"
)

jd_text = st.text_area(
    "📄 Paste Job Description",
    key="jd_input"
)

# -------------------------------
# MAIN LOGIC
# -------------------------------
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

    # -------------------------------
    # SMART FINAL SCORE
    # -------------------------------
    for c in candidates:
        c["final_score"] = int(0.7 * c["match"] + 0.3 * c["score"])

    # -------------------------------
    # SORT BY FINAL SCORE
    # -------------------------------
    candidates = sorted(candidates, key=lambda x: x["final_score"], reverse=True)

    st.header("🏆 Candidate Ranking")

    # -------------------------------
    # DISPLAY RESULTS
    # -------------------------------
    for i, c in enumerate(candidates):

        # 🥇 TOP CANDIDATE
        if i == 0:
            st.success(f"🥇 TOP CANDIDATE: {c['name']} (Final Score: {c['final_score']}%)")
        else:
            st.info(f"{i+1}. {c['name']} (Final Score: {c['final_score']}%)")

        # 💡 Skills
        st.write("💡 Skills:", ", ".join(c["skills"]))

        # -------------------------------
        # 🧠 WHY ANALYSIS
        # -------------------------------
        strong = c["skills"][:3]
        missing = c["missing"][:3]

        st.write("🧠 Analysis:")

        if strong:
            st.success("✔ Strong in: " + ", ".join(strong))

        if missing:
            st.error("❌ Needs improvement in: " + ", ".join(missing))

        # -------------------------------
        # 🏆 TOP CANDIDATE INSIGHT
        # -------------------------------
        if i == 0:
            st.subheader("🏆 Why This Candidate Stands Out")

            reasons = []

            if len(c["skills"]) > 5:
                reasons.append("Strong technical skillset")

            if c["match"] > 70:
                reasons.append("High job-role alignment")

            if c["score"] > 70:
                reasons.append("Well-structured resume")

            for r in reasons:
                st.write("✔", r)

        # -------------------------------
        # 💡 SUGGESTIONS
        # -------------------------------
        if c["suggestions"]:
            st.write("💡 Suggestions:")
            for s in c["suggestions"]:
                st.warning(s)

        # -------------------------------
        # 🎯 QUESTIONS
        # -------------------------------
        st.write("🎯 Interview Questions:")
        for q in c["questions"]:
            st.write("-", q)

        st.divider()