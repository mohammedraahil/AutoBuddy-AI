from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS


# Load knowledge base

loader = TextLoader("knowledge.txt")

documents = loader.load()


# Split documents

splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)


chunks = splitter.split_documents(documents)



# Create embeddings

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)



# Create vector database

db = FAISS.from_documents(
    chunks,
    embeddings
)



# Function used by diagnose.py

def retrieve_context(query):

    results = db.similarity_search(
        query,
        k=3
    )


    context = ""


    for doc in results:
        context += doc.page_content + "\n\n"


    return context