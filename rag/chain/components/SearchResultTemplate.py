class SearchResultTemplate:

    def format(self, documents):
        formatted_result = "Your query appears to be a search request, here are the most relevant documents:\n\n"
        for i, doc in enumerate(documents):
            formatted_result += (
                f"{doc.metadata['title']} \n"
                f"{doc.metadata['source']} \n"
                "\n"
            )
        return formatted_result