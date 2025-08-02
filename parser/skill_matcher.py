SKILL_SET = [
    "Python", "Java", "Machine Learning", "Deep Learning", "NLP", "SQL",
    "PyTorch", "TensorFlow", "Keras", "Git", "Docker", "Pandas", "NumPy",
    "HTML", "CSS", "JavaScript", "Data Analytics"
]

def extract_skills(text):
    skills = []
    for skill in SKILL_SET:
        if skill.lower() in text.lower():
            skills.append(skill)
    return sorted(list(set(skills)))
