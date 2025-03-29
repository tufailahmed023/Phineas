
from dotenv import load_dotenv
import sys 
import os 
import cassio
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from utilities.utilites import get_pdf_text, get_vectorstore , get_text_chunks , get_embeddings
from langchain.indexes.vectorstore import VectorStoreIndexWrapper
load_dotenv()


class VectorIndex:
    def __init__(self, astra_token, astra_db_id, table_name, key_space, pdf_path) -> None:
        self.pdf_path = pdf_path
        self.table_name = table_name
        self.key_space = key_space
        self.session = None  # Initialize self.session

        try:
            # Initialize Cassio
            cassio.init(token=astra_token, database_id=astra_db_id)
            self.session = cassio.get_session()  

            if self.session is None:
                raise ValueError("Failed to retrieve Cassandra session. Check your Astra DB credentials.")

            cassio.set_session(self.session)

        except Exception as e:
            print(f"Error initializing Cassandra session: {e}")

    def initiate(self):
        # if self.session is None:
        #     print("Error: Cassandra session not initialized.")
        #     return None  # Prevent further execution if session is not set

        texts = get_pdf_text(pdf_path=self.pdf_path)
        texts_chunks = get_text_chunks(text=texts)
        embedding = get_embeddings()
        
        vector_store = get_vectorstore(
            text_chunks= texts_chunks,
            embeddings=embedding,
             
        )

        # vector_index = VectorStoreIndexWrapper(vectorstore=vector_store)
        return vector_store

    

    



        
