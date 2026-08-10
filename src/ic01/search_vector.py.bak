#from vector_store import semantic_search

#results = semantic_search(
#    "clinical data repository"
#)

#print("\nRESULT IDS")
#print("=" * 50)

#for req_id in results["ids"][0]:
#    print(req_id)

from vector_store import semantic_search

results = semantic_search(
    "clinical data repository"
)

for i in range(len(results["ids"][0])):

    print("\nID:")
    print(results["ids"][0][i])

    print("\nTEXT:")
    print(results["documents"][0][i])

    print("\n" + "=" * 60)
