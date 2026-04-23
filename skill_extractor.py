import spacy

nlp = spacy.load("en_core_web_sm")

SKILLS = [
    "python", "c++", "machine learning", "deep learning",
    "nlp", "sql", "tensorflow", "opencv", "data science"
]

def extract_skills(text):
    text = text.lower()
    return [skill for skill in SKILLS if skill in text]