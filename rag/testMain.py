from chain.RAGDriver import RAGDriver


rag = RAGDriver()
if not hasattr(rag, 'vectorstore'):
    raise AttributeError("The RAGChain instance does not have a 'vectorstore' attribute.")
user_query = "What is the best way to get started on confluence"

print(rag.query(user_query))
