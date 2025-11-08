import unittest
from agents.research_subagent.tools import query_knowledge_base


class TestResearchTools(unittest.TestCase):
    def test_query_knowledge_base(self):
        result = query_knowledge_base("AI history")
        self.assertIn("[Mock KB]", result)
        self.assertIn("AI history", result)


if __name__ == "__main__":
    unittest.main()
