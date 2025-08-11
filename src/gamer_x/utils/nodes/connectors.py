from langchain_core.messages import AIMessage
from gamer_x.utils.prompts.code_query_router import get_code_query_prompt
from gamer_x.utils.models import(
    code_query_route_agent
)

def set_query(state: dict):
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

async def code_query_assignment(state:dict):
    query = state['query']
    code_query_prompt = get_code_query_prompt(query=query)
    answer = await code_query_route_agent.ainvoke(
        code_query_prompt
    )
    route = answer['route']
    return {"code_or_query": route}  

def code_query_router(state):
    route = state["code_or_query"]

    if route == "mongodb_query":
        return "mongodb"
    # Otherwise if there is, we continue
    else:
        return "python"

async def clarify_query(state:dict):
    query = state['query']
    pass
# def final_node(state):
#     final_answer = str(state.get("generation", "No answer was produced"))
#     #message = final_answer['generation']['content'][0]['text']
    
#     return {"messages": [AIMessage(content=final_answer)],
#             "generation": final_answer}