from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts.chat import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv('.env_ollama')

def LLM_QnA_agent(question,temparature):
    llm = OllamaLLM(model=os.getenv('MODEL_NAME'),temparature=temparature,base_url="http://localhost:11434")
    chat_template = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant."),
            ("human", "{question}"),
        ]
    )

    # chain = messages | llm
    chain = chat_template | llm
    response = chain.invoke({"question":question})
    return(response)

if __name__ == "__main__":
    response = LLM_QnA_agent('who is charlie chaplin',0.00)
    print(response)