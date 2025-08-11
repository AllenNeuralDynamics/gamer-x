from langchain_aws.chat_models.bedrock import ChatBedrockConverse, ChatBedrock

BEDROCK_SONNET_4 = "us.anthropic.claude-sonnet-4-20250514-v1:0"
BEDROCK_HAIKU_3_5 = "us.anthropic.claude-3-5-haiku-20241022-v1:0"

SONNET_4_LLM = ChatBedrockConverse(
    model=BEDROCK_SONNET_4,
    temperature=0,
    #streaming=True,
)
# HAIKU_3_5_LLM = ChatBedrock(
#     model=BEDROCK_HAIKU_3_5,
#     model_kwargs={"temperature": 0},
# )
