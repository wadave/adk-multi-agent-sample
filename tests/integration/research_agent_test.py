import unittest
from unittest.mock import MagicMock
import sys

# Mock google.adk
mock_adk = MagicMock()
sys.modules["google"] = mock_adk
sys.modules["google.adk"] = mock_adk.adk
sys.modules["google.adk.agents"] = mock_adk.adk.agents


# Mock LlmAgent to just store init args
class MockLlmAgent:
    def __init__(self, name, instruction, tools, **kwargs):
        self.name = name
        self.instruction = instruction
        self.tools = tools


sys.modules["google.adk.agents"].LlmAgent = MockLlmAgent

# Now import the agent under test
from agents.research_subagent.agent import research_agent  # noqa: E402


class TestResearchAgentStructure(unittest.TestCase):
    def test_agent_initialization(self):
        """Test that the agent is initialized with correct name and tools."""
        self.assertEqual(research_agent.name, "research_subagent")
        # Check that it has 2 tools
        self.assertEqual(len(research_agent.tools), 2)
        # Tools are raw functions
        tool_names = [t.__name__ for t in research_agent.tools]
        self.assertIn("brave_search", tool_names)
        self.assertIn("query_knowledge_base", tool_names)


if __name__ == "__main__":
    unittest.main()
