from typing import Annotated, List, Optional

from langchain_core.messages import AIMessage, AnyMessage, ToolMessage
from langgraph.graph.message import add_messages
from typing_extensions import TypedDict

class GraphState(TypedDict):
    """
    Represents the state of our graph.

    Attributes --
    messages: Conversation between user and GAMER stored in a list
    query: Question asked by user
    chat_history: Summary of conversation
    generation: LLM generation
    data_source: Chosen db to query
    documents: List of documents
    filter: Used before vector retrieval to minimize the size of db
    top_k: # of docs to retrieve from VI
    tool_output: Retrieved info from MongoDB
    """

    messages: Annotated[list[AnyMessage], add_messages]
    query: str
    tool_call: Optional[str]
    schema_context: Optional[str]
    summarized_schema_context: Optional[str]
    chat_history: Optional[str]
    generation: str
    mongodb_output: Optional[List[ToolMessage]]
    mongodb_query: Optional[dict]
    error: Optional[str]
    code_or_query: Optional[str]
    schema_call_count: Optional[int] 
    mongodb_call_count: Optional[int] 
    python_execute_count: Optional[int] 
    python_code: Optional[str]
    python_code_response: Optional[str]