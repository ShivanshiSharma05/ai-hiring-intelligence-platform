import re

TECH_SKILLS = {
    "python","java","c++","sql","machine learning","deep learning",
    "nlp","tensorflow","pytorch","opencv","data science",
    "aws","docker","kubernetes","system design","data structures","algorithms"
}

def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    return text

def match_resume_to_jd(resume_text, jd_text):

    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text)

    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())

    # Only keep TECH words from JD
    jd_keywords = {word for word in jd_words if word in TECH_SKILLS}

    matched = resume_words.intersection(jd_keywords)
    missing = jd_keywords - resume_words

    score = int((len(matched) / len(jd_keywords)) * 100) if jd_keywords else 0

    return score, sorted(missing)