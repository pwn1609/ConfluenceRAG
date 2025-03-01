class Context:

    def format(self, docs):
        return "\n\n".join([f"Document {i+1}:\nTitle: {doc.metadata['title']} \nURL: {doc.metadata['source']} \nContent: {doc.page_content}" 
                            for i, doc in enumerate(docs)])