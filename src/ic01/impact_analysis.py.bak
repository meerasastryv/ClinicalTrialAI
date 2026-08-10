# src/ic01/impact_analysis.py

# from vector_store import search_requirements

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

    impact_count = len(documents)

    if impact_count >= 5:
        impact_level = "HIGH"
    elif impact_count >= 3:
        impact_level = "MEDIUM"
    else:
        impact_level = "LOW"

    print(f"\nImpact Level: {impact_level}")

    print("\nRecommended Regression Testing:")
    print("- Functional Testing")
    print("- Integration Testing")
    print("- Regression Testing")

#def analyze_impact(changed_requirement):

#    print("\nSearching for related requirements...\n")

   # results = search_requirements(changed_requirement)


#    results = semantic_search(changed_requirement)

#    print("Related Requirements:")
 #   print("-" * 40)
 #   documents = results["documents"][0]

 #   for i, doc in enumerate(documents, start=1):
 #       print(f"\n{i}. {doc}")


    #print("Related Requirements:")
    # print("-" * 40)


    # for result in results:
     #    print(result)

#    print("\nImpact Level: MEDIUM")

 #   print("\nRecommended Regression Testing:")
 #    print("- Functional Testing")
 #   print("- Integration Testing")


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
