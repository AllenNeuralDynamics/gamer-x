""" Cached prompt for use in Langgraph workflow """

def get_mongodb_execute_prompt(mongodb_output, 
                               mongodb_query, 
                               query, 
                               context,
                               tool_call_count):
    

    things_to_note = (
        '''
        ALWAYS unwind nested procedure fields (e.g., {'\$unwind': '\$procedures.subject_procedures.procedures'})
        Use \$unwind for any array fields
        For modality queries, access data_description.modality.name
        Use \$regex instead of \$elemmatch (e.g., {"field": {"\$regex": "term", "\$options": "i"}})
        Be careful with duration queries; don't use \$subtract as durations are stored as strings
        Ignore created and last_modified fields as they're only metadata
        Example query: What is the total duration of the imaging session for the subject in SmartSPIM_662616_2023-04-14_15-11-04?
        Example MONGODB Query:  [{'$match': {'name': 'SmartSPIM_662616_2023-04-14_15-11-04'}}]
        '''
    )

    mongodb_prompt = ("Your goal is to follow the instructions below very carefully."
                      "You are orchestrating tool access to a mongodb database"
                      "If the tool executed successfully, this is the response retrieved"
                      f" by the tool [{mongodb_output}]. This was the query used, [{mongodb_query}]." 
                      f"If there is a response, ensure that it can be used to answer the user's query [{query}]. "
                      "Ignore the syntax in which the response exists, and just process the information the tools retrieved. "
                      "If the output doesn't answer the question, think about how you can change the tool call to achieve an optimal result."
                      "If it answers the query stop tool calling immediately. When summarizing the tool result, "
                      "be conscise, while ensuring all the information requested by the user is present."
                      "If it requires more context, continue. Create an appropriate mongodb query or aggregation pipeline "
                      f"based on the following texts: {context} and execute the query."
                      f"Start with a simple query and refine only if necessary. Here are some things to note: {things_to_note}"
                      f"Optimize Data Retrieval:"
                      f" Use projection to select only necessary fields.\n"
                      f" Apply the `limit` filter.\n"
                      "4. **Tool Call Limits:**\n"
                      f"This is the tool call count number ({tool_call_count})"
                      "   - If tool_call_count exceeds 3, do not use any more tools.\n"
                      "   - Proceed with summarizing what information has been gathered so far.\n\n"
                    )
    messages = [
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": f"{mongodb_prompt}",
                },
                {
                    "type": "text",
                    "text": f"{things_to_note}",
                },
                {
                    "cachePoint": {"type": "default"},
                },
            ],
        },
    ]

    return messages