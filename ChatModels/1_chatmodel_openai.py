from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

# Get token from environment
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("openai_api_key not found. Please set the openai_api_key environment variable.")

model = ChatOpenAI(model='gpt-4.0', temperature=1.5, max_completion_tokens=10, openai_api_key=openai_api_key)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)