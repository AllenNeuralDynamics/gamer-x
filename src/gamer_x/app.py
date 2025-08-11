
from gamer_x.agent import app
import logging

import chainlit as cl
from langchain_core.messages import HumanMessage, AIMessage
from langchain.schema.runnable.config import RunnableConfig

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@cl.set_starters
async def set_starters():
    return [
        cl.Starter(
            label="Learn about the metadata",
            message="Which projects have the most recorded assets?",
            icon="/public/idea.svg",
            ),

        cl.Starter(
            label="Summarize sessions",
            message="Tell me about mouse 747107.",
            icon="/public/learn.svg",
            ),
        cl.Starter(
            label="Create python scripts with the AIND Data Access API",
            message=f"Generate code to find experiments where the animal weight decreased by more than 10% between consecutive procedures.",
            icon="/public/terminal.svg",
            ),
        cl.Starter(
            label="Maintain metadata",
            message="I'm trying to understand an issue with misspelled project names. Could you help me write a query to get all project names and their counts?",
            icon="/public/write.svg",
            )
        ]
# ...

# @cl.on_chat_start
# async def start():
#     await cl.Message(
#         content="👋 Hello! Ask me anything about the AIND metadata!"
#     ).send()

@cl.on_message
async def on_message(msg: cl.Message):
    config = {"configurable": {"thread_id": cl.context.session.id}}
    cb = cl.LangchainCallbackHandler()
    
    # Track intermediate steps for user feedback
    current_step = cl.Message(content="🔄 Processing your query...")
    await current_step.send()
    
    try:
        # Track what we've seen and streaming messages per node
        seen_nodes = set()
        streaming_messages = {}  # Store streaming message for each node
        
        async for chunk, metadata in app.astream(
            {"messages": [HumanMessage(content=msg.content)]}, 
            stream_mode="messages", 
            config=RunnableConfig(callbacks=[cb], **config)
        ):
            node_name = metadata.get("langgraph_node", "unknown")
            #logger.info(f"Node: {node_name}, Content: {chunk.content if hasattr(chunk, 'content') else 'No content'}")
            
            # Track progress through your workflow
            if node_name not in seen_nodes:
                seen_nodes.add(node_name)
                step_messages = {
                    "set_query": "📝 Setting up your query...",
                    "get_schema_context": "🗄️ Getting database schema...",
                    "schema_context_tools": "🔧 Retrieving schema context",
                    "code_query_assignment": "🎯 Determining query type...",
                    "execute_mongodb_query": "🍃 Executing MongoDB query...",
                    "mongodb_execute_tools": "⚙️ Using AIND Data Access API...", 
                    "python_formatter": "🐍 Formatting Python code...",
                    "python_executor": "▶️ Summarizing Python script...",
                    "run_python_script": "▶️ Executing Python script...",
                    "final_node": "✨ Preparing final response..."
                }
                
                if node_name in step_messages:
                    current_step.content = step_messages[node_name]
                    await current_step.update()
            
            # Stream content from specific nodes
            stream_nodes = ["get_schema_context", "execute_mongodb_query", "python_executor"]

            # if (node_name == "python_formatter" and 
            #     hasattr(chunk, 'tool_call_chunks') and 
            #     chunk.tool_call_chunks and 
            #     chunk.tool_call_chunks[0].get('args')):
                
            #     if node_name not in streaming_messages:
            #         # Create a new streaming message for this node
            #         streaming_messages[node_name] = cl.Message(content="")


            #         node_headers = {
            #             "python_formatter": "▶️ **Python Script:**\n",
            #         }

            #         if node_name in node_headers:
            #             await streaming_messages[node_name].stream_token(node_headers[node_name])
                        
            #     await streaming_messages[node_name].stream_token(chunk.tool_call_chunks[0]['args'])
        
            
            if (node_name in stream_nodes and 
                hasattr(chunk, 'content') and 
                chunk.content and 
                not isinstance(chunk, HumanMessage) and
                chunk.content[0].get("text")):
                
                if node_name not in streaming_messages:
                    # Create a new streaming message for this node
                    streaming_messages[node_name] = cl.Message(content="")
                    
                    # Add a header for the node
                    node_headers = {
                        "get_schema_context": "📋 **Schema Information:**\n",
                        "execute_mongodb_query": "📊 **Query Results:**\n", 
                        "python_executor": "🐍 **Analysis Summary:**\n"
                    }
                    
                    if node_name in node_headers:
                        await streaming_messages[node_name].stream_token(node_headers[node_name])
                
                # Stream the content token by token or all at once
                await streaming_messages[node_name].stream_token(chunk.content[0]['text'])
        
        # Send all accumulated streaming messages
        for node_name, streaming_msg in streaming_messages.items():
            if streaming_msg.content.strip():  # Only send if there's content
                await streaming_msg.send()
        
        # Clean up the progress message
        await current_step.remove()
        
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        await current_step.remove()
        await cl.Message(content=f"❌ An error occurred: {str(e)}").send()