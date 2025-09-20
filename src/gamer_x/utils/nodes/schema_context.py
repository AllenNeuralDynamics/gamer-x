
"""
Schema context node for LangGraph workflow.

Functions:
1. get_schema_context() - Analyze user query and retrieve relevant schema information
"""
from typing import Any, Dict, List

from gamer_x.utils.llms import SONNET_4_LLM
from gamer_x.utils.prompts.schema_context_agent import (
    get_schema_context_prompt,
)

async def get_schema_context(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Retrieves and manages database schema context information.
    
    This function uses an AI agent to analyze the user's query and retrieve relevant
    database schema information that can help with query processing and code generation.
    It accumulates schema context over multiple calls to build comprehensive context.
    
    Args:
        state (Dict[str, Any]): The workflow state containing:
            - query (str, optional): The user's query to analyze for schema needs
            - schema_context (List, optional): Previously accumulated schema context
            - schema_call_count (int, optional): Number of schema context calls made
    
    Returns:
        Dict[str, Any]: Updated state with schema context:
            - messages (List): AI agent response with schema information
            - schema_context (List): Accumulated schema context information

    """
    query = state.get("query", "No query was provided")
    schema_context = state.get("schema_context", [])
    tool_call_count = state.get("schema_call_count", 0)

    prompt = get_schema_context_prompt(
        query=query,
        schema_context=schema_context,
        tool_call_count=tool_call_count
    )

    response = await SONNET_4_LLM.ainvoke(prompt)
    
    schema_context.append(response.content)

    return {
        "messages": [response],
        "schema_context": schema_context
    }
