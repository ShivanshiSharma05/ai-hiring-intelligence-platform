import random

def generate_questions(skills):

    advanced_patterns = [
        "Explain a real-world project where you used {}.",
        "How would you optimize performance using {}?",
        "What are common challenges in {} and how do you solve them?",
        "How does {} integrate with other technologies?",
        "What are best practices when working with {}?",
        "Compare {} with alternative tools or frameworks.",
        "How would you design a system using {}?"
    ]

    questions = []

    for skill in skills:
        questions.append(random.choice(advanced_patterns).format(skill))

    random.shuffle(questions)
    return questions[:5]