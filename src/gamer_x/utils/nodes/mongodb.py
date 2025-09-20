"""
MongoDB nodes for LangGraph workflow.

This module contains functions that handle MongoDB operations within the LangGraph workflow.
These functions manage database queries, tool execution, and result processing for the
AIND data access API integration.

Functions:
1. execute_mongodb_query() - Generate and execute MongoDB queries using AI agent
2. get_mongodb_execute_tools() - Execute the actual database tools
3. should_continue_mongodb() - Decide whether to continue or end the MongoDB operations
"""
import json
from typing import Any, Dict

from langchain_core.messages import ToolMessage

from gamer_x.utils.tools import mongodb_execute_tools
from gamer_x.utils.prompts.mongodb_executor import get_mongodb_execute_prompt
from gamer_x.utils.models import(
    mongodb_executor_agent
)
    
def should_continue_mongodb(state: Dict[str, Any]) -> str:
    """
    Determines whether to continue MongoDB operations or end the workflow.
    
    This function acts as a conditional edge in the LangGraph workflow, deciding
    whether to continue with more MongoDB operations or terminate the MongoDB
    processing branch.
    
    Args:
        state (Dict[str, Any]): The workflow state containing:
            - messages (List): List of messages from the conversation
            - mongodb_call_count (int, optional): Number of MongoDB tool calls made
    
    Returns:
        str: Decision for workflow continuation:
            - "end" if no tool calls in last message or call count exceeds limit
            - "continue" if more MongoDB operations should be performed
    
    Note:
        Maximum of 4 MongoDB tool calls are allowed to prevent infinite loops.
    """
    messages = state["messages"]
    last_message = messages[-1]
    mongodb_call_count = state.get("mongodb_call_count", 0)

    if not last_message.tool_calls:
        return "end"
    elif mongodb_call_count > 4:
        return "end"
    else:
        return "continue"

async def get_mongodb_execute_tools(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes MongoDB tools and processes their results.
    
    This function takes tool calls from the last message in the state and executes
    the corresponding MongoDB tools (like get_records, aggregation_retrieval, etc.)
    from the AIND data access API. It handles tool execution, error handling, and
    result formatting.
    
    Args:
        state (Dict[str, Any]): The workflow state containing:
            - messages (List): List of messages with tool calls to execute
            - mongodb_call_count (int, optional): Current count of MongoDB tool calls
    
    Returns:
        Dict[str, Any]: Updated state with tool execution results:
            - messages (List[ToolMessage]): Tool execution results as messages
            - mongodb_output (List[ToolMessage]): Same as messages, for reference
            - mongodb_query (List[Dict]): List of tool call arguments used
            - mongodb_call_count (int): Incremented tool call counter
    
    Note:
        Tool results are JSON-serialized for consistent formatting. Exceptions
        are caught and included in the tool message content for error handling.
    """
    tool_call_count = state.get("mongodb_call_count", 0) + 1
    
    tools_by_name = {tool.name: tool for tool in mongodb_execute_tools}

    outputs = []
    mongodb_query = []

    for i, tool_call in enumerate(state["messages"][-1].tool_calls):
        try:
            tool_result = await tools_by_name[tool_call["name"]].ainvoke(
                tool_call["args"]
            )

            mongodb_query.append(tool_call['args'])
            content = json.dumps(tool_result)
        except Exception as e:
            content = str(e)

        outputs.append(
            ToolMessage(
                content=content,
                name=tool_call["name"],
                tool_call_id=tool_call["id"],
            )
        )

    return {
        "messages": outputs,
        "mongodb_output": outputs,
        "mongodb_query": mongodb_query,
        "mongodb_call_count": tool_call_count
    }


async def execute_mongodb_query(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Summarizes MongoDB query results and generates final response using AI agent.
    
    This function takes the current state with schema context, previous MongoDB
    outputs, and user query to generate appropriate MongoDB tool calls or final
    responses. It uses the MongoDB executor agent to determine next actions.
    
    Args:
        state (Dict[str, Any]): The workflow state containing:
            - schema_context (List, optional): Database schema information
            - mongodb_output (List, optional): Previous MongoDB tool results
            - mongodb_query (str, optional): Previous MongoDB query parameters
            - query (str, optional): Original user query
            - mongodb_call_count (int, optional): Current MongoDB tool call count
    
    Returns:
        Dict[str, Any]: Updated state with agent response:
            - messages (List): Agent response messages
            - generation (str, optional): Final response content if no more tool calls
            - error (str, optional): Error message if input is too long
    
    Raises:
        Exception: Catches and handles model input length errors specifically.
    
    Note:
        If the agent response contains no tool calls, it's considered a final
        answer and includes a 'generation' field. Input length errors are
        handled gracefully with user-friendly error messages.
    """
    context = state.get('schema_context', [])
    mongodb_output = state.get('mongodb_output', [])
    mongodb_query = state.get("mongodb_query", "")
    query = state.get("query", "")
    tool_call_count = state.get("mongodb_call_count", 0) 

    try:
        mongodb_prompt = get_mongodb_execute_prompt(
            context=context,
            mongodb_output=mongodb_output,
            mongodb_query=mongodb_query,
            query=query,
            tool_call_count=tool_call_count
        )

        response = await mongodb_executor_agent.ainvoke(mongodb_prompt)

        if not response.tool_calls:
            return {"messages": [response], "generation": response.content}
    
    except Exception as e:
        error_message = str(e)

        if "Input is too long for requested model" in error_message:
            return {
                "messages": [],
                "error": "Data retrieved is too long for the model to synthesize. Reduce the size of the input, context, or query."
            }
    
    return {"messages": [response]}
