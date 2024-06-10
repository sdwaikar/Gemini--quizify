import sys
import os
import streamlit as st
sys.path.append(os.path.abspath('../../'))
from tasks.task_3.task_3 import DocumentProcessor
from tasks.task_4.task_4 import EmbeddingClient
from tasks.task_5.task_5 import ChromaCollectionCreator



if __name__ == "__main__":
    embed_config = {
        "model_name" : "textembedding-gecko@003",
        "project"    : "gemini-quizify-425514", # Enter your own project id
        "location"   : "us-central1"
    }

    screen = st.empty()
    with screen.container():
        st.header("Shreyas Quizzify")

    processor = DocumentProcessor()
    processor.ingest_documents()
    embed_client = EmbeddingClient(**embed_config)
    chroma_creator = ChromaCollectionCreator(processor, embed_client)

    with st.form("Load data to Choma"):
        st.subheader("Quiz Builder")
        st.write("Select PDFs for Ingestion, the topic for the quiz, and click Generate.")

        # Use streamlit widgets to capture user input for the quiz topic and desired number of questions.
        topic_input = st.text_input("Enter the quiz topic:")
        number_input = st.slider("Select the number of questions", 1, 10, 5)

        document = None

        submitted = st.form_submit_button("Generate a Quiz.")
        if submitted:
            #####Code#####
            # Use create_chroma_collection() method to create a Chroma collection from the processed documents
            chroma_creator.create_chroma_collection()
            document = chroma_creator.query_chroma_collection(topic_input)

    if document:
        screen.empty()
        with st.container():
            st.header("Query Chroma for Topic, top Document: ")
            st.write(document)