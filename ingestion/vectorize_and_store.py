from langchain.vectorstores import FAISS
from langchain.embeddings import OllamaEmbeddings
import datetime

class Vectorize:

    def vectorize_text(self, documents, path):
        self.vectorstore = FAISS.from_documents(
        documents=documents,
        embedding=OllamaEmbeddings(model="llama3.2:3b")
        )
        return self.store_vector(path)

    def store_vector(self, path):
        current_time = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"vectorstore_{current_time}"
        path = f"{path}{filename}"
        self.vectorstore.save_local(path)
        return True
        