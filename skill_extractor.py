import re
import spacy
import subprocess

# -------------------------------
# Load SpaCy model (works locally + cloud)
# -------------------------------
try:
    nlp = spacy.load("en_core_web_sm")
except:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")


# -------------------------------
# Skill Database 
# -------------------------------
SKILL_DB = [
    # Programming
    "python", "java", "c++", "c", "javascript", "typescript", "go", "rust",

    # Data / ML / AI
    "machine learning", "deep learning", "nlp", "data science",
    "computer vision", "tensorflow", "pytorch", "scikit-learn",

    # Tools / Tech
    "opencv", "pandas", "numpy", "matplotlib", "seaborn",

    # Backend / Dev
    "flask", "django", "fastapi", "nodejs", "react",

    # Database
    "sql", "mysql", "postgresql", "mongodb",

    # Cloud / DevOps
    "aws", "docker", "kubernetes", "gcp", "azure",

    # Concepts
    "data structures", "algorithms", "system design"
]


# -------------------------------
# Clean Text
# -------------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9+# ]', ' ', text)
    return text


# -------------------------------
# Extract Skills
# -------------------------------
def extract_skills(text):
    text = clean_text(text)
    doc = nlp(text)

    found_skills = set()

    # 1️⃣ Direct match from database
    for skill in SKILL_DB:
        if skill in text:
            found_skills.add(skill)

    # 2️⃣ Noun phrase detection (extra intelligence)
    for chunk in doc.noun_chunks:
        chunk_text = chunk.text.strip().lower()
        if chunk_text in SKILL_DB:
            found_skills.add(chunk_text)

    # 3️⃣ Token-level matching (fallback)
    for token in doc:
        token_text = token.text.lower()
        if token_text in SKILL_DB:
            found_skills.add(token_text)

    return sorted(found_skills)