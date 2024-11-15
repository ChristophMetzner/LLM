import unittest

from src.evaluation.evaluate import evaluate_sequence


class TestEvaluate(unittest.TestCase):
    def test_evaluate_sequence_same_length(self):
        """
        Tests if two sequences of the same lengths are evaluated correctly
        """
        llm_sequence = ["Node2", "Node4"]
        reference_sequence = ["Node2", "Node4"]
        result = evaluate_sequence(llm_sequence, reference_sequence)
        self.assertEqual(result, 1.0)

    def test_evaluate_sequence_llm_longer(self):
        """
        Tests if two sequences of unequal lengths, with the llm generated sequences being longer
        are evaluated correctly
        """
        llm_sequence = ["Node2", "Node4", "Node5", "Node7"]
        reference_sequence = ["Node2", "Node4"]
        result = evaluate_sequence(llm_sequence, reference_sequence)
        self.assertEqual(result, 0.5)

    def test_evaluate_sequence_llm_shorter(self):
        """
        Tests if two sequences of unequal lengths, with the llm generated sequences being shorter
        are evaluated correctly
        """
        llm_sequence = ["Node2"]
        reference_sequence = ["Node2", "Node4", "Node5", "Node7"]
        result = evaluate_sequence(llm_sequence, reference_sequence)
        self.assertEqual(result, 0.25)

if __name__ == '__main__':
    unittest.main()