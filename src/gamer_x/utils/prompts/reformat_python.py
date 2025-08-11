def get_reformat_python_prompt(
        python_code: str,
        python_code_response: str,
        query: int,
        python_execute_count: int
        ):

    reformat_python_prompt = (
        "You are a Python and MongoDB expert who is also a neuroscientist."
        f"A user asked this question: {query}"
        f"In order to answer this question, the following python code was executed: ({python_code})"
        f"This was the answer that was printed as a result of the python code ({python_code_response})"
        f"This is how many times the code has been formatted: ({python_execute_count})"
        "If the number is greater than 2, do not reformat."
        "Use the following questions to assess the question of whether the python code needs to be reformatted to produce a better answer"
        "Does the answer correlate with what the user asked for? If yes, continue. If no, reformat the python code."
        "Can the python code be reformatted to better answer the question? If yes, reformat the python code. If no, continue."
    )

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{reformat_python_prompt}",
                },
                {
                    "cachePoint": {"type": "default"},
                },
            ],
        },
    ]

    return messages