import streamlit as st
import requests

st.set_page_config(page_title="Multilingual RAG Assistant", layout="wide")

st.title("📄 Multilingual PDF RAG Assistant")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])
language = st.selectbox("Select Language", ["english", "hindi"])
audio_option = st.checkbox("Enable Audio Response")

if uploaded_file:
    files = {"file": uploaded_file}
    response = requests.post("http://localhost:8000/upload/", files=files)

    if response.status_code == 200:
        collection = uploaded_file.name.replace(" ", "_").replace(".pdf", "")

        st.success("File uploaded and processed!")

        question = st.text_input("Ask a question")

        if st.button("Submit"):
            res = requests.post(
                "http://localhost:8000/ask/",
                params={
                    "collection_name": collection,
                    "question": question,
                    "language": language,
                    "audio": audio_option
                }
            )

            result = res.json()

            st.write("### Answer")
            st.write(result["answer"])

            if audio_option and result["audio"]:
                audio_file = open(result["audio"], "rb")
                st.audio(audio_file.read())
