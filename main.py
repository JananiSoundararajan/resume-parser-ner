from parser.pdfreader import extract_text_from_pdf
from parser.ner import extract_entities
from parser.skill_matcher import extract_skills
import json

def main():
    pdf_path = "sample_resumes/sample1.pdf"
    text = extract_text_from_pdf(pdf_path)
    
    entities = extract_entities(text)
    skills = extract_skills(text)

    resume_data = {
        "Name": entities.get("NAME"),
        "Degree": entities.get("DEGREE"),
        "Institutions": entities.get("ORG"),
        "Work Experience": entities.get("WORK_EXPERIENCE", []),
        "Skills": skills
    }

    with open("outputs/parsed_output.json", "w") as f:
        json.dump(resume_data, f, indent=4)

    print("Resume parsed. Check outputs/parsed_output.json")

if __name__ == "__main__":
    main()
