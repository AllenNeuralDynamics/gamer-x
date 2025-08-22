from langchain_core.tools import tool
from aind_data_access_api.document_db import MetadataDbClient
from typing import Literal, Any
from langchain_experimental.utilities import PythonREPL

#from gamer_x.utils.retrievers.schema_context_retriever import SchemaContextRetriever

# API_GATEWAY_HOST = "api.allenneuraldynamics.org"
# DATABASE = "metadata_index"
# COLLECTION = "data_assets"

API_GATEWAY_HOST = "api.allenneuraldynamics-test.org"
DATABASE = "metadata_vector_index"
COLLECTION = "static_eval_data_assets_3_14"

docdb_api_client = MetadataDbClient(
    host=API_GATEWAY_HOST,
    database=DATABASE,
    collection=COLLECTION,
)

# @tool
# async def retrieve_schema_context(
#     query: str,
#     collection: Literal[
#         "data_schema_fields_index",
#         #"data_schema_defs_index",
#         "data_schema_core_index",
#     ],
# ):
#     """
#     collection -
#     1. data_schema_fields_index:
#     - Search for information about schema properties, field definitions,
#     data types, validation rules, and field-specific requirements.
#     - Use when you need to understand what fields are available or how specific
#       properties work.
#     - Use cases:
#         - Building field selections (`$project`)
#         - Understanding field types for queries
#         - Checking required vs optional fields
#         - Field-specific validation rules
#     # 2. data_schema_defs_index:
#     # - Search for schema definitions, enums, nested object structures,
#     # and reusable components.
#     # - Use when you need to understand data models, allowed values,
#     # or complex nested structures.
#     # - Use cases:
#     #     - Working with enum values (`$match` with specific values)
#     #     - Understanding nested object structures
#     #     - Looking up allowed values for fields
#     #     - Complex data type definitions
#     3. data_schema_core_index:
#     - Search for Python implementation details, validation logic,
#         business rules, and model relationships.
#     - Use when you need to understand how validation works or
#         implementation-specific context.
#     query instructions:
#     - Simplify the user's query for the relevant collection, keep in mind that
#     this query will be used to perform vector search against a database
#     - Use cases:
#         - Understanding business logic validation
#         - Model relationships and dependencies
#         - Implementation-specific constraints
#         - Custom validation rules

#     **Process:** Always search the most relevant vector store first,
#                 then use additional stores if you need more context.
#     Hierarchical Search Strategy:
#     1. **Primary Search**: Use the vector store most relevant to
#                             your query type
#     2. **Context Search**: If needed, search related vector stores for
#                             additional context
#     3. **Validation Search**: Check core vector store for any business rules
#         that might affect your query

#     Example: For a query filtering by "sex" field:
#     1. Search Properties → understand "sex" field structure
#     2. Search Defs → get allowed values (Male/Female)
#     3. Search Core → check any validation rules
#     4. Query Type Mapping
#     Provide explicit mappings:

#     Query Intent → Vector Store Priority:

#     **Field Existence/Types**: Properties → Core → Defs
#     **Value Filtering**: Defs → Properties → Core
#     **Aggregation Pipelines**: Properties → Defs → Core
#     **Validation Context**: Core → Properties → Defs
#     **Schema Structure**: Defs → Properties → Core

#     """
#     retriever = SchemaContextRetriever(k=4, collection=collection)
#     documents = await retriever._aget_relevant_documents(query=query)
#     return documents

def count_fields(obj: dict = None)-> int:
    """Recursively count all fields in a nested JSON structure"""
    if isinstance(obj, dict):
        count = len(obj)  
        for value in obj.values():
            count += count_fields(value) 
        return count
    elif isinstance(obj, list):
        count = 0
        for item in obj:
            count += count_fields(item)
        return count
    else:
        return 0 


