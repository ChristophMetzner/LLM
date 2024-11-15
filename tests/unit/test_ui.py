import unittest

from src.ui.ui import parse_input


class TestUI(unittest.TestCase):
    def test_parse_input_prompt(self):
        """
        Tests if a simple prompt is parsed correctly
        """
        prompt = "Navigate"
        result = parse_input(prompt)
        self.assertEqual(result, ["Navigate"])

    def test_parse_input_prompt_and_nodes(self):
        """
        Tests if a prompt followed by a sequence of nodes is parsed correctly
        """
        prompt = "Navigate after click Sequence: Node1 Node2"
        result = parse_input(prompt)
        self.assertEqual(result, [" Navigate after click","  Node1 Node2"])

if __name__ == '__main__':
    unittest.main()