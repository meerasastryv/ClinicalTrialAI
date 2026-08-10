from collections import Counter


class GraphReport:
    """
    Prints a summary of the Knowledge Graph.
    """

    def __init__(self, graph_service):

        self.graph_service = graph_service

    # ---------------------------------------------------------

    def print_report(self):

        print()
        print("=" * 70)
        print("Knowledge Graph Summary")
        print("=" * 70)

        print()

        print(
            f"Total Nodes : {self.graph_service.node_count()}"
        )

        print(
            f"Total Edges : {self.graph_service.edge_count()}"
        )

        print()

        self.__print_node_types()

        print()

        self.__print_relationship_types()

    # ---------------------------------------------------------

    def __print_node_types(self):

        print("Node Types")
        print("-" * 70)

        counter = Counter()

        for node in self.graph_service.get_all_nodes():

            counter[node.node_type] += 1

        if not counter:

            print("No nodes available.")
            return

        for node_type in sorted(counter):

            print(
                f"{node_type:25}"
                f"{counter[node_type]}"
            )

    # ---------------------------------------------------------

    def __print_relationship_types(self):

        print("Relationship Types")
        print("-" * 70)

        counter = Counter()

        for edge in self.graph_service.get_all_edges():

            counter[edge.relationship] += 1

        if not counter:

            print("No relationships available.")
            return

        for relationship in sorted(counter):

            print(
                f"{relationship:25}"
                f"{counter[relationship]}"
            )
