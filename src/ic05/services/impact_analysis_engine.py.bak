"""
Impact Analysis Engine
IC-05 – Knowledge Graph Engine
Milestone 11
"""

from collections import deque

from src.ic05.models.impact_result import ImpactResult


class ImpactAnalysisEngine:
    """
    Performs impact analysis on the Knowledge Graph.
    """

    def __init__(self, repository):
        self.repository = repository
        self.graph = repository.get_graph()

    # ---------------------------------------------------------

    def analyze(self, source_node):
        """
        Perform complete impact analysis.
        """

        result = ImpactResult(source_node=source_node)

        source = self.graph.get_node(source_node)

        if source is None:
            return result

        visited = set()

        queue = deque()

        #
        # Start traversal from the source node.
        #
        queue.append((source_node, 0))

        while queue:

            current_node, depth = queue.popleft()

            if current_node in visited:
                continue

            visited.add(current_node)

            current = self.graph.get_node(current_node)

            if current is None:
                continue

            if current_node != source_node:
                result.impacted_nodes.append(current_node)

            result.dependency_depth = max(
                result.dependency_depth,
                depth
            )

            #
            # Determine traversal direction.
            #
            if current.node_type == "Requirement":

                #
                # Requirement is implemented by Method.
                # Traverse incoming IMPLEMENTS edges first.
                #
                edges = self.graph.get_incoming_edges(current_node)

                next_nodes = [
                    edge.source
                    for edge in edges
                ]

            else:

                #
                # Default traversal.
                #
                edges = self.graph.get_outgoing_edges(current_node)

                next_nodes = [
                    edge.target
                    for edge in edges
                ]

            #
            # Process neighbours.
            #
            for next_node in next_nodes:

                if next_node in visited:
                    continue

                if depth == 0:
                    if next_node not in result.direct_dependencies:
                        result.direct_dependencies.append(next_node)
                else:
                    if next_node not in result.indirect_dependencies:
                        result.indirect_dependencies.append(next_node)

                node = self.graph.get_node(next_node)

                if node:

                    if node.node_type == "Requirement":
                        if node.node_id not in result.impacted_requirements:
                            result.impacted_requirements.append(node.node_id)

                    elif node.node_type == "Class":
                        if node.node_id not in result.impacted_classes:
                            result.impacted_classes.append(node.node_id)

                    elif node.node_type == "Method":
                        if node.node_id not in result.impacted_methods:
                            result.impacted_methods.append(node.node_id)

                    elif node.node_type == "API":
                        if node.node_id not in result.impacted_apis:
                            result.impacted_apis.append(node.node_id)

                    elif node.node_type == "Database":
                        if node.node_id not in result.impacted_databases:
                            result.impacted_databases.append(node.node_id)

                queue.append(
                    (
                        next_node,
                        depth + 1
                    )
                )

        self._calculate_score(result)

        return result

    # ---------------------------------------------------------

    def _calculate_score(self, result):
        """
        Compute impact score and blast radius.
        """

        score = (
            len(result.impacted_nodes)
            + (2 * len(result.direct_dependencies))
            + len(result.indirect_dependencies)
            + (3 * result.dependency_depth)
        )

        result.impact_score = float(score)

        if score >= 25:
            result.blast_radius = "HIGH"
        elif score >= 10:
            result.blast_radius = "MEDIUM"
        else:
            result.blast_radius = "LOW"

    # ---------------------------------------------------------

    def impacted_requirements(self, source_node):
        return self.analyze(source_node).impacted_requirements

    # ---------------------------------------------------------

    def impacted_classes(self, source_node):
        return self.analyze(source_node).impacted_classes

    # ---------------------------------------------------------

    def impacted_methods(self, source_node):
        return self.analyze(source_node).impacted_methods

    # ---------------------------------------------------------

    def impacted_apis(self, source_node):
        return self.analyze(source_node).impacted_apis

    # ---------------------------------------------------------

    def impacted_databases(self, source_node):
        return self.analyze(source_node).impacted_databases

    # ---------------------------------------------------------

    def dependency_depth(self, source_node):
        return self.analyze(source_node).dependency_depth

    # ---------------------------------------------------------

    def blast_radius(self, source_node):
        return self.analyze(source_node).blast_radius

    # ---------------------------------------------------------

    def impact_score(self, source_node):
        return self.analyze(source_node).impact_score
