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
