import pdfplumber
import re
import pandas as pd

def read_pdf(file):
    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text

    return text


def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z0-9 ]', ' ', text)
    return text


def load_skills():
    df = pd.read_csv("skills.csv")
    return df["Skill"].str.lower().tolist()


def extract_skills(text, skills):
    found = []

    for skill in skills:
        if skill.lower() in text.lower():
            found.append(skill)

    return list(set(found))
