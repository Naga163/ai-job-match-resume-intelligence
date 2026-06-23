from resume_parser import extract_skills


def calculate_match_score(resume_text: str, job_description: str) -> dict:
    """Compare resume skills against job-description skills."""

    resume_skills = set(extract_skills(resume_text))
    job_skills = set(extract_skills(job_description))

    matched_skills = sorted(resume_skills.intersection(job_skills))
    missing_skills = sorted(job_skills.difference(resume_skills))

    if not job_skills:
        score = 0.0
    else:
        score = round((len(matched_skills) / len(job_skills)) * 100, 2)

    if score >= 75:
        match_level = "Strong Match"
    elif score >= 45:
        match_level = "Medium Match"
    else:
        match_level = "Low Match"

    return {
        "match_score": score,
        "match_level": match_level,
        "resume_skills": sorted(resume_skills),
        "job_skills": sorted(job_skills),
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
    }