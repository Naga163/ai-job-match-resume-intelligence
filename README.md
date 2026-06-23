# 🎯 AI Job Match & Resume Intelligence

An AI-powered job matching platform that analyzes a resume against job descriptions, identifies skill gaps, recommends suitable roles, and provides a learning roadmap.

## Features

- Upload a resume PDF or paste resume text
- Extract text from PDF resumes
- Compare resume skills with job descriptions
- Generate a job-match score
- Show matched and missing skills
- Provide a skill-gap learning roadmap
- Select a target career role
- Recommend relevant jobs from a dataset
- Show application readiness:
  - Ready to Apply
  - Apply After Small Improvements
  - Learn Key Skills First

## Target Roles

- AI Engineer
- Machine Learning Engineer
- Data Analyst
- Automation Engineer
- Frontend Developer

## Tech Stack

- Python
- Streamlit
- pandas
- NumPy
- pdfplumber
- scikit-learn
- Git and GitHub

## Project Structure

```text
ai-job-match-resume-intelligence/
│
├── backend/
│   ├── job_recommender.py
│   ├── matcher.py
│   ├── pdf_parser.py
│   ├── resume_parser.py
│   └── roadmap.py
│
├── data/
│   └── jobs.csv
│
├── frontend/
│   └── app.py
│
├── screenshots/
├── requirements.txt
└── README.md