from google.adk.agents import LlmAgent
from .tools import run_linter

coding_agent = LlmAgent(
    name="coding_subagent",
    model="gemini-2.5-flash",  # Default model
    instruction="""
    You are a software engineering assistant.
    You can write and lint code.
    """,
    tools=[run_linter],
)

root_agent = coding_agent
