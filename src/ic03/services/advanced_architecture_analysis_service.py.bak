class AdvancedArchitectureAnalysisService:
    """
    Performs advanced architecture analysis using the dependency graph.
    """

    def __init__(self, graph_traversal_service):

        self.graph = graph_traversal_service

    # ---------------------------------------------------------
    # Orphan Components
    # ---------------------------------------------------------

    def orphan_components(self):
        """
        Components having no incoming and no outgoing dependencies.
        """

        orphans = []

        for node in self.graph.get_nodes():

            fan_in = self.graph.in_degree(node)
            fan_out = self.graph.out_degree(node)

            if fan_in == 0 and fan_out == 0:

                orphans.append(node)

        return sorted(orphans)

    # ---------------------------------------------------------
    # Highly Coupled Components
    # ---------------------------------------------------------

    def highly_coupled_components(self, threshold=10):
        """
        Components having high dependency counts.
        """

        components = []

        for node in self.graph.get_nodes():

            fan_in = self.graph.in_degree(node)
            fan_out = self.graph.out_degree(node)

            total = fan_in + fan_out

            if total >= threshold:

                components.append(
                    (
                        node,
                        fan_in,
                        fan_out,
                        total
                    )
                )

        components.sort(
            key=lambda item: item[3],
            reverse=True
        )

        return components

    # ---------------------------------------------------------
    # Basic Statistics
    # ---------------------------------------------------------

    def total_components(self):

        return self.graph.node_count()

    def total_relationships(self):

        return self.graph.edge_count()

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def summary(self):

        return {
            "components": self.total_components(),
            "relationships": self.total_relationships(),
            "orphans": len(self.orphan_components()),
            "highly_coupled": len(
                self.highly_coupled_components()
            )
        }

    # ---------------------------------------------------------
    # Circular Dependency Detection
    # ---------------------------------------------------------

    def detect_cycles(self):
        """
        Detect circular dependencies using DFS.
        """

        visited = set()
        recursion_stack = set()
        cycles = []

        for node in self.graph.get_nodes():

            if node not in visited:

                self._dfs_cycle_detection(
                    node,
                    visited,
                    recursion_stack,
                    [],
                    cycles
                )

        #
        # Remove duplicate cycles
        #
        unique_cycles = []
        seen = set()

        for cycle in cycles:

            key = tuple(sorted(cycle))

            if key not in seen:

                seen.add(key)
                unique_cycles.append(cycle)

        return unique_cycles

    # ---------------------------------------------------------
    # Internal DFS
    # ---------------------------------------------------------

    def _dfs_cycle_detection(
        self,
        node,
        visited,
        recursion_stack,
        path,
        cycles
    ):

        visited.add(node)
        recursion_stack.add(node)
        path.append(node)

        for neighbor in self.graph.get_neighbors(node):

            if neighbor not in visited:

                self._dfs_cycle_detection(
                    neighbor,
                    visited,
                    recursion_stack,
                    path,
                    cycles
                )

            elif neighbor in recursion_stack:

                if neighbor in path:

                    start = path.index(neighbor)

                    cycle = path[start:] + [neighbor]

                    cycles.append(cycle)

        recursion_stack.remove(node)
        path.pop()

    # ---------------------------------------------------------
    # Cycle Count
    # ---------------------------------------------------------

    def cycle_count(self):
        """
        Returns the number of circular dependencies.
        """

        return len(self.detect_cycles())


    # ---------------------------------------------------------
    # Deep Dependency Chains
    # ---------------------------------------------------------

    def find_deep_dependency_chains(self):
        """
        Finds dependency chains starting from every node.
        """

        chains = []

        for node in self.graph.get_nodes():

            chain = self._longest_chain(node)

            if len(chain) > 1:

                chains.append(chain)

        chains.sort(
            key=len,
            reverse=True
        )

        return chains

    # ---------------------------------------------------------
    # Longest Chain From Node
    # ---------------------------------------------------------

    def _longest_chain(self, start_node):

        longest = []

        def dfs(node, path):

            nonlocal longest

            if len(path) > len(longest):

                longest = list(path)

            for neighbor in self.graph.get_neighbors(node):

                if neighbor not in path:

                    path.append(neighbor)

                    dfs(
                        neighbor,
                        path
                    )

                    path.pop()

        dfs(
            start_node,
            [start_node]
        )

        return longest

    # ---------------------------------------------------------
    # Longest Dependency Chain
    # ---------------------------------------------------------

    def longest_dependency_chain(self):
        """
        Returns the longest dependency chain.
        """

        chains = self.find_deep_dependency_chains()

        if not chains:

            return []

        return chains[0]

    # ---------------------------------------------------------
    # Maximum Dependency Depth
    # ---------------------------------------------------------

    def maximum_dependency_depth(self):
        """
        Returns the maximum dependency depth.
        """

        chain = self.longest_dependency_chain()

        return max(
            0,
            len(chain) - 1
        )


    # ---------------------------------------------------------
    # Hub Components
    # ---------------------------------------------------------

    def hub_components(self, threshold=15):
        """
        Components acting as architectural hubs.
        """

        hubs = []

        for node in self.graph.get_nodes():

            fan_in = self.graph.in_degree(node)
            fan_out = self.graph.out_degree(node)

            if fan_in >= threshold and fan_out >= threshold:

                hubs.append(
                    (
                        node,
                        fan_in,
                        fan_out
                    )
                )

        hubs.sort(
            key=lambda item: (
                item[1] + item[2]
            ),
            reverse=True
        )

        return hubs

    # ---------------------------------------------------------
    # Architecture Smells
    # ---------------------------------------------------------

    def architecture_smells(self):
        """
        Detect simple architecture smells.
        """

        smells = []

        #
        # Highly coupled components
        #
        for component in self.highly_coupled_components():

            smells.append(
                (
                    "Highly Coupled",
                    component[0]
                )
            )

        #
        # Hub components
        #
        for component in self.hub_components():

            smells.append(
                (
                    "Hub Component",
                    component[0]
                )
            )

        #
        # Circular dependencies
        #
        for cycle in self.detect_cycles():

            smells.append(
                (
                    "Circular Dependency",
                    " -> ".join(cycle)
                )
            )

        return smells

    # ---------------------------------------------------------
    # Stability Index
    # ---------------------------------------------------------

    def stability_index(self):
        """
        Computes a simple stability indicator.
        """

        components = self.total_components()

        if components == 0:
            return 100.0

        unstable = len(
            self.highly_coupled_components()
        )

        score = max(
            0.0,
            100.0 - (
                unstable / components
            ) * 100
        )

        return round(score, 2)

    # ---------------------------------------------------------
    # Enhanced Summary
    # ---------------------------------------------------------

    def detailed_summary(self):
        """
        Returns detailed architecture statistics.
        """

        return {
            "components": self.total_components(),
            "relationships": self.total_relationships(),
            "orphans": len(self.orphan_components()),
            "highly_coupled": len(
                self.highly_coupled_components()
            ),
            "cycles": self.cycle_count(),
            "deepest_chain": self.maximum_dependency_depth(),
            "hub_components": len(
                self.hub_components()
            ),
            "architecture_smells": len(
                self.architecture_smells()
            ),
            "stability_index": self.stability_index()
        }
