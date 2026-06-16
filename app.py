import sys
sys.path.append('/content/my_notebooks')

import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils import *

st.set_page_config(page_title="Resume Analyzer", layout="wide")

st.title("AI Resume Analyzer")

resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

jd = st.text_area("Paste Job Description")

if resume and jd:

    resume_text = read_pdf(resume)

    resume_text = clean_text(resume_text)
    jd = clean_text(jd)

    skills = load_skills()

    resume_skills = extract_skills(resume_text, skills)
    jd_skills = extract_skills(jd, skills)

    missing_skills = list(set(jd_skills) - set(resume_skills))

    matched_skills = list(set(jd_skills) & set(resume_skills))

    if len(jd_skills) > 0:
      score = round((len(matched_skills) / len(jd_skills)) * 100,2)
    else:
      score=0
  

    st.header("Resume Match Score")

    st.progress(int(score))

    st.write(f"### {score}% Match")

    st.divider()

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Matching Skills")

        if matched_skills:
            for skill in matched_skills:
                st.success(skill.title())

    with col2:

        st.subheader("Missing Skills")

        if missing_skills:
            for skill in missing_skills:
                st.error(skill.title())

    st.divider()

    st.subheader("Resume Skills")

    st.write(", ".join(resume_skills))

    st.subheader("JD Skills")

    st.write(", ".join(jd_skills))

    st.divider()

    st.subheader("Suggestions")

    if len(missing_skills)==0:
        st.success("Excellent Resume!")

    else:
        st.write("Try adding these skills if applicable:")

        for skill in missing_skills:
            st.write("- ", skill.title())
