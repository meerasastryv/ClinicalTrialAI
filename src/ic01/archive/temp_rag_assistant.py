"""
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

def get_vector_db():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="data/chroma_db",
        embedding_function=embeddings
    )

    return db

def retrieve_context(question, k=5):

    db = get_vector_db()

    docs = db.similarity_search(
        question,
        k=k
    )

    return docs

def build_prompt(question, docs):

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""

"""
You are a Clinical Trial Requirement Assistant.

Use only the provided requirements.

Requirements:
{context}

Question:
{question}

Answer:
"""
"""
    return prompt 

"""

from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
import ollama


def get_vector_db():

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    db = Chroma(
        persist_directory="data/chroma_db",
        embedding_function=embeddings
    )

    return db


def retrieve_context(question, k=5):

    db = get_vector_db()

    docs = db.similarity_search(
        question,
        k=k
    )

    return docs


def build_prompt(question, docs):

    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )

    prompt = f"""
You are a Clinical Trial Requirement Assistant.

Answer ONLY from the provided requirements.

Requirements:
{context}

Question:
{question}

Answer:
"""

    return prompt


def ask_llm(prompt):

    response = ollama.chat(
        model="llama3:8b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response["message"]["content"]


def ask_requirement_assistant(question):

    docs = retrieve_context(question)

    print("\nRetrieved Requirements:")
    print("-" * 50)

    for i, doc in enumerate(docs, start=1):
        print(f"\nDocument {i}")
        print(doc.page_content[:200])

    prompt = build_prompt(
        question,
        docs
    )

    answer = ask_llm(prompt)

    return answer


if __name__ == "__main__":

    while True:

        question = input("\nAsk Question: ")

        if question.lower() == "exit":
            break

        answer = ask_requirement_assistant(question)

        print("\nAnswer:")
        print(answer)
