import streamlit as st 
import sys 
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from DatabaseUpdate.vector_index import vector_index
from utilities.utilites import get_llm,get_conversation_chain
from Templates.htmlTemplates import bot_template,user_template,css

llm = get_llm()
vector_index_q = vector_index

def handle_userinput(user_question):
    st.session_state.conversation = get_conversation_chain(vector_index=vector_index,llm=llm)
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i % 2 == 0:
            st.write(user_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace(
                "{{MSG}}", message.content), unsafe_allow_html=True)


def main():
    

    # Set page title and icon
    st.set_page_config(page_title="Chat with Your PDFs 📚", page_icon="📖", layout="wide")

    # Apply custom CSS (if any)
    st.write(css, unsafe_allow_html=True)

    # Initialize session state variables
    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    # Sidebar Section
    st.sidebar.title("📂 Processed PDFs")
    pdf_list_path = "extracted_texts/processed_pdfs.txt"

    if os.path.exists(pdf_list_path):
        with open(pdf_list_path, "r") as file:
            pdf_files = file.readlines()
        pdf_files = [pdf.strip() for pdf in pdf_files if pdf.strip()]  # Remove empty lines
    else:
        pdf_files = []

    if pdf_files:
        for pdf in pdf_files:
            st.sidebar.markdown(f"✅ {pdf}")
    else:
        st.sidebar.markdown("❌ No PDFs processed yet.")

    st.sidebar.markdown("---")
    st.sidebar.markdown("📌 **Happy Analyzing :) **")

    # Page Header
    st.markdown("<h1 style='text-align: center;'>📖 Chat with Your PDFs 📖</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px;'>Ask anything about your uploaded documents!</p>", unsafe_allow_html=True)

    # User Input
    user_question = st.text_input("🔍 Ask a question:")
    if user_question:
        handle_userinput(user_question)

    # Footer Note
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px; color: gray;'>💡 Tip: Upload multiple PDFs and get instant insights!</p>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 14px; color: white;'> @Team Mission Possiable : Phineas </p>", unsafe_allow_html=True)




if __name__ == '__main__':
    main()