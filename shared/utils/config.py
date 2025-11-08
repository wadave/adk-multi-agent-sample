import os


def get_llm_config():
    """Shared utility to get common LLM configuration."""
    return {"model": os.getenv("MODEL_NAME", "gemini-2.5-flash"), "temperature": 0.2}
