#insert python code 
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts.chat import ChatPromptTemplate

load_dotenv('.env_new')


def LLM_QnA_agent(question,temparature):
    model = AzureChatOpenAI(
        openai_api_version=os.environ["AZURE_OPENAI_API_VERSION"],
        azure_deployment=os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"],
        temperature=temparature
    )

    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant."),
            ("human", "{question}"),
        ]
    )
    messages = chat_template.format_messages(
        question = question
    )
    ai_message = model.invoke(messages)
    #print(ai_message.content)
    return ai_message.content

if __name__ == "__main__":
    response = LLM_QnA_agent('who is charlie chaplin',0.00)
    print(response)