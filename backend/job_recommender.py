from pathlib import Path

import pandas as pd

from matcher import calculate_match_score


PROJECT_ROOT = Path(__file__).resolve().parent.parent
JOBS_FILE = PROJECT_ROOT / "data" / "jobs.csv"


ROLE_KEYWORDS = {
    "AI Engineer": [
        "ai engineer",
        "machine learning",
        "llm",
        "rag",
        "fastapi",
        "genai",
        "vector database",
    ],
    "Machine Learning Engineer": [
        "machine learning",
        "ml engineer",
        "scikit-learn",
        "model",
        "random forest",
        "classification",
    ],
    "Data Analyst": [
        "data analyst",
        "sql",
        "excel",
        "power bi",
        "pandas",
        "dashboard",
    ],
    "Automation Engineer": [
        "automation",
        "python",
        "apis",
        "json",
        "fastapi",
    ],
    "Frontend Developer": [
        "frontend",
        "react",
        "html",
        "css",
        "javascript",
    ],
}


def get_role_relevance(job: pd.Series, target_role: str) -> float:
    """Calculate how relevant a job is to the selected target role."""

    if target_role == "All Roles":
        return 1.0

    searchable_text = (
        f"{job['role']} {job['skills']} {job['job_description']}"
    ).lower()

    keywords = ROLE_KEYWORDS.get(target_role, [])

    if not keywords:
        return 0.0

    matched_keywords = sum(
        keyword in searchable_text
        for keyword in keywords
    )

    return matched_keywords / len(keywords)


def get_apply_readiness(final_score: float) -> str:
    """Return a practical application-readiness label."""

    if final_score >= 75:
        return "Ready to Apply"

    if final_score >= 55:
        return "Apply After Small Improvements"

    return "Learn Key Skills First"


def get_top_job_recommendations(
    resume_text: str,
    target_role: str = "All Roles",
    top_n: int = 3,
) -> list[dict]:
    """Return jobs ranked by resume fit and selected target role."""

    jobs_df = pd.read_csv(JOBS_FILE)
    recommendations = []

    for _, job in jobs_df.iterrows():
        job_text = f"{job['skills']} {job['job_description']}"
        result = calculate_match_score(resume_text, job_text)

        role_relevance = get_role_relevance(job, target_role)

        if target_role != "All Roles" and role_relevance == 0:
            continue

        role_score = round(role_relevance * 100, 2)

        final_score = round(
            (result["match_score"] * 0.70)
            + (role_score * 0.30),
            2,
        )

        recommendations.append(
            {
                "role": job["role"],
                "company": job["company"],
                "location": job["location"],
                "experience_required": job["experience_required"],
                "match_score": result["match_score"],
                "role_relevance": role_score,
                "final_score": final_score,
                "apply_readiness": get_apply_readiness(final_score),
                "match_level": result["match_level"],
                "matched_skills": result["matched_skills"],
                "missing_skills": result["missing_skills"],
            }
        )

    recommendations.sort(
        key=lambda item: item["final_score"],
        reverse=True,
    )

    return recommendations[:top_n]