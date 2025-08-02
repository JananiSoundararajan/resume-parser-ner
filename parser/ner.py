import spacy
import re

nlp = spacy.load("en_core_web_sm")

def clean_name(text):
    doc = nlp(text[:300])  # Only check top portion
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text.strip()
    # fallback
    match = re.search(r"Name[:\- ]*([A-Za-z ]+)", text)
    return match.group(1).strip() if match else None

def extract_institutions(text):
    institutions = []
    inst_keywords = ["University", "College", "Institute", "School"]
    lines = text.split('\n')
    for line in lines:
        if any(word in line for word in inst_keywords):
            institutions.append(line.strip())
    return list(set(institutions))

def extract_degrees(text):
    degrees = []
    degree_keywords = ["B.Tech", "M.Tech", "B.Sc", "M.Sc", "B.E", "M.E", "Bachelor", "Master"]
    for degree in degree_keywords:
        if degree.lower() in text.lower():
            degrees.append(degree)
    return list(set(degrees))

def extract_work_experience(text):
    date_pattern = re.compile(r"(20\d{2})")
    years = list(set(re.findall(date_pattern, text)))
    return sorted(years)

def extract_entities(text):
    return {
        "NAME": clean_name(text),
        "ORG": extract_institutions(text),
        "DEGREE": extract_degrees(text),
        "WORK_EXPERIENCE": extract_work_experience(text)
    }
