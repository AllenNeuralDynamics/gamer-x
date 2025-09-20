"""LLM used in workflow"""
from langchain_aws.chat_models.bedrock import ChatBedrockConverse

BEDROCK_SONNET_4 = "us.anthropic.claude-sonnet-4-20250514-v1:0"

SONNET_4_LLM = ChatBedrockConverse(
    model=BEDROCK_SONNET_4,
    temperature=0,
    region_name="us-west-2"
)
