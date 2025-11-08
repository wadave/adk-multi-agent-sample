from google.adk.agents import LlmAgent
import sys
from pathlib import Path

# Ensure project root is in sys.path for imports to work in all contexts
# (works for both 'adk run' and regular Python imports)
project_root = Path(__file__).parent.parent.parent
if str(project_root) not in sys.path:
    sys.path.insert(0, str(project_root))

# Use absolute imports from project root
from agents.research_subagent.agent import research_agent  # noqa: E402
from agents.coding_subagent.agent import coding_agent  # noqa: E402
from shared.tools.common_tools import get_current_time  # noqa: E402

super_orchestrator = LlmAgent(
    name="super_orchestrator",
    model="gemini-2.5-flash",  # Default model
    instruction="""
    You are the lead orchestrator.
    Receive user requests and delegate them to your specialized sub-agents:
    - 'research_subagent' for information gathering.
    - 'coding_subagent' for writing or checking code.

    Always use the appropriate sub-agent for the task.
    """,
    sub_agents=[research_agent, coding_agent],
    tools=[get_current_time],
)

root_agent = super_orchestrator
