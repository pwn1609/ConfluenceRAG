import pathlib
from langchain.vectorstores import FAISS
from langchain.prompts import ChatPromptTemplate
from langchain.embeddings import OllamaEmbeddings
from langchain_community.chat_models import ChatOllama # ChatOllma chat model
from langchain.schema.runnable import RunnablePassthrough
from langchain.schema.output_parser import StrOutputParser 
import os

class VectorStore:
    def __init__(self, dir):
        self.vectorstore_dir = dir
        self.initialize_vectorstore()
        if self.vectorstore is None:
            print("Failed to initialize the vectorstore. Please check the configuration and try again.")
        self.retriever = self.vectorstore.as_retriever()

    def initialize_vectorstore(self):
        try:
            path = pathlib.Path(self.vectorstore_dir)
            files = path.glob('*') 
            latest_file = max(files, key=os.path.getmtime, default=None)
            embeddings=OllamaEmbeddings(model="llama3.2:3b")
            self.vectorstore = FAISS.load_local(latest_file, embeddings, allow_dangerous_deserialization=True)
        except Exception as e:
            print(f"An error occurred while initializing the vectorstore: {e}")
            self.vectorstore = None
