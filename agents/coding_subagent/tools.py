def run_linter(code_snippet: str) -> str:
    """Mock tool to lint code."""
    if "import" not in code_snippet:
        return "Warning: No imports found."
    return "Lint passed."
