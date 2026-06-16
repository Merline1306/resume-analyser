# AI Resume Analyzer

A Streamlit-based AI Resume Analyzer that compares a candidate's resume with a job description and calculates an ATS (Applicant Tracking System) compatibility score. The application extracts technical skills, identifies matched and missing skills, and provides recommendations to improve resume quality.

---

## Live Demo

https://resume-analyser-7r6lappni6wjruvavtnyxrl.streamlit.app/

---



## Features

- Upload Resume (PDF)
- Paste Job Description
- Automatic Resume Parsing
- Technical Skill Extraction
- ATS Score Calculation
- Matching Skills Detection
- Missing Skills Identification
- Resume Strength Analysis
- Interactive Pie Chart
- Interactive Bar Chart
- Resume Recommendations
- User-Friendly Streamlit Interface

---

## Technologies Used

- Python
- Streamlit
- Pandas
- PDFPlumber
- Plotly
- Regular Expressions (Regex)
- Scikit-learn
- spaCy
- Sentence Transformers

---

## Project Structure

```
resume-analyser/
│
├── app.py
├── utils.py
├── skills.csv
├── skill_synonyms.json
├── requirements.txt
├── README.md
│
├── assets/
│   ├── home.png
│   ├── analysis.png
│   ├── charts.png
│   └── recommendations.png
│
└── sample_files/
    ├── sample_resume.pdf
    └── sample_job_description.txt
```

---

## Installation

### Clone the repository

```bash
git clone https://github.com/Merline1306/resume-analyser.git
```

### Navigate to the project folder

```bash
cd resume-analyser
```

### Install the required packages

```bash
pip install -r requirements.txt
```

### Run the application

```bash
streamlit run app.py
```

---

## How It Works

1. Upload a resume in PDF format.
2. Paste the desired job description.
3. The application extracts text from both inputs.
4. Skills are extracted using a predefined skills dataset.
5. Matching and missing skills are identified.
6. ATS compatibility score is calculated.
7. Results are displayed using interactive charts and recommendations.

---

## ATS Score Formula

```
ATS Score = (Matched Skills / Job Description Skills) × 100
```

---

## Application Output

The application provides:

- ATS Score
- Resume Strength
- Matching Skills
- Missing Skills
- Resume Skills
- Job Description Skills
- Skill Coverage Pie Chart
- Skill Comparison Bar Chart
- Personalized Recommendations


```
Job Title: Machine Learning Intern

Required Skills

Python
Machine Learning
Scikit-learn
Pandas
NumPy
Statistics
EDA
Data Preprocessing
Feature Engineering
Model Evaluation
Decision Tree
Random Forest
SVM
Logistic Regression
Streamlit
GitHub
```

---

## Future Enhancements

- Semantic Skill Matching using NLP
- AI-based Resume Feedback
- Resume Ranking
- PDF Report Generation
- Resume Role Recommendation
- Recruiter Dashboard
- Database Integration
- Multi-Resume Comparison

---

## Requirements

```
streamlit
pdfplumber
python-docx
spacy
sentence-transformers
scikit-learn
pandas
plotly
```
