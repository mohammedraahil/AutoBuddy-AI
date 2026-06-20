from langchain_community.document_loaders import TextLoader

from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain_community.embeddings import HuggingFaceEmbeddings

from langchain_community.vectorstores import FAISS



loader = TextLoader("knowledge.txt")

documents = loader.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=300,
    chunk_overlap=50
)


chunks = splitter.split_documents(documents)



embeddings = HuggingFaceEmbeddings(
model_name="sentence-transformers/all-MiniLM-L6-v2"
)



db = FAISS.from_documents(
chunks,
embeddings
)



query="Engine temperature increases after driving"


results=db.similarity_search(query,k=2)


for r in results:
    print("----------------")
    print(r.page_content)