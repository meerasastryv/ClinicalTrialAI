from collections import deque


class GraphQueryEngine:
    """
    Query engine for the Knowledge Graph.

    This implementation works directly with the existing
    GraphRepository and KnowledgeGraph classes developed
    in Milestone 8.
    """

    def __init__(self, repository):
        self.repository = repository

    # ---------------------------------------------------------

    def get_node(self, node_id):
        """
        Return a node by its ID.
        """
        return self.repository.get_node(node_id)

    # ---------------------------------------------------------

    def get_neighbors(self, node_id):
        """
        Return neighboring nodes.
        """
        return self.repository.get_neighbors(node_id)

    # ---------------------------------------------------------

    def search_by_type(self, node_type):
        """
        Return all nodes of a specific type.
        """
        return self.repository.find_nodes_by_type(node_type)

    # ---------------------------------------------------------

    def search_by_name(self, text):
        """
        Search nodes whose name contains the supplied text.
        """

        text = text.lower()

        result = []

        for node in self.repository.get_all_nodes():

            if text in node.name.lower():
                result.append(node)

        return result

    # ---------------------------------------------------------

    def connected_nodes(self, node_id):
        """
        Return every node connected to the supplied node.
        """

        visited = set()

        queue = deque([node_id])

        connected = []

        while queue:

            current = queue.popleft()

            if current in visited:
                continue

            visited.add(current)

            node = self.repository.get_node(current)

            if node:
                connected.append(node)

            #
            # Outgoing neighbours
            #

            for neighbour in self.repository.get_neighbors(current):

                if neighbour.node_id not in visited:
                    queue.append(neighbour.node_id)

            #
            # Incoming neighbours
            #

            for edge in self.repository.get_all_edges():

                if edge.target == current:

                    if edge.source not in visited:
                        queue.append(edge.source)

        return connected

    # ---------------------------------------------------------

    def find_path(self, start_id, end_id):
        """
        Breadth First Search.
        Returns list of Node objects.
        """

        if start_id == end_id:

            node = self.repository.get_node(start_id)

            return [node] if node else []

        visited = set()

        queue = deque()

        queue.append((start_id, []))

        while queue:

            current, path = queue.popleft()

            if current in visited:
                continue

            visited.add(current)

            node = self.repository.get_node(current)

            if node is None:
                continue

            new_path = path + [node]

            #
            # Outgoing neighbours
            #

            for neighbour in self.repository.get_neighbors(current):

                if neighbour.node_id == end_id:
                    return new_path + [neighbour]

                if neighbour.node_id not in visited:

                    queue.append(
                        (
                            neighbour.node_id,
                            new_path,
                        )
                    )

            #
            # Incoming neighbours
            #

            for edge in self.repository.get_all_edges():

                if edge.target == current:

                    if edge.source == end_id:

                        source_node = self.repository.get_node(edge.source)

                        return new_path + [source_node]

                    if edge.source not in visited:

                        queue.append(
                            (
                                edge.source,
                                new_path,
                            )
                        )

        return []
