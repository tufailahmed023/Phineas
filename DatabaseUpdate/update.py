
from dotenv import load_dotenv
import sys 
import os 
import cassio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utilities.utilites import get_pdf_text, get_vectorstore , get_text_chunks , get_embeddings
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
load_dotenv()


class vectorindex():
    def __init__(self,astra_token,astra_db_id,table_name,pdf_path) -> None:

        self.pdf_path = pdf_path
        self.table_name = table_name

        try :
            cassio.init(token=astra_token, database_id=astra_db_id)
        except Exception as e : 
            print(e)

    def initiate(self) :
        texts = get_pdf_text(pdf_path=self.pdf_path)
        texts_chunks = get_text_chunks(text=texts)
        embedding = get_embeddings()
        vector_store = get_vectorstore(text_chunks=texts_chunks,embeddings=embedding,table_name=self.table_name)
        vectorindex = VectorStoreIndexWrapper(vectorstore=vector_store)
        return vectorindex 
    

    



        
