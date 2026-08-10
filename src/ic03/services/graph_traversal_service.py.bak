from collections import defaultdict, deque


class GraphTraversalService:
    """
    Generic graph traversal service built on top of the
    RelationshipRepository.

    This service is intentionally generic and knows nothing about
    classes, methods, modules or files. It simply traverses a graph
    composed of source -> target relationships.
    """

    def __init__(self, repository):
        self.repository = repository

        self.graph = defaultdict(set)
        self.reverse_graph = defaultdict(set)
        self.nodes = set()

        self.build_graph()

    # ---------------------------------------------------------
    # Graph Construction
    # ---------------------------------------------------------

    def build_graph(self):
        """
        Build adjacency and reverse-adjacency maps.
        """

        self.graph.clear()
        self.reverse_graph.clear()
        self.nodes.clear()

        for relationship in self.repository.get_all():

            source = relationship.source
            target = relationship.target

            self.graph[source].add(target)
            self.reverse_graph[target].add(source)

            self.nodes.add(source)
            self.nodes.add(target)

    # ---------------------------------------------------------
    # Basic Graph Information
    # ---------------------------------------------------------

    def get_nodes(self):
        """
        Return every node discovered in the graph.
        """
        return sorted(self.nodes)

    def node_count(self):
        return len(self.nodes)

    def edge_count(self):
        return len(self.repository.get_all())

    # ---------------------------------------------------------
    # Neighbor Queries
    # ---------------------------------------------------------

    def get_neighbors(self, node):
        """
        Alias for outgoing neighbors.
        """
        return self.get_outgoing_neighbors(node)

    def get_outgoing_neighbors(self, node):
        """
        Nodes directly reachable from this node.
        """
        return sorted(self.graph.get(node, set()))

    def get_incoming_neighbors(self, node):
        """
        Nodes pointing to this node.
        """
        return sorted(self.reverse_graph.get(node, set()))

    def out_degree(self, node):
        return len(self.graph.get(node, set()))

    def in_degree(self, node):
        return len(self.reverse_graph.get(node, set()))

    # ---------------------------------------------------------
    # Breadth First Search
    # ---------------------------------------------------------

    def breadth_first_search(self, start):
        """
        Perform BFS traversal from the given node.
        """

        if start not in self.nodes:
            return []

        visited = set()
        queue = deque([start])
        traversal = []

        while queue:

            node = queue.popleft()

            if node in visited:
                continue

            visited.add(node)
            traversal.append(node)

            for neighbor in sorted(
                self.graph.get(node, set())
            ):
                if neighbor not in visited:
                    queue.append(neighbor)

        return traversal


    # ---------------------------------------------------------
    # Depth First Search
    # ---------------------------------------------------------

    def depth_first_search(self, start):
        """
        Perform DFS traversal from the given node.
        """

        if start not in self.nodes:
            return []

        visited = set()
        traversal = []

        self._dfs(start, visited, traversal)

        return traversal

    def _dfs(self, node, visited, traversal):

        visited.add(node)
        traversal.append(node)

        for neighbor in sorted(
            self.graph.get(node, set())
        ):

            if neighbor not in visited:
                self._dfs(
                    neighbor,
                    visited,
                    traversal,
                )

    # ---------------------------------------------------------
    # Reachability
    # ---------------------------------------------------------

    def reachable_nodes(self, start):
        """
        Return every node reachable from the given node.
        """

        traversal = self.breadth_first_search(start)

        if not traversal:
            return []

        return traversal[1:]

    def has_path(self, source, target):
        """
        Returns True if a path exists between source and target.
        """

        if source == target:
            return True

        visited = set()
        queue = deque([source])

        while queue:

            current = queue.popleft()

            if current == target:
                return True

            if current in visited:
                continue

            visited.add(current)

            for neighbor in self.graph.get(
                current,
                set(),
            ):

                if neighbor not in visited:
                    queue.append(neighbor)

        return False

    # ---------------------------------------------------------
    # Transitive Dependencies
    # ---------------------------------------------------------

    def transitive_dependencies(self, node):
        """
        Returns all recursively reachable nodes.
        """

        return self.reachable_nodes(node)

    def incoming_dependencies(self, node):
        """
        Returns every node having a direct dependency on this node.
        """

        return self.get_incoming_neighbors(node)

    def outgoing_dependencies(self, node):
        """
        Returns every node directly referenced by this node.
        """

        return self.get_outgoing_neighbors(node)


    # ---------------------------------------------------------
    # Shortest Path
    # ---------------------------------------------------------

    def shortest_path(self, source, target):
        """
        Returns the shortest path between source and target using BFS.
        Returns an empty list if no path exists.
        """

        if source not in self.nodes or target not in self.nodes:
            return []

        if source == target:
            return [source]

        visited = {source}
        queue = deque([(source, [source])])

        while queue:

            current, path = queue.popleft()

            for neighbor in sorted(
                self.graph.get(current, set())
            ):

                if neighbor == target:
                    return path + [neighbor]

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(
                        (
                            neighbor,
                            path + [neighbor],
                        )
                    )

        return []

    # ---------------------------------------------------------
    # Graph Analysis
    # ---------------------------------------------------------

    def root_nodes(self):
        """
        Nodes having no incoming relationships.
        """

        return sorted(
            [
                node
                for node in self.nodes
                if self.in_degree(node) == 0
            ]
        )

    def leaf_nodes(self):
        """
        Nodes having no outgoing relationships.
        """

        return sorted(
            [
                node
                for node in self.nodes
                if self.out_degree(node) == 0
            ]
        )

    def isolated_nodes(self):
        """
        Nodes having no incoming or outgoing relationships.
        """

        return sorted(
            [
                node
                for node in self.nodes
                if self.in_degree(node) == 0
                and self.out_degree(node) == 0
            ]
        )

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def graph_statistics(self):
        """
        Returns summary statistics about the graph.
        """

        return {
            "nodes": self.node_count(),
            "edges": self.edge_count(),
            "root_nodes": len(self.root_nodes()),
            "leaf_nodes": len(self.leaf_nodes()),
            "isolated_nodes": len(
                self.isolated_nodes()
            ),
        }

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def refresh(self):
        """
        Rebuild the graph after repository updates.
        """

        self.build_graph()

    def clear(self):
        """
        Clear all cached graph structures.
        """

        self.graph.clear()
        self.reverse_graph.clear()
        self.nodes.clear()
