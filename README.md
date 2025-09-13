# PDF Summarizer

A small Streamlit app that summarizes PDF documents using **LangChain**, **HuggingFace embeddings**, **FAISS** vectorstore and a Google generative LLM. This repository contains the Streamlit front-end (`main.py`), helper utilities (`utils.py`), and a flowchart that explains the processing flow.

---

## Features

* Upload a PDF via a simple Streamlit UI.
* Extract text from the PDF (via `pypdf`).
* Split text into overlapping chunks.
* Vectorize chunks using `sentence-transformers/all-MiniLM-L6-v2` embeddings.
* Store embeddings in a FAISS index (in memory in current code).
* Query the vectorstore and generate a concise summary with Google Generative LLM (Gemini).

---

## Flowchart
flowcharts.png

## Repo structure

```
pdf-summarizer/
├─ .gitignore
├─ README.md
├─ requirements.txt
├─ main.py            
├─ utils.py          
├─flowcharts.svg


---

## Quickstart (local)

1. **Clone** the repo (or create it locally) and `cd` into it.

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set the Google API key (required by `langchain-google-genai`):

```bash
export GOOGLE_API_KEY="your_key_here"
```
4. Run the Streamlit app:

```bash
streamlit run main.py
```

Open the URL printed by Streamlit (usually `http://localhost:8501`) and upload a PDF to summarize.


## Recommended `.gitignore`

# Sensitive files
.env

## Environment / secret management

* **Local dev:** use shell environment variables or `python-dotenv` with a `.env` file (don't commit it).
* **Streamlit Cloud / other hosts:** use the provider’s secrets UI.
* **GitHub Actions:** store secrets in repository `Settings → Secrets` and reference them in workflows.

## Notes, caveats & improvements

* **`get_openai_callback()`** is an OpenAI-specific helper (it measures token usage for OpenAI). If you are using the Google generative LLM (`langchain-google-genai`), remove or replace OpenAI-specific callbacks to avoid confusion.
* Building embeddings for very large PDFs can be slow and memory-heavy. Save the FAISS index to disk if you expect to reuse it across runs instead of re-embedding on every upload.
* Scanned PDFs (images) require OCR (Tesseract / OCR service) — `pypdf` won't extract text from images.
* Consider saving the FAISS index with a unique hash for each uploaded file to allow caching.
* Add error handling around network calls and empty/unsupported PDFs.

## Troubleshooting

* **FAISS installation problems (Windows):** prefer `faiss-cpu` wheel or use conda if pip wheel is not available.
* **HuggingFace embeddings require `torch`** (or `tensorflow`). If embeddings fail, install `torch` appropriate for your platform.
* **`langchain-google-genai` errors:** ensure `GOOGLE_API_KEY` is set and your Google Cloud account has the Generative AI API enabled.

## Contributing

PRs welcome — please add issues for bugs and feature requests.

## License

MIT © Yogesh PD
