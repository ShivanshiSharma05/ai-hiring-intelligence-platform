import random

def generate_questions(skills):

    if not skills:
        return ["Tell me about yourself."]

    templates = [
        "How would you apply {skill} in a real-world production system?",
        "Explain a project where {skill} improved system performance.",
        "What challenges have you faced while working with {skill}?",
        "How do you optimize solutions using {skill}?",
        "How does {skill} integrate with other technologies in a scalable system?"
    ]

    questions = []
    selected_skills = skills[:5]

    for skill in selected_skills:
        q = random.choice(templates).format(skill=skill)
        questions.append(q)

    return questions