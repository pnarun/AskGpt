import os
from fastapi import FastAPI
import uvicorn

os. environ ["OPENAI_API_KEY"] = "YOUR OPENAI KEY"

from llama_index import StorageContext, load_index_from_storage

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)
query_engine = index.as_query_engine()



# response = query_engine.query("Explain Document splitting?")
# print (response)


app = FastAPI()

@app.get("/query")
def query(question : str):
    response = query_engine.query(question)
    return response

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host = "0.0.0.0",
        port = 8080,
    )