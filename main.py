import streamlit as st
import os
from utils import * 

def main():
    st.set_page_config(page_title="PDF Summarizer", layout="wide")
    st.title("PDF Summarizer App")
    st.write("Summarize the content of your PDF documents easily.")
    st.divider()

    pdf_file = st.file_uploader("Upload PDF", type=["pdf"])

    submit = st.button("Summarize")

    google_api_key = os.getenv("GOOGLE_API_KEY")

    if submit and pdf_file is not None:
        response = summarizer(pdf_file)
        st.subheader("Summary")
        st.write(response)
    
if __name__ == '__main__':
    main()