from google.adk.agents import LlmAgent
import sys
from pathlib import Path

# Ensure project root is in sys.path for imports to work in all contexts
# (works for both 'adk run' and regular Python imports)
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

from shared.tools.common_tools import brave_search  # noqa: E402
from .tools import query_knowledge_base  # noqa: E402

# Define the agent
research_agent = LlmAgent(
    name="research_subagent",
    model="gemini-2.5-flash",  # Default model
    instruction="""
    You are a specialized research assistant.
    Use `brave_search` for general web info and `query_knowledge_base` for deep internal knowledge.
    Provide concise summaries of your findings.
    """,
    tools=[brave_search, query_knowledge_base],
)

# Expose as root_agent if we want to run this agent in isolation via `adk run agents/research_subagent`
root_agent = research_agent
