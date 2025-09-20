"""
Python nodes for LangGraph workflow.

This module contains functions that handle Python code generation, execution, and processing
within the LangGraph workflow. These functions manage the complete Python script lifecycle
from code generation to execution and result summarization.

Functions:
1. python_formatter() - Generate Python code using AI agent
2. should_execute() - Decide between execution or summarization
3a. python_executor() -> run_python_script() - Execute code path
3b. python_summarizer() - Summarization path
4. should_continue_python_run() - Continue execution if needed
5. should_reformat() - Reformat code if execution failed
"""
import json
from typing import Any, Dict

from langchain_core.messages import ToolMessage,  AIMessage

from gamer_x.utils.models import(
    code_generator_agent,
    python_execute_agent,
    script_reformat_agent
)
from gamer_x.utils.models import(
    SONNET_4_LLM
)
from gamer_x.utils.prompts.python_executor import (
    get_python_excecute_prompt
    )
from gamer_x.utils.prompts.reformat_python import (
    get_reformat_python_prompt
    )
from gamer_x.utils.prompts.python_formatter import (
    get_python_format_prompt
    )
from gamer_x.utils.prompts.python_summarizer import(
    get_python_summary_prompt
)
from gamer_x.utils.tools import python_execute_tools

async def python_formatter(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Generates Python code based on user queries and schema context.
    
    This function uses an AI agent to generate Python code that addresses the user's
    query, taking into account any available schema context and previous code/responses.
    It handles both initial code generation and code refinement scenarios.
    
    Args:
        state (Dict[str, Any]): The workflow state containing:
            - query (str): The user's original query
            - schema_context (List, optional): Database schema information
            - python_code (str, optional): Previously generated Python code
            - python_code_response (str, optional): Previous code execution response
    
    Returns:
        Dict[str, Any]: Updated state with generated code:
            - messages (List): Generated Python code as message
            - python_code (str): The generated Python code
            - generation (str): Same as python_code for consistency
    """
    query = state['query']
    schema_context = state.get('schema_context', [])
    python_code = state.get("python_code", "No code has been generated yet")
    python_code_response = state.get("python_code_response", " ")

    prompt = get_python_format_prompt(
        python_code_response=python_code_response,
        python_code=python_code,
        schema_context=schema_context,
        query=query
    )
    
    try:
        answer = await code_generator_agent.ainvoke(prompt)
        
        # Safe extraction of python_code
        if hasattr(answer, 'tool_calls') and answer.tool_calls:
            python_code = answer.tool_calls[0]['args'].get('python_code', 'No code generated')
        else:
            # Fallback: try to extract from content
            python_code = getattr(answer, 'content', 'No code generated')
            
        return {
            "messages": [python_code],
            "python_code": python_code, 
            "generation": python_code
        }
    except Exception as e:
        error_msg = f"Python formatter failed: {str(e)}"
        return {
            "messages": [AIMessage(content=error_msg)],
            "python_code": error_msg,
            "generation": error_msg
        }

def should_execute(state: Dict[str, Any]) -> str:
    """
    Determines whether to execute or summarize Python code without execution.
    
    Args:
        state (Dict[str, Any]): The workflow state containing:
            - code_or_query (str): Route decision from code_query_assignment
    
    Returns:
        str: Execution path decision:
            - "execute" if route is "python_script_execute"
            - "summarize" for all other routes

    """
    route = state["code_or_query"]

    if route == "python_script_execute":
        return "execute" 
    # Otherwise if there is, we continue
    else:
        return "summarize"
    
async def python_summarizer(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Summarizes Python code without execution.
    
    This function provides a summary or explanation of the generated Python code
    without actually executing it. It's used when the workflow determines that
    code execution is not necessary or appropriate.
    
    Args:
        state (Dict[str, Any]): The workflow state containing:
            - python_code (str, optional): The Python code to summarize
            - query (str, optional): The original user query for context
    
    Returns:
        Dict[str, Any]: Updated state with summary:
            - messages (List): LLM response with code summary
            - generation (str): Extracted summary content

    """
    python_code = state.get("python_code", "No code has been generated yet")
    query = state.get("query")
    python_summary_prompt = get_python_summary_prompt(
        query=query,
        python_code=python_code
    )

    try:
        response = await SONNET_4_LLM.ainvoke(python_summary_prompt)
        
        # Safe content extraction
        if hasattr(response, 'content'):
            if isinstance(response.content, list) and len(response.content) > 0:
                content = response.content[0].get('text', str(response.content))
            else:
                content = str(response.content)
        else:
            content = str(response)

        return {
            "messages": [response], 
            "generation": content
        }
        
    except Exception as e:
        error_msg = f"Python summarizer failed: {str(e)}"
        return {
            "messages": [AIMessage(content=error_msg)],
            "generation": error_msg
        }


async def python_executor(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes Python code and returns result summary using AI agent.
    
    This function uses an AI agent to determine how to execute the generated
    Python code, taking into account previous execution attempts and responses.
    It generates tool calls for actual code execution. It summarizes the returned 
    code execution results.
    
    Args:
        state (Dict[str, Any]): The workflow state containing:
            - python_code (str, optional): The Python code to execute
            - python_code_response (str, optional): Previous execution response
            - python_execute_count (int, optional): Number of execution attempts
    
    Returns:
        Dict[str, Any]: Updated state with execution plan:
            - messages (List): Agent response with execution instructions
            - generation (str): Extracted response content
    
    """
    python_code = state.get("python_code", "No code has been generated yet")
    python_code_response = state.get("python_code_response", "There was no response generated by the script")

    python_execute_count = state.get("python_execute_count", 0)

    python_execute_prompt = get_python_excecute_prompt(
        python_code=python_code,
        python_code_response=python_code_response,
        python_execute_count=python_execute_count
    )

    try:
        response = await python_execute_agent.ainvoke(python_execute_prompt)
        
        # Safe content extraction
        if hasattr(response, 'content'):
            if isinstance(response.content, list) and len(response.content) > 0:
                content = response.content[0].get('text', str(response.content))
            else:
                content = str(response.content)
        else:
            content = str(response)

        return {
            "messages": [response],
            "generation": content
        }
        
    except Exception as e:
        error_msg = f"Python executor failed: {str(e)}"
        return {
            "messages": [AIMessage(content=error_msg)],
            "generation": error_msg
        }



async def run_python_script(state: Dict[str, Any]) -> Dict[str, Any]:
    """
    Executes Python tools and processes their results.

    Args:
        state (Dict[str, Any]): The workflow state containing:
            - messages (List): List of messages with tool calls to execute
            - python_execute_count (int, optional): Current count of Python execution attempts
    
    Returns:
        Dict[str, Any]: Updated state with execution results:
            - messages (List[ToolMessage]): Tool execution results as messages
            - python_code_response (str): Last tool execution result content
            - python_execute_count (int): Incremented execution counter
    
    """
    tool_call_count = state.get("python_execute_count", 0) + 1
    tools_by_name = {tool.name: tool for tool in python_execute_tools}

    outputs = []

    for i, tool_call in enumerate(state["messages"][-1].tool_calls):
        try:
            tool_result = await tools_by_name[tool_call["name"]].ainvoke(
                tool_call["args"]
            )

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
        "python_code_response": content,
        "python_execute_count": tool_call_count
    }

def should_continue_python_run(state: Dict[str, Any]) -> str:
    """
    Determines whether to continue Python execution or end the workflow.
    
    This function acts as a conditional edge in the LangGraph workflow, deciding
    whether to continue with more Python execution attempts or terminate the
    Python processing branch based on execution count and tool calls.
    
    Args:
        state (Dict[str, Any]): The workflow state containing:
            - messages (List): List of messages from the conversation
            - python_execute_count (int, optional): Number of Python execution attempts
    
    Returns:
        str: Decision for workflow continuation:
            - "end" if execution count exceeds limit or no tool calls present
            - "continue" if more Python execution should be performed
    
    Note:
        Maximum of 3 Python execution attempts are allowed to prevent infinite loops.
        Execution stops if the last message contains no tool calls.
    """
    messages = state["messages"]
    last_message = messages[-1]
    python_execute_count = state.get("python_execute_count", 0)

    # Add maximum retry limit to prevent infinite loops
    if python_execute_count >= 3:
        return "end"
    
    if not hasattr(last_message, 'tool_calls') or not last_message.tool_calls:
        return "end"
    else:
        return "continue"


async def should_reformat(state: Dict[str, Any]) -> str:
    """
    Determines if Python code needs reformatting based on execution results.
    
    This function uses an AI agent to analyze the current Python code, its execution
    response, and the original query to determine whether the code should be
    reformatted or improved for better results.
    
    Args:
        state (Dict[str, Any]): The workflow state containing:
            - python_code (str): The current Python code
            - python_code_response (str, optional): Execution response from the script
            - query (str): The original user query
            - python_execute_count (int, optional): Number of execution attempts
    
    Returns:
        str: Reformatting decision from the AI agent:
            - "reformat" if code should be reformatted
            - "no_reformat" if code is satisfactory
    
    """
    python_code = state["python_code"]
    python_code_response = state.get(
        "python_code_response", 
        "There was no response generated by the script"
    )
    query = state['query']
    python_execute_count = state.get("python_execute_count", 0)

    prompt = get_reformat_python_prompt(
        python_code=python_code,
        python_code_response=python_code_response,
        query=query,
        python_execute_count=python_execute_count
    )
    
    response = await script_reformat_agent.ainvoke(prompt)

    reformat = response['reformat']
    return reformat
