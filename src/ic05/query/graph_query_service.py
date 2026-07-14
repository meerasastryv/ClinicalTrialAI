from src.ic05.query.graph_query_engine import GraphQueryEngine


class GraphQueryService:
    """
    Service layer for Graph Query Engine.
    """

    def __init__(self, repository):

        self.engine = GraphQueryEngine(repository)

    # ---------------------------------------------------------

    def get_node(self, node_id):

        return self.engine.get_node(node_id)

    # ---------------------------------------------------------

    def neighbors(self, node_id):

        return self.engine.get_neighbors(node_id)

    # ---------------------------------------------------------

    def path(self, start_node, end_node):

        return self.engine.find_path(
            start_node,
            end_node,
        )

    # ---------------------------------------------------------

    def connected(self, node_id):

        return self.engine.connected_nodes(node_id)

    # ---------------------------------------------------------

    def search_type(self, node_type):

        return self.engine.search_by_type(node_type)

    # ---------------------------------------------------------

    def search_name(self, text):

        return self.engine.search_by_name(text)
