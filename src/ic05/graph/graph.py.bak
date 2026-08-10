from collections import defaultdict

from src.ic05.graph.node import Node
from src.ic05.graph.edge import Edge


class KnowledgeGraph:
    """
    In-memory Knowledge Graph.
    """

    def __init__(self):

        self.nodes = []

        self.edges = []

        self.node_lookup = {}

        self.outgoing_edges = defaultdict(list)

        self.incoming_edges = defaultdict(list)

    # ---------------------------------------------------------

    def add_node(self, node: Node):

        if node.node_id in self.node_lookup:
            return

        self.nodes.append(node)

        self.node_lookup[node.node_id] = node

    # ---------------------------------------------------------

    def add_edge(self, edge: Edge):

        self.edges.append(edge)

        self.outgoing_edges[edge.source].append(edge)

        self.incoming_edges[edge.target].append(edge)

    # ---------------------------------------------------------

    def get_node(self, node_id):

        return self.node_lookup.get(node_id)

    # ---------------------------------------------------------

    def get_all_nodes(self):

        return self.nodes

    # ---------------------------------------------------------

    def get_all_edges(self):

        return self.edges

    # ---------------------------------------------------------

    def get_outgoing_edges(self, node_id):

        return self.outgoing_edges.get(node_id, [])

    # ---------------------------------------------------------

    def get_incoming_edges(self, node_id):

        return self.incoming_edges.get(node_id, [])

    # ---------------------------------------------------------

    def get_neighbors(self, node_id):

        neighbors = []

        for edge in self.get_outgoing_edges(node_id):

            node = self.get_node(edge.target)

            if node:
                neighbors.append(node)

        return neighbors

    # ---------------------------------------------------------

    def find_nodes_by_type(self, node_type):

        return [
            node
            for node in self.nodes
            if node.node_type == node_type
        ]

    # ---------------------------------------------------------

    def node_count(self):

        return len(self.nodes)

    # ---------------------------------------------------------

    def edge_count(self):

        return len(self.edges)
