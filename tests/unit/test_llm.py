import unittest

from src.llm.llm import preprocess_prompt, postprocess_output

node_dictionary = {
        "OnVariableChange": "Triggered when a specified variable changes value.",
        "OnKeyRelease": "Triggered when a key is released",
        "OnKeyPress": "Triggered when a key is pressed.",
        "OnClick": "Triggered when an element is clicked.",
        "OnWindowResize": "Triggered when the window is resized.",
        "OnMouseEnter": "Triggered when the mouse pointer enters an element.",
        "OnMouseLeave": "Triggered when the mouse pointer leaves an element.",
        "OnTimer": "Triggered at specified time intervals.",
        "Console": "Prints a message to the console.",
        "Alert": "Displays an alert message.",
        "Log": "Logs information for debugging purposes.",
        "Assign": "Assigns a value to a variable.",
        "SendRequest": "Sends a network request.",
        "Navigate": "Navigates to a different URL or page.",
        "Save": "Saves data to local storage or a database.",
        "Delete": "Deletes specified data or records..",
        "PlaySound": "Plays an audio file.",
        "PauseSound": "Pauses an audio file.",
        "StopSound": "Stops an audio file.",
        "Branch": "Conditional node that branches based on a true/false evaluation.",
        "Map": "Transforms data from one format to another.",
        "Filter": "Filters data based on specified criteria.",
        "Reduce": "Reduces a list of items to a single value.",
        "Sort": "Sorts data based on specified criteria.",
        "GroupBy": "Groups data by a specified attribute.",
        "Merge": "Merges multiple datasets into one.",
        "Split": "Splits data into multiple parts based on criteria.",
        "Show": "Displays information on the screen.",
        "Hide": "Hides information from the screen.",
        "Update": "Updates the display with new information.",
        "DisplayModal": "Displays a modal dialog.",
        "CloseModal": "Closes an open modal dialog.",
        "Highlight": "Highlights an element on the screen.",
        "Tooltip": "Shows a tooltip with additional information.",
        "RenderChart": "Renders a chart with specified data.",
        "FetchData": "Fetches data from an API or database.",
        "StoreData": "Stores data in a variable or storage.",
        "UpdateData": "Updates existing data.",
        "DeleteData": "Deletes specified data.",
        "CacheData": "Caches data for performance improvement.",
    }


class TestLLM(unittest.TestCase):
    def test_preprocess_prompt(self):
        """
        Tests if a prompt is augmented correctly
        """
        prompt = "Navigate"
        result = preprocess_prompt(prompt)
        node_dict_text = str(node_dictionary)
        reference = "Map the following prompt [Navigate] to a sequence of nodes" +\
                          " from this dictionary of nodes " + node_dict_text + "\n"
        self.assertEqual(result, reference)

    def test_postprocess_output(self):
        """
        Tests if the sequence of nodes is correctly extracted.
        """
        llm_output = "The sequence of nodes is OnClick followed by Navigate"
        result = postprocess_output(llm_output)
        self.assertEqual(result, ["OnClick", "Navigate"])

    def test_postprocess_output_no_sequence(self):
        """
        Tests if postprocessing correctly identifies when no sequence is present.
        """
        llm_output = "This sentence does not contain a sequence."
        result = postprocess_output(llm_output)
        self.assertEqual(result, ["No sequence of nodes matching your prompt found."])