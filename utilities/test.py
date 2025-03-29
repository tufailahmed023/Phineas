from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
import os
from dotenv import load_dotenv
load_dotenv()


open_ai_api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-3.5-turbo-1106",api_key=open_ai_api_key)
response = llm([HumanMessage(content="What is LangChain?")])
print(response)
