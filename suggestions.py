def get_suggestions(skills, text):

    suggestions = []

    if len(skills) < 5:
        suggestions.append("Add more technical skills")

    if "project" not in text.lower():
        suggestions.append("Include project experience")

    if "internship" not in text.lower():
        suggestions.append("Add internship or practical experience")

    if len(text.split()) < 200:
        suggestions.append("Increase resume content for better impact")

    return suggestions