import plotly.express as px
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
  

    st.header("ATS Resume Analysis")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("ATS Score", f"{score}%")
    col2.metric("Matched Skills", len(matched_skills))
    col3.metric("Missing Skills", len(missing_skills))
    if score >= 85:
      rating = "Excellent ⭐⭐⭐⭐⭐"
    elif score >= 70:
      rating = "Good ⭐⭐⭐⭐"
    elif score >= 50:
      rating = "Average ⭐⭐⭐"
    else:
      rating = "Needs Improvement ⭐⭐"

    col4.metric("Rating", rating)
    st.progress(score/100)
    st.write(f"Overall ATS Score : {score}%")
    st.subheader("Resume Strength")

    if score >= 90:
      st.success("★★★★★ Excellent Resume")

    elif score >= 75:
      st.success("★★★★☆ Very Good Resume")

    elif score >= 60:
      st.warning("★★★☆☆ Good Resume")

    else:
      st.error("★★☆☆☆ Needs Improvement")

    fig = px.pie(

    values=[len(matched_skills), len(missing_skills)],

    names=["Matched Skills", "Missing Skills"],

    title="Skill Coverage")

    st.plotly_chart(fig, use_container_width=True)

    fig = px.bar(

    x=["Matched", "Missing"],

    y=[len(matched_skills), len(missing_skills)],

    title="Skill Comparison")

    st.plotly_chart(fig, use_container_width=True)

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

    st.subheader("Recommendations")

    if len(missing_skills)==0:

      st.success("Excellent! Your resume aligns well with the job description.")

    else:

      st.info("Consider adding these skills if you have relevant experience:")

      for skill in missing_skills:

        st.write(f"✔ {skill.title()}")
    st.markdown("---")

    st.write("### Additional Tips")

    st.write("• Include measurable project outcomes.")

    st.write("• Add GitHub project links.")

    st.write("• Mention certifications.")

    st.write("• Highlight internship achievements.")

    st.write("• Quantify your accomplishments wherever possible.")
