from transformers import AutoTokenizer, AutoModelForSeq2SeqLM


tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-xl")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-xl")

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

def preprocess_prompt(prompt):
    """ Takes the prompt input from the user and augments it with further
    information to optimize LLM inference.

    Parameters
    ----------
    prompt : str
        The prompt input from the user.

    Returns
    -------
    preprocessed_prompt : str
        The augmented prompt.
    """
    node_dict_text = str(node_dictionary)
    preprocessed_prompt = "Map the following prompt [" + prompt + "] to a sequence of nodes" +\
                          " from this dictionary of nodes " + node_dict_text + "\n"

    return preprocessed_prompt

def llm(prompt,max_new_tokens):
    """ Takes the preprocessed prompt, tokenizes it, passes it to the LLM model and decodes the LLM output .

    Parameters
    ----------
    prompt : str
        The preprocessed prompt.
    max_new_tokens : int
        Model parameter limiting the length of the model output.

    Returns
    -------
    llm_output : str
        The decoded model output.
    """


    inputs = tokenizer(prompt, return_tensors='pt')
    outputs = model.generate(**inputs, max_new_tokens=max_new_tokens)
    llm_output = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return llm_output


def postprocess_output(llm_output):
    """ Takes the output from the LLM and extracts the sequence of nodes.
    Formats the sequence of nodes appropriately.

    Parameters
    ----------
    llm_output : str
        The output from the LLM.

    Returns
    -------
    sequence_of_nodes : list
        The extracted sequence of nodes.
    """
    sequence_of_nodes = []
    for word in llm_output.split():
        if word in node_dictionary.keys():
            sequence_of_nodes.append(word)
    #sequence_of_nodes = llm_output  # so far doesn't do anything
    if not sequence_of_nodes:
        sequence_of_nodes = ["No sequence of nodes matching your prompt found."]
    return sequence_of_nodes

