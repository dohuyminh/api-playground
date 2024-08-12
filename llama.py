# This example is the new way to use the OpenAI lib for python
from openai import OpenAI

keyObj = open("llama-api-key.txt", "r")

client = OpenAI(
api_key = keyObj.readline(),
base_url = "https://api.llama-api.com"
)

keyObj.close()

response = client.chat.completions.create(
    model="llama-13b-chat",
    messages=[
        {"role": "system", "content": "Assistant is a large language model trained by OpenAI."},
        {"role": "user", "content": "Write a python script to print \"Hello, World!\" to the console"}
    ]
)

#print(response)
print(response.model_dump_json(indent=2))

for rep in response.choices:
    print(rep.message.content)
