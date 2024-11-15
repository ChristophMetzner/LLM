from ui.ui import prompt_welcome, ask_input, parse_input
from llm.llm import preprocess_prompt, llm, postprocess_output
from evaluation.evaluate import evaluate_sequence



def main():
    # launch UI and get user input
    prompt_welcome()
    user_input = ask_input()
    parsed_input = parse_input(user_input)
    # preprocess user input
    preprocessed_prompt = preprocess_prompt(parsed_input[0])
    # pass preprocessed input to llm
    llm_output = llm(preprocessed_prompt,50)
    # postprocess llm output
    postprocessed_output = postprocess_output(llm_output)
    # display output
    print("The sequence of nodes to your prompt:\n")
    print(postprocessed_output)
    # optional: evaluate output
    if len(parsed_input)>1:
        reference_sequence = parsed_input[1].split()
        evaluation_results = evaluate_sequence(reference_sequence, postprocessed_output)
        print("Evaluating generated sequence of nodes against the user provided sequence of nodes:\n")
        print(evaluation_results)


if __name__ == "__main__":
    main()