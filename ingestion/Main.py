from data_retriever import DataRetriever
from vectorize_and_store import Vectorize
from dotenv import load_dotenv
import os



def main():
    load_dotenv()

    # Initialize DataRetriever with .env variables
    api_key = os.getenv('API_TOKEN')
    confluence_url = os.getenv('CONFLUENCE_URL')
    confluence_username = os.getenv('CONFLUENCE_USERNAME')
    confluence_space_key = os.getenv('CONFLUENCE_SPACE')
    data_retriever = DataRetriever(api_key, confluence_url, confluence_username, confluence_space_key)

    # Retrieve data
    data = data_retriever.retrieve_data()

    # Initialize Vectorize and store data
    vectorizer = Vectorize()
    vectorizer.vectorize_text(data, "vectorStores\\")

if __name__ == "__main__":
    main()