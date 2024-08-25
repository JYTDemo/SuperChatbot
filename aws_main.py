import os
import boto3
import json
from dotenv import load_dotenv

load_dotenv('.env_aws')


# Get an environment variable
AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
REGION_NAME = os.getenv('REGION_NAME')

boto3.setup_default_session(aws_access_key_id=AWS_ACCESS_KEY_ID,
                            aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                            region_name=REGION_NAME)

bedrock = boto3.client(service_name='bedrock-runtime')

modelId = os.getenv('MODEL_ID')
accept = 'application/json'
contentType = 'application/json'

def LLM_QnA_agent(question,temperature):
    body = json.dumps(
        {
            "anthropic_version": os.getenv("VERSION"),
            "max_tokens": 2000,
            "temperature":temperature,
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text":question
                        }
                    ]
                }
            ]
        }
    )




    # stream the response to client
    response = bedrock.invoke_model(body=body, modelId=modelId, accept=accept, contentType=contentType)
    response_body = json.loads(response.get('body').read())
    answer = response_body["content"][0]["text"]
    # print(answer)
    return(answer)

if __name__ == "__main__":
    response = LLM_QnA_agent('who is charlie chaplin',0.00)
    print(response)