@tool
def aggregation_retrieval(agg_pipeline: list) -> Any:
    """
    Executes a MongoDB aggregation pipeline for complex data transformations
    and analysis.

    WHEN TO USE THIS FUNCTION:
    - When you need to perform multi-stage data processing operations
    - For complex queries requiring grouping, filtering, sorting in sequence
    - When you need to calculate aggregated values (sums, averages, counts)
    - For data transformation operations that can't be done with simple queries

    NOT RECOMMENDED FOR:
    - Simple document retrieval (use get_records instead)
    - When you only need to filter data without transformations
    Executes a MongoDB aggregation pipeline and returns the aggregated results.

    This function processes complex queries using MongoDB's aggregation
    framework, allowing for data transformation, filtering, grouping, and
    analysis operations. It handles the execution of multi-stage aggregation
    pipelines and provides error handling for failed aggregations.

    Parameters
    ----------
    agg_pipeline : list
        A list of dictionary objects representing MongoDB aggregation stages.
        Each stage should be a valid MongoDB aggregation operator.
        Common stages include: $match, $project, $group, $sort, $unwind.

    Returns
    -------
    list
        Returns a list of documents resulting from the aggregation pipeline.
        If an error occurs, returns an error message string describing
        the exception.

    Notes
    -----
    - Include a $project stage early in the pipeline to reduce data transfer
    - Avoid using $map operator in $project stages as it requires array inputs
    """
    try:
        result = docdb_api_client.aggregate_docdb_records(
            pipeline=agg_pipeline
        )

        if not result:
            return "No documents matched the query"

        field_count_in_one_asset = count_fields(result[0])
        len_list = len(result)
        estimated_total_fields = field_count_in_one_asset * len_list

        if estimated_total_fields > 8000:
            return ("The data retrieved is too long to injest." 
                    "Refine your query to limit data retrieved.")
    
        return result

    except Exception as ex:
        template = "An exception of type {0} occurred. Arguments:\n{1!r}"
        message = template.format(type(ex).__name__, ex.args)
        return message


@tool
def get_records(filter: dict = {}, 
                projection: dict = {}, 
                limit: int = 100) -> Any:
    """
    Retrieves documents from MongoDB database using simple filters
    and projections.

    WHEN TO USE THIS FUNCTION:
    - For straightforward document retrieval based on specific criteria
    - When you need only a subset of fields from documents
    - When the query logic doesn't require multi-stage processing
    - For better performance with simpler queries

    NOT RECOMMENDED FOR:
    - Complex data transformations (use aggregation_retrieval instead)
    - Grouping operations or calculations across documents
    - Joining or relating data across collections

    Parameters
    ----------
    filter : dict
        MongoDB query filter to narrow down the documents to retrieve.
        Example: {"subject.sex": "Male"}
        If empty dict object, returns all documents.

    projection : dict
        Fields to include or exclude in the returned documents.
        Use 1 to include a field, 0 to exclude.
        Example: {"subject.genotype": 1, "_id": 0}
        will return only the genotype field.
        If empty dict object, returns all documents.

    limit: int
        Limit retrievals to a reasonable number, try to not exceed 100

    Returns
    -------
    list
        List of dictionary objects representing the matching documents.
        Each dictionary contains the requested fields based on the projection.

    """

    records = docdb_api_client.retrieve_docdb_records(
        filter_query=filter, projection=projection, limit=limit
    )

    if not records:
        return "No documents matched the query"

    field_count_in_one_asset = count_fields(records[0])
    len_list = len(records)
    estimated_total_fields = field_count_in_one_asset * len_list

    if estimated_total_fields > 8000:
        return ("The data retrieved is too long to injest." 
                "Refine your query to limit data retrieved.")

    return records


@tool
def python_executor(python_code: str):
    ''' Tool that executes python code '''
    python_run = PythonREPL() 
    answer = python_run.run(python_code)

    return answer


#schema_context_tools = [retrieve_schema_context]
mongodb_execute_tools = [aggregation_retrieval, get_records]
python_execute_tools = [python_executor]