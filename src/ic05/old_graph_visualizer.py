"""
Knowledge Graph Visualizer
IC-05 – Knowledge Graph Engine
Milestone 12
"""


class GraphVisualizer:
    """
    Generates human-readable views of the Knowledge Graph.
    """

    def __init__(self, repository):
        self.graph = repository.get_graph()

    # ---------------------------------------------------------

    def visualize(self):
        """
        Returns a complete textual representation of the graph.
        """
        lines = []

        lines.append("Knowledge Graph")
        lines.append("=" * 70)

        for node in sorted(
            self.graph.get_all_nodes(),
            key=lambda n: n.node_id
        ):

            lines.append(
                f"{node.node_id} [{node.node_type}] {node.name}"
            )

            edges = self.graph.get_outgoing_edges(node.node_id)

            for edge in edges:
                lines.append(
                    f"   └── {edge.relationship} → {edge.target}"
                )

            lines.append("")

        return "\n".join(lines)

    # ---------------------------------------------------------

    def visualize_node(self, node_id):
        """
        Returns the neighborhood of a single node.
        """

        node = self.graph.get_node(node_id)

        if node is None:
            return f"Node '{node_id}' not found."

        lines = [
            f"{node.node_id} [{node.node_type}] {node.name}"
        ]

        edges = self.graph.get_outgoing_edges(node.node_id)

        for edge in edges:
            lines.append(
                f"   └── {edge.relationship} → {edge.target}"
            )

        return "\n".join(lines)
