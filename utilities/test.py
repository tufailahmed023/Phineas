from langchain_openai.chat_models import ChatOpenAI
from langchain.schema import HumanMessage
from langchain_community.vectorstores import Cassandra
import sys 
import os 
import cassio


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utilities.utilites import get_pdf_text, get_vectorstore , get_text_chunks , get_embeddings
import os
from dotenv import load_dotenv
load_dotenv()

print(os.path.dirname(os.path.abspath(__file__)))

astra_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
astra_db_id = os.getenv("ASTRA_DB_ID")
key_space = os.getenv("ASTRA_KEYSPACE")
open_ai_api_key = os.getenv("OPENAI_API_KEY")
table_name = "mission_possiable"

# llm = ChatOpenAI(model="gpt-3.5-turbo-1106",api_key=open_ai_api_key)
# response = llm([HumanMessage(content="What is LangChain?")])
# print(response)
pdf_path = '/Users/tufailahmed/Desktop/PDFs'

# text = get_pdf_text(pdf_path=pdf_path)
# t_c = get_text_chunks(text)
# embeddings = get_embeddings(
# print(t_c[:1])

from astrapy import DataAPIClient

# Initialize the client
client = DataAPIClient(astra_token)
db = client.get_database_by_api_endpoint(
  "https://3aa8de08-63ca-41b8-9840-624ab97f9e12-us-east-2.apps.astra.datastax.com",
    keyspace="phines",
)
      
print(f"Connected to Astra DB: {db.list_collection_names()}")

# cassio.init(token=astra_token, database_id=astra_db_id , keyspace = key_space)



# vectorstore = Cassandra(
# embedding=embeddings,
# table_name= table_name) 
