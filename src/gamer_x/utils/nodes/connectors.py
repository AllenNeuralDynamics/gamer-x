"""
Miscellaneous nodes used in LangGraph workflow.

Functions:
1. set_query() - Extract user query and initialize state
2. code_query_assignment() - Classify query type using AI agent
3. code_query_router() - Route to appropriate execution path
4. clarify_query() - Ask for clarification if needed (TODO)
"""
from typing import Any

from gamer_x.utils.prompts.code_query_router import get_code_query_prompt
from gamer_x.utils.models import(
    code_query_route_agent
)

def set_query(state: dict) -> dict[str, Any]:
    """
    First node in workflow.
    Sets query in state graph, and resets tool call nodes to 0.
    
    Args:
        state (dict): The workflow state containing messages from the user.
                     Expected to have a 'messages' key with a list of messages.
    
    Returns:
        dict[str, Any]: Updated state with query extracted and counters reset:
            - query (str): The content of the last user message, 
                           which should be a query
            - mongodb_call_count (int): Reset to 0
            - schema_call_count (int): Reset to 0  
            - python_execute_count (int): Reset to 0
            - python_code_response (str): Default response message
    """
    query = state["messages"][-1].content
    tool_call_count = 0
    response = "Code hasn't been executed yet"
    return {
        "query": query,
        "mongodb_call_count": tool_call_count,
        "schema_call_count": tool_call_count,
        "python_execute_count": tool_call_count,
        "python_code_response": response
    }

async def code_query_assignment(state: dict) -> dict[str, str]:
    """
    Determines if a query needs to be solved through the
    MongoDB (and the AIND data access API) or through
    writing a python script and executing it.
    
    Args:
        state (dict): The workflow state containing the user query.
                     Expected to have a 'query' key with the user's question.
    
    Returns:
        dict[str, str]: Dictionary containing the routing decision:
            - code_or_query (str): Either "mongodb_query" for database queries
                                  or "python" for code execution tasks
    
    Note:
        This is an async function that invokes an AI agent to classify the query type.
    """
    query = state['query']
    code_query_prompt = get_code_query_prompt(query=query)
    answer = await code_query_route_agent.ainvoke(
        code_query_prompt
    )
    route = answer['route']
    return {"code_or_query": route}  

def code_query_router(state: dict) -> str:
    """
    Explicit path for workflow to follow based on results 
    of the code_query_assignment node.
    
    Args:
        state (dict): The workflow state containing routing information.
                     Expected to have a 'code_or_query' key with the route decision.
    
    Returns:
        str: The next node to execute in the workflow:
            - "mongodb" if the query should be handled by MongoDB query execution
            - "python" if the query should be handled by Python code execution
    
    Note:
        This function acts as a conditional edge in the LangGraph workflow.
    """
    route = state["code_or_query"]

    if route == "mongodb_query":
        return "mongodb"
    # Otherwise if there is, we continue
    else:
        return "python"

async def clarify_query(state: dict) -> dict[str, Any]:
    """
    Asks clarifying questions if user's query isn't
    specific enough.
    
    Args:
        state (dict): The workflow state containing the user query.
                     Expected to have a 'query' key with the user's question.
    
    Returns:
        dict[str, Any]: Updated state with clarification response.
    
    Note:
        This function is currently not implemented (contains only 'pass').
        When implemented, it should analyze the query for ambiguity and
        generate appropriate clarifying questions for the user.
    
    TODO:
        - Implement query analysis logic
        - Generate clarifying questions
        - Return appropriate response structure
    """
    query = state['query']
    # TODO: Implement clarification logic
    pass
