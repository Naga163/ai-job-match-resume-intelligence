import sys
from pathlib import Path

import streamlit as st


PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(PROJECT_ROOT / "backend"))

from job_recommender import get_top_job_recommendations
from matcher import calculate_match_score
from pdf_parser import extract_text_from_pdf
from roadmap import get_learning_roadmap


st.set_page_config(
    page_title="AI Job Match Platform",
    page_icon="🎯",
    layout="wide",
)

st.title("🎯 AI Job Match & Resume Intelligence")

st.write(
    "Upload your resume PDF or paste resume text, then compare it with a job description."
)

target_role = st.selectbox(
    "Choose your target role",
    [
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Analyst",
        "Automation Engineer",
        "Frontend Developer",
        "All Roles",
    ],
    index=0,
)

uploaded_resume = st.file_uploader(
    "Upload resume PDF",
    type=["pdf"],
)

resume_text = st.text_area(
    "Or paste your resume text",
    height=220,
    placeholder="Paste your resume content here...",
)

job_description = st.text_area(
    "Paste the job description",
    height=250,
    placeholder="Paste the job description here...",
)

if uploaded_resume is not None:
    try:
        extracted_resume_text = extract_text_from_pdf(uploaded_resume)

        if extracted_resume_text.strip():
            resume_text = extracted_resume_text
            st.success("Resume PDF text extracted successfully.")

            with st.expander("Preview extracted resume text"):
                st.write(extracted_resume_text)
        else:
            st.warning(
                "No readable text was found in this PDF. "
                "Try pasting the resume text manually."
            )

    except ValueError as error:
        st.error(str(error))

if st.button("Analyze Job Match", type="primary"):
    if not resume_text.strip() or not job_description.strip():
        st.warning("Please upload/paste a resume and paste the job description.")

    else:
        result = calculate_match_score(resume_text, job_description)

        st.metric("Job Match Score", f"{result['match_score']}%")
        st.subheader(result["match_level"])

        col1, col2 = st.columns(2)

        with col1:
            st.success("Matched Skills")

            if result["matched_skills"]:
                st.markdown(
                    " ".join(
                        f"`{skill.title()}`"
                        for skill in result["matched_skills"]
                    )
                )
            else:
                st.info("No matching skills found.")

        with col2:
            st.error("Missing Skills")

            if result["missing_skills"]:
                st.markdown(
                    " ".join(
                        f"`{skill.title()}`"
                        for skill in result["missing_skills"]
                    )
                )
            else:
                st.success("No major skill gaps found.")

        with st.expander("View all detected resume skills"):
            st.markdown(
                " ".join(
                    f"`{skill.title()}`"
                    for skill in result["resume_skills"]
                )
            )

        with st.expander("View all detected job skills"):
            st.markdown(
                " ".join(
                    f"`{skill.title()}`"
                    for skill in result["job_skills"]
                )
            )

        roadmap_items = get_learning_roadmap(result["missing_skills"])

        if roadmap_items:
            st.subheader("📚 Skill-Gap Learning Roadmap")

            for item in roadmap_items:
                with st.expander(
                    f"{item['skill'].title()} — {item['priority']} Priority"
                ):
                    st.write(item["why"])
                    st.markdown("**What to learn:**")

                    for topic in item["learn"]:
                        st.markdown(f"- {topic}")

        st.divider()
        st.subheader(
            f"💼 Recommended {target_role} Jobs for Your Resume"
        )

        recommendations = get_top_job_recommendations(
            resume_text=resume_text,
            target_role=target_role,
        )

        if not recommendations:
            st.info(
                f"No suitable {target_role} jobs were found in the current dataset."
            )

        for index, job in enumerate(recommendations, start=1):
            with st.expander(
                f"#{index} — {job['role']} at {job['company']} "
                f"({job['final_score']}% Recommendation Score)"
            ):
                st.write(f"**Location:** {job['location']}")
                st.write(
                    f"**Experience Required:** {job['experience_required']}"
                )
                st.write(f"**Resume Match:** {job['match_score']}%")
                st.write(f"**Match Level:** {job['match_level']}")
                st.write(
                    f"**Apply Readiness:** {job['apply_readiness']}"
                )
                st.write(
                    f"**Target Role Relevance:** "
                    f"{job['role_relevance']}%"
                )

                st.markdown("**Matched skills:**")

                if job["matched_skills"]:
                    st.markdown(
                        " ".join(
                            f"`{skill.title()}`"
                            for skill in job["matched_skills"]
                        )
                    )
                else:
                    st.write("No matched skills found.")

                st.markdown("**Missing skills:**")

                if job["missing_skills"]:
                    st.markdown(
                        " ".join(
                            f"`{skill.title()}`"
                            for skill in job["missing_skills"]
                        )
                    )
                else:
                    st.write("No major skill gaps found.")