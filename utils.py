from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.llms import google_palm
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.callbacks import get_openai_callback
from pypdf import PdfReader

def process_text(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    knowledge_base = FAISS.from_texts(chunks, embeddings)

    return knowledge_base

def summarizer(pdf):
    if pdf is not None:
        pdf_reader = PdfReader(pdf)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()

        knowledge_base = process_text(text)

        query = "Summarize the content of the document in a concise manner."

        if query:
            docs = knowledge_base.similarity_search(query)

            llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash",temperature=0.2)

            chain = load_qa_chain(llm, chain_type="stuff")

            with get_openai_callback() as cost:
                response = chain.run(input_documents=docs, question=query)

            return response