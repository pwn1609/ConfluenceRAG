from .components.VectorStore import VectorStore
from .components.Prompt import Prompt
from .components.Context import Context
from .components.Model import Model
from .components.UserQuery import UserQuery
from .components.SearchResultTemplate import SearchResultTemplate

class RAGDriver:

    def __init__(self):

        self.vectorstore = VectorStore("C:\\Data\\Code\\ConfluenceRAG\\ingestion\\vectorstores")
        self.prompt = Prompt()
        self.llm = Model("llama3.2:3b", {"temperature": 0.3})

    def query(self, question):
        question = UserQuery(question)
        response = self.process_query(question)
        return response

    def process_query(self, query):        
        # Retrieve relevant documents
        retrieved_docs = self.vectorstore.retriever.get_relevant_documents(query.query)

        if query.is_search_query:
            # Format search results into a response
            response = SearchResultTemplate().format(retrieved_docs)
            return response
        
        # Format context from documents
        context = Context().format(retrieved_docs)

        # Generate response
        response = self.llm.query(self.prompt.format(context=context, input=query.query)).content
        return response

