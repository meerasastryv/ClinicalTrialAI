from src.ic05.graph.edge import Edge
from src.ic05.graph.graph import KnowledgeGraph
from src.ic05.graph.node import Node


class GraphRepository:
    """
    Repository responsible for managing the Knowledge Graph.
    """

    def __init__(self):

        self.graph = KnowledgeGraph()

    # ---------------------------------------------------------

    def add_node(
        self,
        node_id,
        node_type,
        name,
        properties=None,
    ):

        node = Node(
            node_id=node_id,
            node_type=node_type,
            name=name,
            properties=properties or {},
        )

        self.graph.add_node(node)

        return node

    # ---------------------------------------------------------

    def add_edge(
        self,
        source,
        target,
        relationship,
        properties=None,
    ):

        edge = Edge(
            source=source,
            target=target,
            relationship=relationship,
            properties=properties or {},
        )

        self.graph.add_edge(edge)

        return edge

    # ---------------------------------------------------------

    def get_node(self, node_id):

        return self.graph.get_node(node_id)

    # ---------------------------------------------------------

    def has_node(self, node_id):

        return self.get_node(node_id) is not None

    # ---------------------------------------------------------

    def has_edge(
        self,
        source,
        target,
        relationship,
    ):

        for edge in self.graph.get_all_edges():

            if (
                edge.source == source
                and edge.target == target
                and edge.relationship == relationship
            ):
                return True

        return False

    # ---------------------------------------------------------

    def remove_node(self, node_id):

        node = self.get_node(node_id)

        if node is None:
            return False

        self.graph.nodes.remove(node)

        del self.graph.node_lookup[node_id]

        self.graph.edges = [
            edge
            for edge in self.graph.edges
            if edge.source != node_id
            and edge.target != node_id
        ]

        self.graph.outgoing_edges.pop(node_id, None)

        self.graph.incoming_edges.pop(node_id, None)

        for edges in self.graph.outgoing_edges.values():
            edges[:] = [
                edge
                for edge in edges
                if edge.target != node_id
            ]

        for edges in self.graph.incoming_edges.values():
            edges[:] = [
                edge
                for edge in edges
                if edge.source != node_id
            ]

        return True

    # ---------------------------------------------------------

    def remove_edge(
        self,
        source,
        target,
        relationship,
    ):

        removed = False

        self.graph.edges = [
            edge
            for edge in self.graph.edges
            if not (
                edge.source == source
                and edge.target == target
                and edge.relationship == relationship
            )
        ]

        outgoing = self.graph.outgoing_edges.get(source, [])

        self.graph.outgoing_edges[source] = [
            edge
            for edge in outgoing
            if not (
                edge.target == target
                and edge.relationship == relationship
            )
        ]

        incoming = self.graph.incoming_edges.get(target, [])

        self.graph.incoming_edges[target] = [
            edge
            for edge in incoming
            if not (
                edge.source == source
                and edge.relationship == relationship
            )
        ]

        removed = True

        return removed

    # ---------------------------------------------------------

    def get_all_nodes(self):

        return self.graph.get_all_nodes()

    # ---------------------------------------------------------

    def get_all_edges(self):

        return self.graph.get_all_edges()

    # ---------------------------------------------------------

    def get_neighbors(self, node_id):

        return self.graph.get_neighbors(node_id)

    # ---------------------------------------------------------

    def find_nodes_by_type(self, node_type):

        return self.graph.find_nodes_by_type(node_type)

    # ---------------------------------------------------------

    def find_nodes_by_label(self, label):

        return [
            node
            for node in self.graph.get_all_nodes()
            if label in node.labels
        ]

    # ---------------------------------------------------------

    def find_nodes_by_tag(self, tag):

        return [
            node
            for node in self.graph.get_all_nodes()
            if tag in node.tags
        ]

    # ---------------------------------------------------------

    def find_nodes_by_property(
        self,
        key,
        value,
    ):

        return [
            node
            for node in self.graph.get_all_nodes()
            if node.get_property(key) == value
        ]

    # ---------------------------------------------------------

    def clear(self):

        self.graph = KnowledgeGraph()

    # ---------------------------------------------------------

    def statistics(self):

        labels = set()
        tags = set()

        for node in self.graph.get_all_nodes():

            labels.update(node.labels)

            tags.update(node.tags)

        return {
            "nodes": self.node_count(),
            "edges": self.edge_count(),
            "labels": len(labels),
            "tags": len(tags),
        }

    # ---------------------------------------------------------

    def node_count(self):

        return self.graph.node_count()

    # ---------------------------------------------------------

    def edge_count(self):

        return self.graph.edge_count()

    # ---------------------------------------------------------

    def get_graph(self):

        return self.graph
