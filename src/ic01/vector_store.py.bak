import chromadb
from sentence_transformers import SentenceTransformer

# Create/Open database
client = chromadb.PersistentClient(path="./vector_db")

collection = client.get_or_create_collection(
    name="requirements"
)

# Embedding model
model = SentenceTransformer(
    "all-MiniLM-L6-v2"
)

def store_requirement(req):
    embedding = model.encode(req.text).tolist()

    collection.add(
        ids=[req.id],
        embeddings=[embedding],
        documents=[req.text],
        metadatas=[
            {
                "product": req.product,
                "req_type": req.req_type
            }
        ]
    )
def semantic_search(query, n_results=5):

    query_embedding = model.encode(
        query
    ).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=n_results
    )

    return results

from vector_store import semantic_search


def analyze_impact(changed_requirement):

    print("\nSearching for related requirements...\n")

    results = semantic_search(changed_requirement)

    print("=" * 60)
    print("IMPACT ANALYSIS REPORT")
    print("=" * 60)

    documents = results.get("documents", [[]])[0]

    if not documents:
        print("No related requirements found.")
        return

    print("\nRelated Requirements:")

    for i, doc in enumerate(documents, start=1):
        print(f"\n{i}. {doc}")

    count = len(documents)

    if count >= 5:
        impact = "HIGH"
    elif count >= 3:
        impact = "MEDIUM"
    else:
        impact = "LOW"

    print(f"\nImpact Level: {impact}")

    print("\nRecommended Regression Areas:")

    recommendations = [
        "Functional Testing",
        "Integration Testing",
        "Regression Testing"
    ]

    for item in recommendations:
        print(f"- {item}")


def main():

    print("=" * 60)
    print("IC-01 Milestone 11 - Impact Analysis Engine")
    print("=" * 60)

    changed_requirement = input(
        "\nEnter changed requirement: "
    )

    analyze_impact(changed_requirement)


if __name__ == "__main__":
    main()
