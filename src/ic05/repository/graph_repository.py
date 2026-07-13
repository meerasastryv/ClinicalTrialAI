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

    def node_count(self):

        return self.graph.node_count()

    # ---------------------------------------------------------

    def edge_count(self):

        return self.graph.edge_count()

    # ---------------------------------------------------------

    def get_graph(self):

        return self.graph
