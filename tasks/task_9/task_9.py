import streamlit as st
import os
import sys
import json
sys.path.append(os.path.abspath('../../'))
from tasks.task_3.task_3 import DocumentProcessor
from tasks.task_4.task_4 import EmbeddingClient
from tasks.task_5.task_5 import ChromaCollectionCreator
from tasks.task_8.task_8 import QuizGenerator

class QuizManager:

    def __init__(self, questions: list):
        self.questions = questions
        self.total_questions = len(questions)
    
    def get_question_at_index(self, index: int):
        valid_index = index % self.total_questions
        return self.questions[valid_index]

    def next_question_index(self, direction=1):
        if st.session_state["question_index"] is not None:
            current_index = st.session_state["question_index"]
            new_index = (current_index + direction) % self.total_questions
            st.session_state["question_index"] = new_index
        else:
            return ValueError("session_state not found")

if __name__ == "__main__":
    from tasks.task_3.task_3 import DocumentProcessor
    from tasks.task_4.task_4 import EmbeddingClient
    from tasks.task_5.task_5 import ChromaCollectionCreator
    from tasks.task_8.task_8 import QuizGenerator

    embed_config = {
        "model_name" : "textembedding-gecko@003",
        "project"    : "gemini-quizify-425514", # Enter your own project id
        "location"   : "us-central1"
    }

    screen = st.empty()
    with screen.container():
        st.header("Quiz Builder")
        processor = DocumentProcessor()
        processor.ingest_documents()

        embed_client = EmbeddingClient(**embed_config)
        chroma_creator = ChromaCollectionCreator(processor, embed_client)

        question = None
        question_bank = None
        
        with st.form("Load Data to Chroma"):
            st.subheader("Quiz Builder")
            st.write("Select PDFs for Ingestion, the topic for the Quiz, and click Generate.")

            topic_input = st.text_input("Topic for Generative Quiz", placeholder="Enter the topic of the document.")
            number_input = st.slider("Number of Questions", min_value=1, max_value=10, value=1)

            submitted = st.form_submit_button("Submit")
            if submitted:
                chroma_creator.create_chroma_collection()

                st.write(topic_input)

                
                generator = QuizGenerator(topic_input, number_input, chroma_creator)
                question_bank = generator.generate_quiz()
    
    if question_bank:
        screen.empty()
        with st.container():
            st.header("Generated Quiz Question: ")
            quiz_manager = QuizManager(question_bank)
            with st.form("Multiple Choice Question"):
                index_question = quiz_manager.get_question_at_index(0)
                choices = []
                for choice in index_question['choices']:
                    key = choice["key"]
                    value = choice["value"]
                    choices.append(f"{key}) {value}")
                    
                st.write(f"{index_question['question']}")

                answer = st.radio(
                    'Choose the correct answer',
                    choices
                )
                st.form_submit_button("Submit")

                if submitted:
                    correct_answer_key = index_question['answer']
                    if answer.startswith(correct_answer_key):
                        st.success("Correct")
                    else:
                        st.error("Incorrect")