import streamlit as st
from chain.RAGDriver import RAGDriver

#TODO:Edit the ingenestion pipeline to use an observer to update the vector database, it runs on a schedule and when it identifies a new document it adds it to the database

st.title("RAG-Powered Knowledge Assistant")
st.write("Retrieve insights from Confluence documents")

rag = RAGDriver()
user_query = st.text_input("Enter your question:", "")

if st.button("Search") and user_query:
    with st.spinner("Fetching response..."):
        response = rag.query(user_query)
    st.subheader("Response:")
    st.write(response)
