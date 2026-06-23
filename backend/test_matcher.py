from matcher import calculate_match_score


resume_text = """
B.Tech CSE Data Analytics graduate with Python, pandas, NumPy,
SQL, FastAPI, Git, GitHub, Streamlit and machine learning experience.
Built dashboards, APIs, and automation projects.
"""

job_description = """
We need an AI Engineer with Python, Machine Learning, FastAPI,
LLM, RAG, APIs, JSON and SQL knowledge.
"""

result = calculate_match_score(resume_text, job_description)

for key, value in result.items():
    print(f"{key}: {value}")