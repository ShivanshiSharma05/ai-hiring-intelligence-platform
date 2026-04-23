import re

# -------------------------------
# Clean Text
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    return text


# -------------------------------
# Match Resume to JD
# -------------------------------
def match_resume_to_jd(resume_text, jd_text):

    resume_text = clean_text(resume_text)
    jd_text = clean_text(jd_text)

    resume_words = set(resume_text.split())
    jd_words = set(jd_text.split())

    # Remove useless words
    stopwords = {
        "and", "or", "the", "is", "are", "a", "an", "to", "for",
        "with", "of", "in", "on", "we", "you", "will", "be"
    }

    jd_keywords = jd_words - stopwords

    matched = resume_words.intersection(jd_keywords)
    missing = jd_keywords - resume_words

    if len(jd_keywords) == 0:
        score = 0
    else:
        score = int((len(matched) / len(jd_keywords)) * 100)

    return score, sorted(missing)