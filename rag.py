from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
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


    results = db.similarity_search_with_score(
        query,
        k=3
    )


    context = ""

    scores = []


    for doc, score in results:

        context += doc.page_content + "\n\n"

        scores.append(score)



    average_score = sum(scores) / len(scores)



    # Convert distance into confidence

    confidence = int(
    100 / (1 + average_score)
    )


    return context, confidence