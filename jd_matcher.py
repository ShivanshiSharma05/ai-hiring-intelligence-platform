import re
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('all-MiniLM-L6-v2')

TECH_KEYWORDS = {
    "python","c++","sql","machine","learning","deep","nlp",
    "tensorflow","opencv","data","science","aws","docker",
    "system","design","pytorch"
}

def extract_keywords(text):
    words = re.findall(r'\b[a-zA-Z]+\b', text.lower())
    return set([w for w in words if w in TECH_KEYWORDS])


def match_resume_to_jd(resume_text, jd_text):

    # 🔹 Extract important keywords only
    resume_keys = extract_keywords(resume_text)
    jd_keys = extract_keywords(jd_text)

    # 🔹 Skill match score
    common = resume_keys.intersection(jd_keys)
    skill_score = len(common) / (len(jd_keys) + 1)

    # 🔹 Semantic score (reduced weight)
    emb1 = model.encode(" ".join(resume_keys), convert_to_tensor=True)
    emb2 = model.encode(" ".join(jd_keys), convert_to_tensor=True)

    semantic_score = util.cos_sim(emb1, emb2).item()

    # 🔥 FINAL SCORE (balanced)
    final_score = int((0.7 * skill_score + 0.3 * semantic_score) * 100)

    # 🔹 Missing (only meaningful)
    missing = list(jd_keys - resume_keys)

    return final_score, missing[:5]