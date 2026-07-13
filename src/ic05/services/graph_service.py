from src.ic05.repository.graph_repository import GraphRepository


class GraphService:
    """
    Service layer for the Knowledge Graph.
    """

    def __init__(self):

        self.repository = GraphRepository()

    # ---------------------------------------------------------

    def add_node(
        self,
        node_id,
        node_type,
        name,
        properties=None,
    ):

        return self.repository.add_node(
            node_id=node_id,
            node_type=node_type,
            name=name,
            properties=properties,
        )

    # ---------------------------------------------------------

    def add_edge(
        self,
        source,
        target,
        relationship,
        properties=None,
    ):

        return self.repository.add_edge(
            source=source,
            target=target,
            relationship=relationship,
            properties=properties,
        )

    # ---------------------------------------------------------

    def get_node(self, node_id):

        return self.repository.get_node(node_id)

    # ---------------------------------------------------------

    def get_all_nodes(self):

        return self.repository.get_all_nodes()

    # ---------------------------------------------------------

    def get_all_edges(self):

        return self.repository.get_all_edges()

    # ---------------------------------------------------------

    def get_neighbors(self, node_id):

        return self.repository.get_neighbors(node_id)

    # ---------------------------------------------------------

    def find_nodes_by_type(self, node_type):

        return self.repository.find_nodes_by_type(node_type)

    # ---------------------------------------------------------

    def node_count(self):

        return self.repository.node_count()

    # ---------------------------------------------------------

    def edge_count(self):

        return self.repository.edge_count()

    # ---------------------------------------------------------

    def get_graph(self):

        return self.repository.get_graph()
