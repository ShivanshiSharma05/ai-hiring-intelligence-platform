def get_suggestions(skills, text):

    suggestions = []
    text = text.lower()

    if "internship" not in text:
        suggestions.append("Add internship experience")

    if "project" not in text:
        suggestions.append("Add more projects")

    if len(skills) < 5:
        suggestions.append("Add more technical skills")

    return suggestions