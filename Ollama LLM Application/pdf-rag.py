## Things to do
# 1. Ingest PDF Files
# 2. Extract text from PDF files and split into small chunks
# 3. Send the chunks to the embedding model
# 4. Save the embeddings to a vector database
# 5. Perform similarity serrch on the vector database to find similarities
# 6. Retrieve the similar documents and present them to the user
## pip install -r requirements.txt

from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain_community.document_loaders import OnlinePDFLoader

doc_path = "./data/BOI.pdf"
model = "llama3.2"

# Local pdf file uploads
if doc_path: 
    loader = UnstructuredPDFLoader(file_path=doc_path)
    data = loader.load()
    print("done loading....")
else:
    print("Upload a pdf file")

# Preview the first page
content = data[0].page_content
print(content[:100])

# Pdf ingestion done

# extract text from pdf files and split into small chunks

from langchain_ollama import OllamaEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma

# Split and chunk
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1200, chunk_overlap=300)
chunks = text_splitter.split_documents(data)
print("done splitting")

# print(f"Number of chunks: {len(chunks)}")
# print(f"Example chunk: {chunks[0]}")

# Adding to the vector database

import ollama
ollama.pull("nomic-embed-text")

# create a vector database
vector_db = Chroma.from_documents(
    documents=chunks, 
    embedding=OllamaEmbeddings(model="nomic-embed-text"),
    collection_name="simple-rag"
)
print("done adding to the vector database.....")

# Retrieval

from langchain.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser

from langchain_ollama import ChatOllama

from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_query import MultiQueryRetriever

# set up out moedel to use
llm = ChatOllama(model=model)


# a simple technique to generate multiple questions form a single prompt and then retrieve document
# based on thse questions, getting the best of both worlds

QUERY_PROMPT = PromptTemplate(
    input_variables=["question"],
    template="""You are an AI language model assistant. Your task is to genetrate five
    different versions of the given user question to retrieve relevant document from
    a vector database. By generating miltiple perspectives on the user question, your
    goal is to help the user overcome some of the limitations of the distance-based
    similarity search. Provide these alternative questions seperated by newlines.
Original question: {question}""",
)

retriever = MultiQueryRetriever.from_llm(
    vector_db.as_retriever(), llm, prompt=QUERY_PROMPT
)

# RAG prompt
template = """Answer the question based ONLY on the following context:
{context}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)

chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

res = chain.invoke(input=("what is the document about?",))

res2 = chain.invoke(
    input=("what are the main points as a business owner I should be aware of?",)
)

res3 = chain.invoke(input=("how to report BOI?",))

print("res")
print(res)
print("\n")
print("res2")
print(res2)
print("\n")
print("res3")
print(res3)