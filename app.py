import streamlit as st
from parser.pdfreader import extract_text_from_pdf
from parser.ner import extract_entities
from parser.skill_matcher import extract_skills

st.title("Resume Parser using NLP")

uploaded_file = st.file_uploader("Upload your Resume", type=["pdf"])

if uploaded_file:
    text = extract_text_from_pdf(uploaded_file)
    entities = extract_entities(text)
    skills = extract_skills(text)

    st.json({
        "Name": entities.get("NAME"),
        "Degree": entities.get("DEGREE"),
        "Institutions": entities.get("ORG"),
        "Work Experience": entities.get("WORK_EXPERIENCE", []),
        "Skills": skills
    })
