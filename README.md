**AI Resume Analyzer & Job Description Matcher**

Problem Statement

Students often apply to jobs without tailoring their resumes to the job description. Recruiters use Applicant Tracking Systems (ATS) that scan resumes for relevant keywords, skills, and qualifications. If important keywords are missing, the resume may never reach a human recruiter.

The objective is to build a web application that compares a student's resume with a given job description, calculates a match score, identifies missing keywords and skills, and provides suggestions to improve the resume.

Objectives

The application should:

Upload a resume (PDF/DOCX)
Paste or upload a Job Description
Compare resume with the JD
Calculate ATS Match Score
Highlight
Missing technical skills
Missing soft skills
Missing keywords
Suggest improvements
Display visual analytics
Tech Stack
Component	Technology
Frontend	Streamlit
Backend	Python
Resume Parsing	pdfplumber / PyMuPDF / python-docx
NLP	spaCy
Keyword Extraction	KeyBERT / YAKE
Similarity	Sentence Transformers
Visualization	Plotly / Matplotlib
AI Suggestions (Optional)	OpenAI API / Gemini API
Project Workflow
Resume Upload
      │
      ▼
Extract Text from Resume
      │
      ▼
Paste Job Description
      │
      ▼
Preprocess Text
(Remove stop words,
lowercase,
lemmatization)
      │
      ▼
Extract Skills & Keywords
      │
      ▼
Compare Resume vs JD
      │
      ├── Similarity Score
      ├── Matching Skills
      ├── Missing Skills
      ├── Missing Keywords
      ▼
Generate Suggestions
      │
      ▼
Display Dashboard
Features
1. Resume Upload

Supports

PDF
DOCX

Example

Upload Resume
2. Job Description Input

User pastes

Python Developer

Required Skills:

Python
SQL
Machine Learning
Git
Docker
AWS
REST APIs
3. ATS Match Score

Example

ATS Score

78%

or

Resume Match

████████░░ 80%
4. Matching Skills

✅ Found

Python
SQL
Git
Machine Learning
5. Missing Skills

❌ Missing

Docker
AWS
REST API
6. Missing Keywords

Example

CI/CD
Unit Testing
Agile
Pandas
NumPy
7. Suggestions
Add projects using Docker.

Mention AWS deployment.

Include REST API experience.

Add GitHub links.

Mention CI/CD pipeline experience.
8. Visual Dashboard

Charts

Skill Match Pie Chart
ATS Score Gauge
Keyword Frequency
Resume vs JD Similarity
Folder Structure
ResumeAnalyzer/

│
├── app.py
├── requirements.txt
│
├── parser/
│     pdf_parser.py
│     docx_parser.py
│
├── utils/
│     preprocessing.py
│     keyword_extractor.py
│     similarity.py
│     skills.py
│
├── data/
│     skills.csv
│
├── assets/
│
└── README.md
Algorithms Used
Text Preprocessing
Lowercase
Remove punctuation
Remove stopwords
Lemmatization

Libraries

spaCy
NLTK
Keyword Extraction

Possible methods

TF-IDF
KeyBERT
YAKE
Similarity

Best option

Sentence Transformers

all-MiniLM-L6-v2

Produces semantic similarity instead of simple keyword matching.

Skill Matching

Maintain a predefined skill database

Example

Python
Java
C++
SQL
MongoDB
Docker
AWS
Azure
Git
Linux
TensorFlow
PyTorch
Pandas
NumPy

Find intersection

Resume Skills ∩ JD Skills

Missing

JD Skills - Resume Skills
Streamlit Interface
---------------------------------------------------

        AI Resume Analyzer

---------------------------------------------------

Upload Resume

[ Choose PDF ]

Paste Job Description

-----------------------------------
|                                 |
|                                 |
|                                 |
-----------------------------------

[ Analyze Resume ]

---------------------------------------------------

ATS Score

82%

Matching Skills

✔ Python
✔ SQL
✔ Git

Missing Skills

✘ Docker
✘ AWS
✘ REST API

Suggestions

• Add Docker experience.
• Mention AWS deployment.
• Add REST API project.

---------------------------------------------------
Future Enhancements
Resume grammar checking
AI-generated resume improvements
Job recommendations based on resume
Resume rewriting
LinkedIn profile analysis
Multi-page resume support
Recruiter dashboard
Resume ranking for multiple candidates
Support for multiple languages
