import json

from langchain_core.messages import ToolMessage

from gamer_x.utils.tools import mongodb_execute_tools
from gamer_x.utils.prompts.mongodb_executor import get_mongodb_execute_prompt
from gamer_x.utils.models import(
    mongodb_executor_agent
)
    
def should_continue_mongodb(state):
    messages = state["messages"]
    last_message = messages[-1]
    mongodb_call_count = state.get("mongodb_call_count", 0)

    if not last_message.tool_calls:
        return "end"
    elif mongodb_call_count > 4:
        return "end"
    else:
        return "continue"

async def get_mongodb_execute_tools(state: dict):
    """
    Retrieving information from MongoDB with tools
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
            content = e

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


async def execute_mongodb_query(state: dict):

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

        response = await mongodb_executor_agent.ainvoke(
            mongodb_prompt
        )


        if not response.tool_calls:
            return {"messages": [response], "generation": response.content}
    
    except Exception as e:
        error_message = str(e)

        if "Input is too long for requested model" in error_message:
            return {
                "messages": [],
                "error": "Data retrieved is too long for the model to synthesize. Reduce the size of the input, context, or query."
            }
    return {"messages":[response]}
