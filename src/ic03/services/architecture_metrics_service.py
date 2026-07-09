

class ArchitectureMetricsService:
    """
    Computes architecture-level metrics from the relationship graph.
    """

    def __init__(self, graph_traversal_service):

        self.graph = graph_traversal_service

    # ---------------------------------------------------------
    # Basic Metrics
    # ---------------------------------------------------------

    def get_node_count(self):
        """
        Total number of unique nodes.
        """

        return self.graph.node_count()

    def get_edge_count(self):
        """
        Total number of relationships.
        """

        return self.graph.edge_count()

    # ---------------------------------------------------------
    # Fan-Out
    # ---------------------------------------------------------

    def get_fan_out(self, node):
        """
        Number of outgoing relationships.
        """

        return self.graph.out_degree(node)

    # ---------------------------------------------------------
    # Fan-In
    # ---------------------------------------------------------

    def get_fan_in(self, node):
        """
        Number of incoming relationships.
        """

        return self.graph.in_degree(node)

    # ---------------------------------------------------------
    # Average Metrics
    # ---------------------------------------------------------

    def average_fan_out(self):

        nodes = self.graph.get_nodes()

        if not nodes:
            return 0.0

        total = sum(
            self.get_fan_out(node)
            for node in nodes
        )

        return round(total / len(nodes), 2)

    def average_fan_in(self):

        nodes = self.graph.get_nodes()

        if not nodes:
            return 0.0

        total = sum(
            self.get_fan_in(node)
            for node in nodes
        )

        return round(total / len(nodes), 2)


    # ---------------------------------------------------------
    # Top Fan-Out
    # ---------------------------------------------------------

    def top_fan_out(self, top_n=10):
        """
        Returns the nodes with the highest fan-out.
        """

        nodes = self.graph.get_nodes()

        results = [
            (node, self.get_fan_out(node))
            for node in nodes
        ]

        results.sort(
            key=lambda item: item[1],
            reverse=True
        )

        return results[:top_n]

    # ---------------------------------------------------------
    # Top Fan-In
    # ---------------------------------------------------------

    def top_fan_in(self, top_n=10):
        """
        Returns the nodes with the highest fan-in.
        """

        nodes = self.graph.get_nodes()

        results = [
            (node, self.get_fan_in(node))
            for node in nodes
        ]

        results.sort(
            key=lambda item: item[1],
            reverse=True
        )

        return results[:top_n]

    # ---------------------------------------------------------
    # Architecture Hotspots
    # ---------------------------------------------------------

    def hotspots(self, threshold=5):
        """
        Returns nodes with high architectural connectivity.
        """

        nodes = self.graph.get_nodes()

        hotspots = []

        for node in nodes:

            fan_in = self.get_fan_in(node)
            fan_out = self.get_fan_out(node)

            if fan_in >= threshold or fan_out >= threshold:

                hotspots.append(
                    (
                        node,
                        fan_in,
                        fan_out
                    )
                )

        hotspots.sort(
            key=lambda item: (
                item[1] + item[2],
                item[1]
            ),
            reverse=True
        )

        return hotspots

    # ---------------------------------------------------------
    # Architecture Health
    # ---------------------------------------------------------

    def health_score(self):
        """
        Computes a simple architecture health score.
        """

        hotspots = len(self.hotspots())

        score = max(
            0,
            100 - hotspots
        )

        return score

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def summary(self):
        """
        Returns architecture summary statistics.
        """

        return {
            "nodes": self.get_node_count(),
            "edges": self.get_edge_count(),
            "average_fan_in": self.average_fan_in(),
            "average_fan_out": self.average_fan_out(),
            "health_score": self.health_score(),
            "hotspots": len(self.hotspots())
        }
