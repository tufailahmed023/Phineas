
import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Cassandra
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


import os
from PyPDF2 import PdfReader

load_dotenv()

open_ai_api_key = os.getenv("OPENAI_API_KEY")

def get_pdf_text(pdf_path, log_file="processed_pdfs.txt", output_folder="extracted_texts"):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    # Read the log file to track already processed PDFs
    processed_pdfs = set()
    if os.path.exists(log_file):
        with open(log_file, "r") as f:
            processed_pdfs.update(f.read().splitlines())

    # Get list of PDF files to process
    pdf_files = []
    if os.path.isdir(pdf_path):  # If a folder is given
        pdf_files = [os.path.join(pdf_path, f) for f in os.listdir(pdf_path) if f.endswith(".pdf")]
    elif os.path.isfile(pdf_path) and pdf_path.endswith(".pdf"):  # If a single PDF file is given
        pdf_files = [pdf_path]
    else:
        print(f"Invalid path: {pdf_path}")
        return

    for pdf_file in pdf_files:
        pdf_name = os.path.basename(pdf_file)
        
        if pdf_name in processed_pdfs:
            print(f"Skipping already processed PDF: {pdf_name}")
            continue  # Skip already processed files

        print(f"Processing: {pdf_name}")
        text = ""

        try:
            pdf_reader = PdfReader(pdf_file)
            for page in pdf_reader.pages:
                text += page.extract_text() or ""  # Handle NoneType cases

            # Log the processed file
            with open(log_file, "a") as f:
                f.write(pdf_name + "\n")

        except Exception as e:
            print(f"Error processing {pdf_name}: {e}")

    print("PDF processing completed.")
    return text

# Example Usage:
# get_pdf_text("path/to/folder_with_pdfs")  # Process all PDFs in a folder
# get_pdf_text("path/to/single.pdf")  # Process a single PDF



def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def get_embeddings():
    embeddings = OpenAIEmbeddings(api_key=open_ai_api_key)
    return embeddings

def get_llm(): 
    llm = ChatOpenAI(model="gpt-3.5-turbo-1106",api_key=open_ai_api_key)
    return llm 

def get_vectorstore(text_chunks,embeddings,table_name):
    vectorstore = Cassandra(
    embedding=embeddings,
    table_name= table_name 
    session=None,
    keyspace=None,)
    return vectorstore

def get_conversation_chain(vectorstore,llm):
    
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_userinput(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)