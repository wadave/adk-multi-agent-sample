import unittest
from shared.tools.common_tools import brave_search, get_current_time


class TestCommonTools(unittest.TestCase):
    def test_brave_search(self):
        result = brave_search("test query")
        self.assertIn("[Mock Search Result]", result)
        self.assertIn("test query", result)

    def test_get_current_time(self):
        result = get_current_time()
        self.assertRegex(result, r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}")


if __name__ == "__main__":
    unittest.main()
