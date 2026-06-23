SKILL_ROADMAP = {
    "fastapi": {
        "priority": "High",
        "why": "Needed to build and deploy AI APIs.",
        "learn": [
            "Create GET and POST endpoints",
            "Use Pydantic request and response models",
            "Build a simple /chat API",
            "Deploy on Render",
        ],
    },
    "langchain": {
        "priority": "High",
        "why": "Useful for building RAG pipelines and AI workflows.",
        "learn": [
            "Prompt templates",
            "Document loaders",
            "Text chunking",
            "Retriever chains",
        ],
    },
    "llm": {
        "priority": "High",
        "why": "Required for GenAI applications and AI agents.",
        "learn": [
            "Tokens and context windows",
            "Temperature and top-p",
            "Prompt engineering",
            "Structured JSON outputs",
        ],
    },
    "rag": {
        "priority": "High",
        "why": "Common requirement for document-based AI assistants.",
        "learn": [
            "Embeddings",
            "Vector databases",
            "Chunking strategies",
            "Retrieval evaluation",
        ],
    },
    "docker": {
        "priority": "Medium",
        "why": "Useful for packaging and deploying applications.",
        "learn": [
            "Dockerfile basics",
            "Build and run containers",
            "Environment variables",
        ],
    },
    "aws": {
        "priority": "Medium",
        "why": "Common cloud platform requirement.",
        "learn": [
            "EC2 basics",
            "S3 basics",
            "Deploy a Python app",
        ],
    },
}


def get_learning_roadmap(missing_skills: list[str]) -> list[dict]:
    roadmap_items = []

    for skill in missing_skills:
        if skill in SKILL_ROADMAP:
            roadmap_items.append(
                {
                    "skill": skill,
                    **SKILL_ROADMAP[skill],
                }
            )

    return roadmap_items