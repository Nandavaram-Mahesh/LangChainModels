from langchain_openai import OpenAI
from dotenv import load_dotenv
import os

# This is Paid Veresion , which Requires API Key
load_dotenv()

# Get token from environment
openai_api_key = os.getenv("OPENAI_API_KEY")

if not openai_api_key:
    raise ValueError("openai_api_key not found. Please set the openai_api_key environment variable.")

llm = OpenAI(
    model="gpt-3.5-turbo-instruct",
    temperature=0,
    # max_retries=2,
    api_key=openai_api_key,
    # base_url="...",
    # organization="...",
    # other params...
)


input_text = "The meaning of life is "

result = llm.invoke(input_text)

print(result)