def get_python_summary_prompt(
        python_code: str,
        query:str
        ):

    python_summary_prompt = (
        f"""
    You are a Python expert who excels in summarizing python scripts. 
    Your task is to neatly display the python code you receive. Do not edit any part of the script. 
    You will also explain how the code works very briefly, given the user's query. Do not over explain. 
    Do not assume any information. Just work with the information below.

    User query: {query}
    Python code: {python_code}
    
    """
    )

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{python_summary_prompt}",
                },
                {
                    "cachePoint": {"type": "default"},
                },
            ],
        },
    ]

    return  messages