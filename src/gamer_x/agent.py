from dotenv import load_dotenv
load_dotenv()

from langgraph.graph import END, START, StateGraph
from langchain_core.messages import AIMessage, AnyMessage, ToolMessage, HumanMessage

from gamer_x.utils.state import GraphState
from gamer_x.utils.nodes.connectors import (
    set_query,
    code_query_assignment,
    code_query_router,
    # final_node
)
from gamer_x.utils.nodes.schema_context import (
    # should_continue_schema,
    get_schema_context,
    # get_schema_context_tools,
)
from gamer_x.utils.nodes.mongodb import (
    execute_mongodb_query, 
    get_mongodb_execute_tools,
    should_continue_mongodb,
)
from gamer_x.utils.nodes.python import (
    python_formatter,
    should_execute,
    python_summarizer,
    python_executor,
    run_python_script,
    should_continue_python_run,
    should_reformat
    )


workflow = StateGraph(GraphState)

workflow.add_node(set_query)
workflow.add_node(get_schema_context)
workflow.add_node(execute_mongodb_query)
# workflow.add_node("schema_context_tools", get_schema_context_tools)
workflow.add_node("mongodb_execute_tools", get_mongodb_execute_tools)
workflow.add_node(code_query_assignment)
workflow.add_node(python_formatter)
workflow.add_node(python_summarizer)
workflow.add_node(python_executor)
workflow.add_node("validate_python_script", run_python_script)
# workflow.add_node(final_node)

workflow.add_edge(START, "set_query")
workflow.add_edge("set_query", "get_schema_context")
workflow.add_edge("get_schema_context", "code_query_assignment")
# workflow.add_conditional_edges(
#     "get_schema_context",
#        should_continue_schema,
#     {
#         "continue": "schema_context_tools",
#         "end": "code_query_assignment",
#     },
# )

# workflow.add_edge("schema_context_tools", "get_schema_context")

workflow.add_conditional_edges(
    "code_query_assignment",
       code_query_router,
    {
        "mongodb": "execute_mongodb_query",
        "python": "python_formatter",
    },
)


workflow.add_conditional_edges(
    "execute_mongodb_query",
       should_continue_mongodb,
    {
        "continue": "mongodb_execute_tools",
        "end": END,
    },
)
workflow.add_edge("mongodb_execute_tools", "execute_mongodb_query")

workflow.add_conditional_edges(
    "python_formatter",
       should_execute,
    {
        "execute": "python_executor",
        "summarize": "python_summarizer"
    },
)
workflow.add_edge("python_summarizer", END)

workflow.add_conditional_edges(
    "python_executor",
       should_continue_python_run,
    {
        "continue": "validate_python_script",
        "end": END,
    },
)

workflow.add_conditional_edges(
    "validate_python_script",
    should_reformat,
    {
        "yes": "python_formatter",
        "no": "python_executor",
    },
)

# workflow.add_edge("final_node", END)



# workflow.add_conditional_edges(
#     "run_python_script",
#     should_continue_python,
#     {
#         "continue": "python_formatter",
#         "end": END,
#     },
# )

app = workflow.compile()

async def main(query: str):

    inputs = {
        "messages": [HumanMessage(query)],
        "query": query
    }

    # for chunk in app.astream(inputs,
    #                         stream_mode="values"):
    #     print(chunk)


    answer = await app.ainvoke(inputs)
    if hasattr(answer, "generation"):
        return answer["generation"]
    else:
        return answer

    #print(answer['generation'])

# import asyncio
# query = "for mouse 721291 can you make a table of sessions, date, and session_type?"
# print(asyncio.run((main(query))))
