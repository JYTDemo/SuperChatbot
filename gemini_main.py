from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts.chat import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv('.env_gemini')

def LLM_QnA_agent(question,temparature):
    
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro-latest",temperature=temparature)
    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant."),
            ("human", "{question}"),
        ]
    )

    # chain = messages | llm
    chain = chat_template | llm
    response = chain.invoke({"question":question})
    return(response.content)

if __name__ == "__main__":
    response = LLM_QnA_agent('who is charlie chaplin',0.00)
    print(response)