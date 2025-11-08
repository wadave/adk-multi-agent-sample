def query_knowledge_base(topic: str) -> str:
    """
    Agent-specific tool for querying a specialized internal database.
    Only the researcher agent needs this.
    """
    return f"[Mock KB] Detailed academic notes on {topic}"
