
import streamlit as st
from langchain_google_vertexai import VertexAIEmbeddings
import os

class EmbeddingClient:
    def __init__(self, model_name, project, location):
        try:
            self.client = VertexAIEmbeddings(model_name=model_name, project=project, location=location)
        except Exception as e:
            print(f"Failed to initialize client: {e}")
            self.client = None

    def embed_query(self, query):
        try:
            return self.client.embed_query(query)
        except AttributeError:
            print("Method embed_query not defined for the client.")
            return None
    
    def embed_documents(self, documents):
        try:
            return self.client.embed_documents(documents)
        except AttributeError:
            print("Method embed_documents not defined for the client.")
            return None
        
if __name__ == "__main__":
    model_name = "textembedding-gecko@003"
    project = "gemini-quizify-425514" 
    location = "us-central1"
    
    embedding_client = EmbeddingClient(model_name, project, location)
    vectors = embedding_client.embed_query("Hello World!")
    if vectors:
        st.write(vectors)