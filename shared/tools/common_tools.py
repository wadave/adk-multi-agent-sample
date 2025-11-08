from datetime import datetime


def brave_search(query: str) -> str:
    """
    Shared tool for searching the web.
    Useful for any agent that needs external information.
    """
    # In a real app, this would call an actual API.
    return f"[Mock Search Result] Results for: {query}"


def get_current_time() -> str:
    """Returns the current server time."""
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
