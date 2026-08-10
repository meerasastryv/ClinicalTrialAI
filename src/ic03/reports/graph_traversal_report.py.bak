class GraphTraversalReport:
    """
    Prints summary information for the Graph Traversal Engine.
    """

    def __init__(self, traversal_service):
        self.traversal_service = traversal_service

    def print_report(self):
        print()
        print("=" * 70)
        print("                 GRAPH TRAVERSAL REPORT")
        print("=" * 70)

        stats = self.traversal_service.graph_statistics()

        print()
        print("Graph Statistics")
        print("-" * 70)
        print(f"Total Nodes      : {stats['nodes']}")
        print(f"Total Edges      : {stats['edges']}")
        print(f"Root Nodes       : {stats['root_nodes']}")
        print(f"Leaf Nodes       : {stats['leaf_nodes']}")
        print(f"Isolated Nodes   : {stats['isolated_nodes']}")

        print()
        print("Sample Traversal")
        print("-" * 70)

        nodes = self.traversal_service.get_nodes()

        if not nodes:
            print("Graph is empty.")
            return

        start = nodes[0]

        print(f"Start Node       : {start}")

        bfs = self.traversal_service.breadth_first_search(start)
        dfs = self.traversal_service.depth_first_search(start)

        print()
        print("Breadth First Search")
        for node in bfs[:15]:
            print(f"  {node}")

        if len(bfs) > 15:
            print(f"  ... ({len(bfs)} nodes)")

        print()
        print("Depth First Search")
        for node in dfs[:15]:
            print(f"  {node}")

        if len(dfs) > 15:
            print(f"  ... ({len(dfs)} nodes)")

        print()
        print("=" * 70)
