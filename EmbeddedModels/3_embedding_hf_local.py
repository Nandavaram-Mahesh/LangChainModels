from langchain_huggingface import HuggingFaceEmbeddings

embedding = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "Delhi is the capital of India",
    "Kolkata is the capital of West Bengal",
    "Paris is the capital of France"
]

# If single Query
# query = "What is the capital of India?"
# vector = embedding.embed_query(query)

#If list of Queries/Documents 
vector = embedding.embed_documents(documents)

print(str(vector))