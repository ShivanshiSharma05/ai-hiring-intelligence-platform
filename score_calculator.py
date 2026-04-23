def calculate_score(skills, text):

    score = 0

    # Skill weight
    score += min(len(skills) * 10, 40)

    # Resume length
    word_count = len(text.split())

    if word_count > 300:
        score += 20
    elif word_count > 150:
        score += 10

    # Keywords boost
    important = ["project", "experience", "internship"]
    for word in important:
        if word in text.lower():
            score += 10

    return min(score, 100)