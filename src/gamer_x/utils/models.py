# Models used in graph nodes

import os

from typing import Annotated, Literal, TypedDict

from langsmith import Client
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


from gamer_x.utils.tools import (
    schema_context_tools, 
    mongodb_execute_tools,
    python_execute_tools
    )
from gamer_x.utils.llms import SONNET_4_LLM


client = Client(api_key=os.getenv("LANGSMITH_API_KEY"))

#  Model that retrieves information about the schema structure 
template = client.pull_prompt("eden19/mcp-langgraph-schema-context")
schema_context_model = SONNET_4_LLM.bind_tools(schema_context_tools)
schema_context_agent = template | schema_context_model

#  Model that determines whether Python script or MongoDB query should be executed
class CodeorQuery(TypedDict):
    """Route a user query to the most relevant datasource."""

    route: Annotated[
        Literal["mongodb_query", "python_script_generate", "python_script_execute"],
        ...,
        (
            "Response to whether user's query "
            "should be solved with a mongodb query "
            "or python script. Select python_script_generate "
            "if script should just be generated. Choose "
            "python_script_execute if script should also be executed"
        ),
    ]

code_query_route_agent = SONNET_4_LLM.with_structured_output(CodeorQuery)


#  Model that executes MongoDB tools
mongodb_executor_agent = SONNET_4_LLM.bind_tools(mongodb_execute_tools)

#  Model that gives back code with the AIND data access API
class CodeGenerator(TypedDict):
    """Route a user query to the most relevant datasource."""

    python_code: Annotated[
        str,
        ...,
        (
            "String representation of pythonic code with the "
            "necessary imports and print statements"
        ),
    ]
code_generator_agent = SONNET_4_LLM.with_structured_output(CodeGenerator)
#prompt = client.pull_prompt("eden19/python_formatter")
# code_generator_agent = prompt | structured_code_generator

# Agent that examines python executor's output
class ScriptReformatOrNo(TypedDict):
    """Route a user query to the most relevant datasource."""

    reformat: Annotated[
        Literal["yes", "no"],
        ...,
        (
            "Yes if the python code should be reformatted"
            "No if python response can be summarized"
        ),
    ]

script_reformat_agent = SONNET_4_LLM.with_structured_output(ScriptReformatOrNo)

# Model that executes python script and summarize the response
python_execute_agent = SONNET_4_LLM.bind_tools(python_execute_tools)

# Filter generation for vector retrieval
class FilterGenerator(TypedDict):
    """MongoDB filter to be applied before vector retrieval"""

    filter_query: Annotated[dict, ..., "MongoDB match filter"]
    top_k: int = Annotated[dict, ..., "Number of documents"]


filter_prompt = client.pull_prompt("eden19/filtergeneration")
filter_generator_llm = SONNET_4_LLM.with_structured_output(FilterGenerator)
filter_generation_agent = filter_prompt | filter_generator_llm

# Check if retrieved documents answer question
class RetrievalGrader(TypedDict):
    """Relevant material in the retrieved document +
    Binary score to check relevance to the question"""

    binary_score: Annotated[
        Literal["yes", "no"],
        ...,
        "Retrieved documents are relevant to the query, 'yes' or 'no'",
    ]
retrieval_grader = SONNET_4_LLM.with_structured_output(RetrievalGrader)
retrieval_grade_prompt = client.pull_prompt("eden19/retrievalgrader")
doc_grader_agent = retrieval_grade_prompt | retrieval_grader

# Generating response to documents retrieved from the vector index
answer_generation_prompt = client.pull_prompt("eden19/answergeneration")
rag_agent = answer_generation_prompt | SONNET_4_LLM | StrOutputParser()