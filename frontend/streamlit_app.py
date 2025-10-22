import streamlit as st
import requests

st.set_page_config(page_title="AI Study Assistant", page_icon="🧠", layout="centered")

st.title("🧠 AI Study Assistant")
st.write("Upload notes, then chat with them!")

backend_url = "http://127.0.0.1:8000"

# Upload Section
uploaded_file = st.file_uploader("📘 Upload your study material (PDF)", type=["pdf"])
if uploaded_file:
    files = {"file": uploaded_file.getvalue()}
    res = requests.post(f"{backend_url}/docs/upload", files={"file": uploaded_file})
    if res.status_code == 200:
        st.success("Document uploaded & embedded successfully!")

# Chat Section
query = st.text_input("Ask a question about your notes:")
if st.button("Ask") and query:
    res = requests.post(f"{backend_url}/chat/", json={"question": query})
    st.write("**Assistant:** ", res.json()["answer"])
