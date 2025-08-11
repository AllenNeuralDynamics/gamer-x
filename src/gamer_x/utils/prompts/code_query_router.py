def get_code_query_prompt(query: str):

    code_query_prompt = (
        "You are an expert at understanding a user's query and their goal."
        "The user will ask questions that would require you to access a mongodb database."
        "There are 2 types of queries - "
        "1. The user wants an answer to a question in the database, without any code or context about how the answer was derived"
        "2. The user wants to know the answer and how it can be derived with a python script that uses the AIND data access API."
        "To approach query type #1, there are 2 routes you can take. In the first route, you can use a mongodb client, and "
        "problem solve with queries, projections and aggregation pipelines."
        "Choose this route if the query is straightforward doesn't require complex math calculations."
        "The other route is to generate a python script that uses pythonic mongodb retrieval functions and execute the script."
        "Use this route if access to pythonic elements will benefit approaching the problem. "
        "Like creating a dataframe, or if you suspect the retrieval will be especially dense."
        "If the second type of query is asked, choose the python method always."
        "If any mathematical operators like, division, less than or greater than have to be used, use python."
        f"This is the user's query: {query}"
        "Respond with one of the following:"
        "mongodb_query - query can be approached with executing a mongodb query,"
        "python_script_execute - python script needs to be generated and executed"
        "python_script_generate - python script only needs to be generated"
    )

    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{code_query_prompt}",
                },
                {
                    "cachePoint": {"type": "default"},
                },
            ],
        },
    ]

    return messages