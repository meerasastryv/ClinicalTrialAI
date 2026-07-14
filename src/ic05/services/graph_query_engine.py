"""
Graph Query Engine
IC-05 - Knowledge Graph Engine
Milestone 10
"""

from collections import Counter, deque

from src.ic05.models.graph_statistics import GraphStatistics


class GraphQueryEngine:
    """
    Provides query operations on the Knowledge Graph.
    """

    def __init__(self, repository):
        self.repository = repository
        self.graph = repository.get_graph()

    # ---------------------------------------------------------

    def find_node(self, node_id):
        """
        Find a node by ID.
        """
        return self.graph.get_node(node_id)

    # ---------------------------------------------------------

    def find_neighbors(self, node_id):
        """
        Return neighbouring nodes.
        """
        return self.graph.get_neighbors(node_id)

    # ---------------------------------------------------------

    def find_outgoing(self, node_id):
        """
        Return outgoing edges.
        """
        return self.graph.get_outgoing_edges(node_id)

    # ---------------------------------------------------------

    def find_incoming(self, node_id):
        """
        Return incoming edges.
        """
        return self.graph.get_incoming_edges(node_id)

    # ---------------------------------------------------------

    def find_relationships(self, relationship_type=None):
        """
        Return graph relationships.

        If relationship_type is supplied,
        only matching relationships are returned.
        """

        edges = self.graph.get_all_edges()

        if relationship_type is None:
            return edges

        return [
            edge
            for edge in edges
            if edge.relationship == relationship_type
        ]

    # ---------------------------------------------------------

    def find_nodes_by_type(self, node_type):
        """
        Find nodes of a specific type.
        """
        return self.graph.find_nodes_by_type(node_type)

    # ---------------------------------------------------------

    def shortest_path(self, start_node, end_node):
        """
        Breadth First Search shortest path.
        """

        if start_node == end_node:
            return [start_node]

        visited = set()

        queue = deque()

        queue.append((start_node, [start_node]))

        while queue:

            current, path = queue.popleft()

            if current in visited:
                continue

            visited.add(current)

            for edge in self.graph.get_outgoing_edges(current):

                target = edge.target

                if target == end_node:
                    return path + [target]

                queue.append((target, path + [target]))

        return []

    # ---------------------------------------------------------

    def dependency_chain(self, node_id):
        """
        Return all reachable nodes.
        """

        visited = set()

        chain = []

        queue = deque([node_id])

        while queue:

            current = queue.popleft()

            if current in visited:
                continue

            visited.add(current)

            if current != node_id:
                chain.append(current)

            for edge in self.graph.get_outgoing_edges(current):
                queue.append(edge.target)

        return chain

    # ---------------------------------------------------------

    def graph_statistics(self):
        """
        Compute graph statistics.
        """

        nodes = self.graph.get_all_nodes()

        edges = self.graph.get_all_edges()

        node_counter = Counter()

        relationship_counter = Counter()

        isolated = 0

        for node in nodes:

            node_counter[node.node_type] += 1

            degree = (
                len(self.graph.get_outgoing_edges(node.node_id))
                +
                len(self.graph.get_incoming_edges(node.node_id))
            )

            if degree == 0:
                isolated += 1

        for edge in edges:
            relationship_counter[edge.relationship] += 1

        average_degree = 0.0

        if nodes:
            average_degree = (2 * len(edges)) / len(nodes)

        return GraphStatistics(
            total_nodes=len(nodes),
            total_edges=len(edges),
            node_types=dict(node_counter),
            relationship_types=dict(relationship_counter),
            average_degree=average_degree,
            isolated_nodes=isolated
        )

    # ---------------------------------------------------------

    def node_exists(self, node_id):
        """
        Check whether a node exists.
        """
        return self.find_node(node_id) is not None

    # ---------------------------------------------------------

    def relationship_exists(
        self,
        source,
        target,
        relationship
    ):
        """
        Check whether a relationship exists.
        """

        for edge in self.graph.get_outgoing_edges(source):

            if (
                edge.target == target
                and
                edge.relationship == relationship
            ):
                return True

        return False
