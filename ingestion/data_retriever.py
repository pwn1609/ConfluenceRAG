from langchain_community.document_loaders import ConfluenceLoader


class DataRetriever:

    def __init__(self, api_key, confluence_url, confluence_username, confluence_space_key):
        self.api_key = api_key
        self.confluence_url = confluence_url
        self.confluence_username = confluence_username
        self.confluence_space_key = confluence_space_key

    def retrieve_data(self):

        if not self.api_key or not self.confluence_url or not self.confluence_username or not self.confluence_space_key:
            print("Missing Variables")
            return

        # Initialize the Confluence document loader
        loader = ConfluenceLoader(
            url=self.confluence_url,
            api_key=self.api_key,
            username=self.confluence_username,
            space_key=self.confluence_space_key,
        )

        return loader.load()