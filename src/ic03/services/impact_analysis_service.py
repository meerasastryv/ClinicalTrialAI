class ImpactAnalysisService:
    """
    Performs impact analysis using the GraphTraversalService.

    Given any node in the relationship graph, this service determines
    the components that may be affected by a change.
    """

    def __init__(self, traversal_service):
        self.traversal_service = traversal_service

    # ---------------------------------------------------------
    # Core Impact Analysis
    # ---------------------------------------------------------

    def analyze_impact(self, node):
        """
        Returns a complete impact analysis for the specified node.
        """

        affected = self.affected_nodes(node)

        return {
            "node": node,
            "affected_nodes": affected,
            "affected_count": len(affected),
            "impact_score": self.impact_score(node),
            "dependency_depth": self.dependency_depth(node),
        }

    # ---------------------------------------------------------
    # Affected Nodes
    # ---------------------------------------------------------

    def affected_nodes(self, node):
        """
        Returns every node that may be affected by a change.
        """

        return self.traversal_service.reachable_nodes(node)

    def directly_affected_nodes(self, node):
        """
        Returns nodes directly connected to this node.
        """

        return self.traversal_service.get_outgoing_neighbors(node)

    def indirectly_affected_nodes(self, node):
        """
        Returns nodes affected beyond the first level.
        """

        direct = set(
            self.directly_affected_nodes(node)
        )

        all_nodes = set(
            self.affected_nodes(node)
        )

        return sorted(all_nodes - direct)





    # ---------------------------------------------------------
    # Impact Metrics
    # ---------------------------------------------------------

    def impact_score(self, node):
        """
        Calculates a simple impact score based on the number of
        affected nodes.

        Future versions may incorporate weighted scoring.
        """

        return len(self.affected_nodes(node))

    def dependency_depth(self, node):
        """
        Calculates the maximum dependency depth from the given node.

        The depth is approximated using breadth-first traversal.
        """

        reachable = self.traversal_service.reachable_nodes(node)

        if not reachable:
            return 0

        max_depth = 0

        for target in reachable:

            path = self.traversal_service.shortest_path(
                node,
                target
            )

            if path:
                depth = len(path) - 1

                if depth > max_depth:
                    max_depth = depth

        return max_depth

    # ---------------------------------------------------------
    # High Impact Nodes
    # ---------------------------------------------------------

    def critical_nodes(self, minimum_score=10):
        """
        Returns nodes whose impact score exceeds the threshold.
        """

        critical = []

        for node in self.traversal_service.get_nodes():

            score = self.impact_score(node)

            if score >= minimum_score:
                critical.append(
                    {
                        "node": node,
                        "impact_score": score,
                    }
                )

        critical.sort(
            key=lambda item: item["impact_score"],
            reverse=True,
        )

        return critical

    def high_impact_nodes(self, top_n=10):
        """
        Returns the top N highest-impact nodes.
        """

        nodes = []

        for node in self.traversal_service.get_nodes():

            nodes.append(
                {
                    "node": node,
                    "impact_score": self.impact_score(node),
                }
            )

        nodes.sort(
            key=lambda item: item["impact_score"],
            reverse=True,
        )

        return nodes[:top_n]

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def impact_summary(self):
        """
        Returns summary statistics for the impact analysis engine.
        """

        nodes = self.traversal_service.get_nodes()

        if not nodes:
            return {
                "total_nodes": 0,
                "average_impact_score": 0,
                "highest_impact_score": 0,
                "critical_nodes": 0,
            }

        scores = [
            self.impact_score(node)
            for node in nodes
        ]

        average_score = sum(scores) / len(scores)

        return {
            "total_nodes": len(nodes),
            "average_impact_score": round(average_score, 2),
            "highest_impact_score": max(scores),
            "critical_nodes": len(
                self.critical_nodes()
            ),
        }

    # ---------------------------------------------------------
    # Reporting
    # ---------------------------------------------------------

    def print_summary(self):
        """
        Prints a concise summary of the impact analysis.
        """

        summary = self.impact_summary()

        print()
        print("=" * 70)
        print("                IMPACT ANALYSIS SUMMARY")
        print("=" * 70)

        print(f"Total Nodes            : {summary['total_nodes']}")
        print(
            f"Average Impact Score   : "
            f"{summary['average_impact_score']}"
        )
        print(
            f"Highest Impact Score   : "
            f"{summary['highest_impact_score']}"
        )
        print(
            f"Critical Nodes         : "
            f"{summary['critical_nodes']}"
        )

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def node_exists(self, node):
        """
        Returns True if the node exists in the graph.
        """

        return node in self.traversal_service.get_nodes()

    def refresh(self):
        """
        Refreshes the underlying traversal graph.
        """

        self.traversal_service.refresh()
