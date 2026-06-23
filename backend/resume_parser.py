import re
from typing import List


SKILL_LIBRARY = [
    "python",
    "sql",
    "excel",
    "pandas",
    "numpy",
    "matplotlib",
    "scikit-learn",
    "machine learning",
    "deep learning",
    "fastapi",
    "flask",
    "streamlit",
    "react",
    "javascript",
    "html",
    "css",
    "git",
    "github",
    "json",
    "llm",
    "rag",
    "langchain",
    "chromadb",
    "faiss",
    "power bi",
    "tableau",
    "postgresql",
    "mysql",
    "docker",
    "aws",
    "azure",
    "tensorflow",
    "pytorch",
]

SKILL_ALIASES = {
    "api": "apis",
    "apis": "apis",
    "rest api": "apis",
    "rest apis": "apis",
    "machine-learning": "machine learning",
    "ml": "machine learning",
    "large language model": "llm",
    "large language models": "llm",
}


def extract_skills(text: str) -> List[str]:
    """Extract normalized technical skills from text."""

    normalized_text = text.lower()
    found_skills = set()

    for skill in SKILL_LIBRARY:
        pattern = r"\b" + re.escape(skill) + r"\b"

        if re.search(pattern, normalized_text):
            found_skills.add(skill)

    for alias, standard_skill in SKILL_ALIASES.items():
        pattern = r"\b" + re.escape(alias) + r"\b"

        if re.search(pattern, normalized_text):
            found_skills.add(standard_skill)

    return sorted(found_skills)