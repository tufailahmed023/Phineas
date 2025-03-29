from dotenv import load_dotenv
import sys 
import os 

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from DatabaseUpdate.update import vectorindex
load_dotenv()

astra_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
astra_db_id = os.getenv("ASTRA_DB_ID")
pdf_path = ''
table_name = "mission_possiable"
vectorindex_obj = vectorindex(astra_token= astra_token,
                              astra_db_id=astra_db_id,
                              pdf_path= pdf_path
                              table_name=table_name
                              )

vector_index = vectorindex_obj.initiate()