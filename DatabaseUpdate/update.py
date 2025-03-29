# from utilities.utilites import get_pdf_text, get_vectorstore , get_text_chunks 
from dotenv import load_dotenv
import os 
import cassio
load_dotenv()
astra_token = os.getenv("ASTRA_DB_APPLICATION_TOKEN")
print(astra_token)
class vectorindex():
    def __init__(self) -> None:
        try :
            # cassio.init(token=ASTRA_DB_APPLICATION_TOKEN, database_id=ASTRA_DB_ID)
            print(ASTRA_DB_APPLICATION_TOKEN)
        except Exception as e : 
            print(e)

        
