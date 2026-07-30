from platform.graph.dependency_graph import DependencyGraph


class GraphStatistics:

    def __init__(self, graph: DependencyGraph):

        self.graph = graph

    def summary(self):

        return {
            "modules": self.graph.node_count(),
            "edges": self.graph.edge_count(),
            "internal_imports": self.graph.internal_imports,
            "external_imports": self.graph.external_imports,
            "unresolved_imports": self.graph.unresolved_imports,
        }

    def print_summary(self):

        s = self.summary()

        print("=" * 60)
        print("Graph Statistics")
        print("=" * 60)

        for key, value in s.items():
            print(f"{key:22}: {value}")
