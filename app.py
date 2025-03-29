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
    
    st.set_page_config(page_title="Chat with multiple PDFs",page_icon=":books:")
    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header("Chat with multiple PDFs :books:")
    user_question = st.text_input("Ask a question about your documents:")
    if user_question:
        handle_userinput(user_question)





if __name__ == '__main__':
    main()