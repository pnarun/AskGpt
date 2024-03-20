import os

os. environ ["OPENAI_API_KEY"] = "YOUR OPENAI KEY"

from llama_index import VectorStoreIndex, SimpleDirectoryReader

documents = SimpleDirectoryReader("docs").load_data()
index = VectorStoreIndex.from_documents(documents)
index.storage_context.persist()