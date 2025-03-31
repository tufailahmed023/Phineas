
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Cassandra
from langchain.vectorstores import FAISS
from langchain_community.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from cassandra.cluster import Cluster


import os
from PyPDF2 import PdfReader

load_dotenv()

open_ai_api_key = os.getenv("OPENAI_API_KEY")

def get_pdf_text(pdf_path, log_file="processed_pdfs.txt", output_folder="extracted_texts"):

    output_folder_path = output_folder = os.path.join(os.path.expanduser("~/Desktop/Phineas"), output_folder)

    # Read the log file to track already processed PDFs
    processed_pdfs = set()
    log_file_path = os.path.join(output_folder_path, log_file)  # Fix path issue

    if os.path.exists(log_file_path):
        with open(log_file_path, "r") as f:
            processed_pdfs.update(f.read().splitlines())

    # Get list of PDF files to process
    pdf_files = []
    if os.path.isdir(pdf_path):  # If a folder is given
        pdf_files = [os.path.join(pdf_path, f) for f in os.listdir(pdf_path) if f.endswith(".pdf")]
    elif os.path.isfile(pdf_path) and pdf_path.endswith(".pdf"):  # If a single PDF file is given
        pdf_files = [pdf_path]
    else:
        print(f"Invalid path: {pdf_path}")
        return None  # Return None for invalid input

    

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
        
            with open(log_file_path, "a") as f:
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
    embeddings = OpenAIEmbeddings(model='text-embedding-3-small',api_key=open_ai_api_key)
    return embeddings

def get_llm(): 
    llm = ChatOpenAI(model="gpt-3.5-turbo-1106",api_key=open_ai_api_key)
    return llm 

# def get_vectorstore(embeddings,table_name,keyspace):
#     vectorstore = Cassandra(
#     embedding=embeddings,
#     table_name= table_name,
#     keyspace=keyspace
#     )
#     return vectorstore

def get_vectorstore(text_chunks,embeddings):
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore

def get_conversation_chain(vector_index,llm):
    
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_index.as_retriever(),
        memory=memory
    )
    return conversation_chain

