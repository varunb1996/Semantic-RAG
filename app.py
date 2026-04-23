import streamlit as st
import requests

st.title("🧠 Semantic RAG Assistant")

query = st.text_input("Ask something:")

if st.button("Search"):
    res = requests.get(f"http://127.0.0.1:8000/query?q={query}")
    st.write(res.json()["response"])