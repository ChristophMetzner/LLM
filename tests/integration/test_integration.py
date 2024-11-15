import unittest

from src.ui.ui import  parse_input
from src.llm.llm import preprocess_prompt, llm, postprocess_output
from src.evaluation.evaluate import evaluate_sequence

class TestPrompt(unittest.TestCase):
    def test_simple_prompt(self):
        user_input = "Navigate on mouse click"
        parsed_input = parse_input(user_input)
        # preprocess user input
        preprocessed_prompt = preprocess_prompt(parsed_input[0])
        # pass preprocessed input to llm
        llm_output = llm(preprocessed_prompt, 50)
        # postprocess llm output
        postprocessed_output = postprocess_output(llm_output)
        self.assertEqual(postprocessed_output, ["OnCLick","Navigate"])

    def test_prompt_and_sequence(self):
        user_input = "Navigate on mouse click Sequence: OnClick Navigate"
        parsed_input = parse_input(user_input)
        #preprocess user input
        preprocessed_prompt = preprocess_prompt(parsed_input[0])
        # pass preprocessed input to llm
        llm_output = llm(preprocessed_prompt,50)
        # postprocess llm output
        postprocessed_output = postprocess_output(llm_output)
        # display output
        # optional: evaluate output
        if len(parsed_input)>1:
            reference_sequence = parsed_input[1].split()
            evaluation_results = evaluate_sequence(reference_sequence, postprocessed_output)
            self.assertEqual(evaluation_results, 1.0)