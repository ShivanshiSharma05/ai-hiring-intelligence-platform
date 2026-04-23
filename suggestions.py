def get_suggestions(skills, text):

    suggestions = []

    text_lower = text.lower()

    # 🔹 Basic improvements
    if len(skills) < 5:
        suggestions.append("Add more technical skills relevant to the role")

    if "project" not in text_lower:
        suggestions.append("Include project experience to showcase practical skills")

    if "internship" not in text_lower:
        suggestions.append("Add internship or real-world experience")

    if len(text.split()) < 200:
        suggestions.append("Increase resume content with more detailed descriptions")

    # 🔥 FAANG-level improvements
    if "aws" not in skills:
        suggestions.append("Consider adding cloud experience (AWS/GCP)")

    if "docker" not in skills:
        suggestions.append("Add deployment or containerization experience (Docker/Kubernetes)")

    if "machine learning" in skills and "project" in text_lower:
        suggestions.append("Include measurable results in ML projects (accuracy, performance improvement)")

    if "data science" in skills:
        suggestions.append("Highlight data handling, preprocessing, and visualization experience")

    return suggestions