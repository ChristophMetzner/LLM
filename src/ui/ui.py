def prompt_welcome():
    """
    Welcomes user and prompts options.
    """
    print("Welcome to Text-to-Sequence-of-Nodes Generation!\n"
          "The program offers two options:\n\n"
          "1) Enter a text describing the functionality you wish to be performed. "
          "The program will then print a sequence of nodes implementing this functionality.\n\n"
          "2) Enter a text describing the functionality you wish to be performed"
          "and a sequence of nodes in this format Sequence: Node1 Node2 Node3 ... . The program will "
          "then print a sequence of nodes implementing this "
          "functionality together with an evaluation of its accuracy based on your input sequence"
          " of nodes.\n\n")

def ask_input():
    """
    Asks the user to provide input.

    Returns
    -------
    user_input : str
        Input text from the user.
    """
    user_input = input("Please enter your text:\n\n")
    return user_input

def parse_input(user_input):
    """
    Parses the user input and returns its components.

    Parameters
    -------
    user_input : str
        Input text from the user.

    Returns
    -------
    parsed_input : list
    """
    split_input = user_input.split()
    prompt = ""
    sequence = ""
    if "Sequence:" in split_input:
        found = False
        for element in split_input:
            if element == "Sequence:":
                found = True
                element = "" # this removes Sequence from the sequence of nodes
            if not found:
                prompt = prompt + " " + element
            else:
                sequence = sequence + " " + element
        parsed_input = [prompt, sequence]
    else:
        parsed_input = [user_input]
    return parsed_input