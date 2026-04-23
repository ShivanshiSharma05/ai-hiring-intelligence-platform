import random

def generate_questions(skills):

    if not skills:
        return ["Tell me about yourself."]

    # 🔥 High-value skills only (avoid weak ones like 'c')
    priority_skills = [
        "python","machine learning","deep learning","nlp",
        "tensorflow","pytorch","opencv","sql","aws","docker",
        "data science","system design"
    ]

    # Filter important skills
    filtered_skills = [s for s in skills if s in priority_skills]

    # Fallback if no priority skills found
    selected_skills = filtered_skills[:5] if filtered_skills else skills[:5]

    templates = [
        "How would you apply {skill} in a real-world production system?",
        "Explain a project where {skill} improved system performance.",
        "What challenges have you faced while working with {skill}?",
        "How do you optimize solutions using {skill}?",
        "How does {skill} integrate with other technologies in a scalable system?"
    ]

    questions = []

    for skill in selected_skills:
        q = random.choice(templates).format(skill=skill)
        questions.append(q)

    return questions