import re

TECH_SKILLS = {
    "python","java","c++","sql","machine learning","deep learning",
    "nlp","tensorflow","pytorch","opencv","data science",
    "aws","docker","kubernetes","system design",
    "data structures","algorithms"
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    return text


def match_resume_to_jd(resume_text, jd_text):

    resume_text_clean = clean_text(resume_text)
    jd_text_clean = clean_text(jd_text)

    resume_words = set(resume_text_clean.split())

    # ✅ Only extract REAL TECH skills from JD
    jd_keywords = set()
    for skill in TECH_SKILLS:
        if skill in jd_text_clean:
            jd_keywords.add(skill)

    matched = resume_words.intersection(jd_keywords)
    missing = jd_keywords - resume_words

    score = int((len(matched) / len(jd_keywords)) * 100) if jd_keywords else 0

    return score, sorted(missing)