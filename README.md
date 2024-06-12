# Gemini-quizify

# Description

An AI-powered platform for generating quizzes using Google Cloud's Vertex AI. It features document ingestion via Streamlit, embedding creation with Vertex AI, and dynamic quiz generation. Users can upload PDFs, process them, and generate unique quiz questions through an interactive Streamlit interface.

# Task 1

Step 1: Create a Google Cloud Account
Substep A: Provide billing information to access GCP free trial credits

Step 2: Create a new Google Cloud Project

Step 3: Enable recommended APIs on Vertex AI

Step 4: Create a Service Account
Substep A: Give the service account 'owner' permissions
Substep B: Create a key for the service account

# Task 2

Step 1: Using your terminal, clone or fork the mission-quizify repository: https://github.com/radicalxdev/mission-quizify

Step 2: Add the local service account key to the repository
Substep A: Ensure that the .gitignore explicitly excludes your key for security purposes

Step 3: Export the key as authentication. An example command for WSL would be, export GOOGLE_APPLICATION_CREDENTIALS='service_account_key.json"
Substep A: If you encounter errors, check the path of authentication
Substep B: A second area of errors come from setting incorrect GCP permissions

# Task 3

Step 1: Render a file uploader widget. Replace 'None' with the Streamlit file uploader code.
Substep A: Allow multiple PDF types for ingestion

Step 2: Process the file
Substep A: Use PyPDFLoader from Langchain to load the PDF and extract pages. A reference document can be found here: https://python.langchain.com/docs/modules/data_connection/document_loaders/pdf#using-pypdf

Step 3: Add the extracted pages to the pages class variable

Step 4: Test the file using streamlit run to ensure documents can be ingested and processed for PDFs

![alt text](Task__3.png)

# Task 4

Step 1: Implement the init method to accept 'model_name', 'project', and 'location' parameters.

Step 2: Within the init method, initialize the 'self.client' attribute as an instance of VertexAIEmbeddings.

Step 3: Test the file using streamlit run and have a preview of Hello World as an embedding.

![alt text](Task__4.png)

# Task 5

Step 1: Check if any documents have been processed by the DocumentProcessor instance and display an error message if not.

Step 2: Split the processed documents into text chunks suitable for embedding and indexing using the CharacterTextSplitter from Langchain.

Step 3: Create a Chroma collection in memory with the text chunks obtained from step 2 and the embeddings model initialized in the class using the Chroma.from_documents method.

Step 4: Test the ChromaDB using streamlit run and upload a small PDF for testing if the Chroma Collection is created.

![alt text](Task__5.png)

# Task 6

Step 1: Begin by initializing an instance of the DocumentProcessor and invoke the ingest_documents() method to process the uploaded PDF documents.

Step 2: Configure and initialize the EmbeddingClient with the specified model, project, and location details as provided in the embed_config.

Step 3: Instantiate the ChromaCollectionCreator using the previously initialized DocumentProcessor and EmbeddingClient.

Step 4: Utilize Streamlit to construct a form. This form should prompt users to input the quiz's topic and select the desired number of questions via a slider component.

Step 5: Following the form submission, employ the ChromaCollectionCreator to forge a Chroma collection from the documents processed earlier.

Step 6: Enable users to input a query pertinent to the quiz topic. Utilize the generated Chroma collection to extract relevant information corresponding to the query, which aids in quiz question generation.

![alt text](Task__6.png)

# Task 7

Step 1: Within the init_llm() method for QuizGenerator class, set the LLM's model name to "gemini-pro"

Step 2: Configure the 'temperature' parameter to control the randomness of the output. A lower temperature results in more deterministic outputs.

Step 3: Specify 'max_output_tokens' to limit the length of the generated text. It is recommended to set within a range of 300 - 500 tokens.

Step 4: Initialize the LLM with the specified parameters to be ready for generating quiz questions.

Step 5: Within the generate_question_with_vectorstore() method, Verify the LLM and vectorstore are initialized and available.

Step 6: Retrieve relevant documents or context for the quiz topic from the vectorstore.

Step 7: Format the retrieved context and the quiz topic into a structured prompt using the system template.

![alt text](Task__7.png)

# Task 8

Step 1: Begin with the generate_quiz() method. Initialize an empty list to store the unique quiz questions.

Step 2: Loop through the desired number of questions (num_questions), generating each question via generate_question_with_vectorstore.

Step 3: For each generated question, validate its uniqueness using validate_question.

Step 4: If the question is unique, add it to the quiz; if not, continue the loop. Consider implementing a retry limit to prevent runaway LLM inferences and error loops.

Step 5: Return the compiled list of unique quiz questions.

Step 6: Within the validate_question() method, Extract the question text from the provided dictionary.

Step 7: Iterate over the existing questions in question_bank and compare their texts to the current question's text.

Step 8: If a duplicate is found, return False to indicate the question is not unique. If no duplicates are found, return True, indicating the question is unique and can be added to the quiz.

![alt text](Task__8.png)

# Task 9

Step 1: Within the QuizManager class, Store the provided list of quiz question objects in an instance variable named questions.

Step 2: Calculate and store the total number of questions in the list in an instance variable named total_questions.

Step 3: Within the next_question_index() method, Retrieve the current question index from Streamlit's session state.

Step 4: Adjust the index based on the provided direction (1 for next, -1 for previous), using modulo arithmetic to wrap around the total number of questions.

Step 5: Update the question_index in Streamlit's session state with the new, valid index.

Step 6: Starting on Line 113 under the line, Generated Quiz Question: , Use the get_question_at_index method to set the 0th index for a variable, index_question

Step 7: Unpack the choices from the question onto a radio Substep A: Set the key from the index question Substep B: Set the value from the index question

Step 8: Display the question onto streamlit using st.write()

Step 9: Use streamlit run to test the application. Upload a small PDF for ingestion and preview the generated question.

![alt text](Task__9.png)

# Task 10

Step 1: Initialize the question bank list in st.session_state on line 24.

Step 2: Set the topic input and number of questions using Streamlit's widgets for input starting on line 43.

Step 3: Initialize a QuizGenerator class using the topic, number of questions, and the chroma collection.

Step 4: Initialize the question bank list in st.session_state.

Step 5: Set a display_quiz flag in st.session_state to True.

Step 6: Set the question_index to 0 in st.session_state.

Step 7: Set index_question using the Quiz Manager method get_question_at_index passing the st.session_state["question_index"].

Step 8: Use the next_question_index method from our quiz_manager class in order to navigate the different questions within the quiz. Example: st.form_submit_button("Next Question, on_click=lambda: quiz_manager.next_question_index(direction=1)").

![alt text](Task__10.png)
