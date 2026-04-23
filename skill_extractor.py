import re

# -------------------------------
# Skill Database
# -------------------------------
SKILL_DB = [
    "python", "java", "c++", "c", "javascript",
    "machine learning", "deep learning", "nlp", "data science",
    "computer vision", "tensorflow", "pytorch",
    "opencv", "pandas", "numpy",
    "sql", "mysql", "mongodb",
    "flask", "django", "fastapi",
    "aws", "docker", "kubernetes",
    "data structures", "algorithms", "system design"
]

# -------------------------------
# Clean text
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

    found_skills = set()

    for skill in SKILL_DB:
        if skill in text:
            found_skills.add(skill)

    return sorted(found_skills)