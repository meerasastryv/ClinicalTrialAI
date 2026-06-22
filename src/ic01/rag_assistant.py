import chromadb
from sentence_transformers import SentenceTransformer
import ollama

# Connect to ChromaDB

client = chromadb.PersistentClient(
    path="./vector_db"
)

collection = client.get_collection(
    name="requirements"
)

# Embedding model

model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)


def retrieve_context(question, n_results=5):

    query_embedding = model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results


def build_context(results):

    docs = results["documents"][0]

    return "\n\n".join(docs)

def ask_llm(question, context):

    prompt = f"""
You are a Clinical Trial Requirement Assistant.

Use ONLY the provided requirements.

If the answer cannot be found in the supplied requirements,
respond exactly with:

Information not available in the current requirement repository.

Do not use external knowledge.
Do not guess.
Do not infer missing information.
Do not provide general advice.

Requirements:
{context}

Question:
{question}

Answer:
"""

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

    results = retrieve_context(question)

    print("\nRetrieved Requirements")
    print("=" * 60)

    for i in range(len(results["ids"][0])):

        print(f"\nRequirement ID: {results['ids'][0][i]}")
        print(results["documents"][0][i][:200])

    context = build_context(results)

    answer = ask_llm(
        question,
        context
    )

    return answer


if __name__ == "__main__":

    while True:

        question = input("\nAsk Question: ")

        if question.lower() == "exit":
            break

        answer = ask_requirement_assistant(
            question
        )

        print("\nAnswer")
        print("=" * 60)
        print(answer)
