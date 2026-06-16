# AI Resume Analyzer using Streamlit

## 📌 Project Overview

The **AI Resume Analyzer** is a web application built using **Python** and **Streamlit** that compares a student's resume with a specific Job Description (JD).

The application analyzes both documents, calculates a similarity score, identifies matching and missing skills, and provides suggestions to improve the resume for better ATS (Applicant Tracking System) compatibility.

---

## 🎯 Problem Statement

**Build a tool that compares a student resume against a specific job description and highlights missing keywords or skills.**

---

## 🚀 Features

- Upload Resume in PDF format
- Paste any Job Description
- Extract skills from Resume
- Extract skills from Job Description
- Calculate Resume Match Score
- Highlight Matching Skills
- Highlight Missing Skills
- Suggest Improvements
- Simple and Interactive Streamlit Interface

---

## 🛠 Technologies Used

- Python 3.x
- Streamlit
- Pandas
- Scikit-learn
- pdfplumber
- spaCy
- NLTK

---

## 📁 Project Structure

```
Resume_Analyzer/
│
├── app.py
├── utils.py
├── skills.csv
├── requirements.txt
├── README.md
├── sample_resume.pdf
└── sample_jd.txt
```

---

## 📦 Installation

### Step 1: Clone or Download the Project

```bash
git clone <repository_link>
```

or download the ZIP file.

---

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 3: Install spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

---

## ▶️ Run the Application

Open a terminal inside the project folder and run:

```bash
streamlit run app.py
```

The application will automatically open in your browser.

If it does not, open:

```
http://localhost:8501
```

---

## 📄 Input

### Resume

- Upload Resume as PDF

### Job Description

- Paste the Job Description into the text box.

---

## 📊 Output

The application provides:

- Resume Match Score (%)
- Matching Skills
- Missing Skills
- Resume Skills
- Job Description Skills
- Suggestions for Resume Improvement

---

## 📚 Dataset

The project uses a custom **skills.csv** file containing commonly used technical skills.

Example:

| Skill |
|-------|
| Python |
| SQL |
| Machine Learning |
| Docker |
| AWS |
| TensorFlow |
| Git |
| Pandas |
| NumPy |

The dataset can be extended by adding more skills.

---

## ⚙️ Working

1. User uploads Resume (PDF).
2. User pastes the Job Description.
3. Resume text is extracted using pdfplumber.
4. Text is cleaned and preprocessed.
5. Skills are extracted from both Resume and JD.
6. Cosine Similarity is calculated.
7. Matching and missing skills are displayed.
8. Suggestions are generated.

---

## 📈 Future Enhancements

- ATS Score Prediction
- Resume Formatting Analysis
- Semantic Skill Matching using Sentence Transformers
- AI-based Resume Suggestions
- PDF Report Generation
- Resume Ranking
- Multiple Resume Comparison
- Job Recommendation System
- Dashboard with Charts
- Support for DOCX Resume Upload

---

## 📷 Sample Output

```
Resume Match Score: 78%

Matching Skills
---------------
Python
SQL
Machine Learning
Git

Missing Skills
--------------
Docker
AWS
TensorFlow
NLP

Suggestions
-----------
Consider adding the missing skills if they match your experience.
```

---

## 👨‍💻 Author

**Name:** Your Name

**College:** Your College Name

**Department:** Computer Science / Information Technology

---

## 📄 License

This project is developed for educational purposes.
