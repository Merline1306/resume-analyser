import pdfplumber
import re
import pandas as pd


def read_pdf(file):
    text = ""

    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()

            if page_text:
                text += page_text + " "

    return text


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^\w\s]", " ", text)
    text = re.sub(r"\s+", " ", text)

    return text.strip()


def load_skills():
    df = pd.read_csv("skills.csv")

    skills = (
        df["Skill"]
        .dropna()
        .astype(str)
        .str.lower()
        .unique()
        .tolist()
    )

    return skills


def extract_skills(text, skills):

    text = clean_text(text)

    found = set()

    for skill in skills:

        skill = skill.lower().strip()

        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, text):
            found.add(skill)

    return sorted(list(found))
