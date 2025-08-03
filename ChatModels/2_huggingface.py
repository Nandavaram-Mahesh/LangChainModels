from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
import os
from dotenv import load_dotenv

load_dotenv()

# Get token from environment
hf_token = os.getenv("HUGGINGFACEHUB_ACCESS_TOKEN")

if not hf_token:
    raise ValueError("Hugging Face token not found. Please set the HUGGINGFACEHUB_ACCESS_TOKEN environment variable.")



llm = HuggingFaceEndpoint(
    
    repo_id="deepseek-ai/DeepSeek-R1-0528",
    task="text-generation",
    huggingfacehub_api_token=hf_token,
    
)

model = ChatHuggingFace(llm=llm)

result = model.invoke("What is the capital of India")

print(result.content)