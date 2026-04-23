import random

def generate_questions(skills):

    if not skills:
        return ["Tell me about yourself."]

    templates = [
        "How have you applied {skill} in a real-world project?",
        "Explain a challenging problem you solved using {skill}.",
        "How would you design a scalable system using {skill}?",
        "What are best practices when working with {skill}?",
        "What are common pitfalls in {skill} and how do you avoid them?"
    ]

    questions = []
    selected_skills = skills[:5]

    for skill in selected_skills:
        q = random.choice(templates).format(skill=skill)
        questions.append(q)

    return questions