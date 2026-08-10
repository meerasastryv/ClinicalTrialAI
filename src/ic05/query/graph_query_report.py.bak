class GraphQueryReport:
    """
    Reporting utility for Graph Query Engine.
    """

    # ---------------------------------------------------------

    @staticmethod
    def print_neighbors(node_id, neighbors):

        print()
        print("=" * 70)
        print("GRAPH NEIGHBORS")
        print("=" * 70)

        print(f"Node : {node_id}")
        print()

        if not neighbors:
            print("No neighbors found.")
            return

        for node in neighbors:
            print(
                f"{node.node_id:15}"
                f"{node.node_type:18}"
                f"{node.name}"
            )

    # ---------------------------------------------------------

    @staticmethod
    def print_path(path):

        print()
        print("=" * 70)
        print("GRAPH PATH")
        print("=" * 70)

        if not path:
            print("No path found.")
            return

        for i, node in enumerate(path):

            if i > 0:
                print("   |")
                print("   V")

            print(
                f"{node.node_id}"
                f" ({node.node_type}) "
                f"{node.name}"
            )

    # ---------------------------------------------------------

    @staticmethod
    def print_search(title, nodes):

        print()
        print("=" * 70)
        print(title)
        print("=" * 70)

        if not nodes:
            print("No matching nodes.")
            return

        for node in nodes:

            print(
                f"{node.node_id:15}"
                f"{node.node_type:18}"
                f"{node.name}"
            )

    # ---------------------------------------------------------

    @staticmethod
    def print_connected(nodes):

        print()
        print("=" * 70)
        print("CONNECTED COMPONENT")
        print("=" * 70)

        if not nodes:
            print("No connected nodes.")
            return

        for node in nodes:

            print(
                f"{node.node_id:15}"
                f"{node.node_type:18}"
                f"{node.name}"
            )
