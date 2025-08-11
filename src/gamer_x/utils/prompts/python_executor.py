def get_python_excecute_prompt(
        python_code: str,
        python_code_response: str,
        python_execute_count: int
        ):

    python_execute_prompt = f"""
    You are a Python and MongoDB expert.
    You have two types of tasks:
    1. Executing Python code by calling a tool.
    2. Summarizing the result of executed code.
    You must follow these strict rules:
    - Only execute code if there is NO response from a previous run.
    - If a response **has already been generated**, DO NOT call any tool. Summarize the response instead.
    - If the Python execute count exceeds 2, DO NOT execute code again. Summarize the current response instead.
    - NEVER modify the code — run it as is.
    - When summarizing do  not mention variables like the python code response, or python execute count, that is just for your reference.
    Inputs:
    - Python code: {python_code}
    - Python code response: {python_code_response}
    - Python execute count: {python_execute_count}
    Instructions:
    - If `python_code_response` is NOT empty or `python_execute_count` > 2, proceed directly to summarization.
    - Otherwise, execute the provided code using the tool.
    """
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{python_execute_prompt}",
                },
                {
                    "cachePoint": {"type": "default"},
                },
            ],
        },
    ]

    return messages