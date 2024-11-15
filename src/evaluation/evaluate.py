def evaluate_sequence(reference_sequence,llm_sequence):
    """ Takes the sequence of nodes inferred by the LLM and compares it
    to the reference sequence provided by the user.

    Parameters
    ----------
    llm_sequence : list
        The postprocessed output sequence from the LLM.
    reference_sequence : list
        The sequence provided by the user.

    Returns
    -------
    match_score : float
        The fraction of nodes matching between both sequences.
    """
    score = 0
    if len(llm_sequence) == len(reference_sequence):
        for i in range(len(llm_sequence)):
            if llm_sequence[i] == reference_sequence[i]:
                score +=1
        match_score = score/len(llm_sequence)
    elif len(llm_sequence) > len(reference_sequence):
        for i in range(len(reference_sequence)):
            if reference_sequence[i] == llm_sequence[i]:
                score +=1
        match_score = score/len(llm_sequence)
    else:
        for i in range(len(llm_sequence)):
            if reference_sequence[i] == llm_sequence[i]:
                score +=1
        match_score = score/len(reference_sequence)

    return match_score