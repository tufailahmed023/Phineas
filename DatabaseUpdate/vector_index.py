from dotenv import load_dotenv
import sys 
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from DatabaseUpdate.update import VectorIndex
load_dotenv()

astra_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
astra_db_id = os.getenv("ASTRA_DB_ID")
key_space = os.getenv("ASTRA_KEYSPACE")

pdf_path = '/Users/tufailahmed/Desktop/PDFs'
table_name = "mission_possiable"
vectorindex_obj = VectorIndex(astra_token= astra_token,
                              astra_db_id=astra_db_id,
                              pdf_path= pdf_path,
                              table_name=table_name,
                              key_space=key_space
                              )

vector_index = vectorindex_obj.initiate()