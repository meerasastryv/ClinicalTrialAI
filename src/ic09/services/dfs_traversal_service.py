from __future__ import annotations

from typing import Dict, List, Set, Optional

from ct_platform.graph.dependency_graph import DependencyGraph


class DFSTraversalService:
    """
    Depth First Search traversal over a DependencyGraph.

    Provides:
    - Downstream traversal
    - Upstream traversal
    - Maximum depth support
    - Reachability analysis
    - Reachable node discovery
    """

    def __init__(self, graph: DependencyGraph):
        self.graph = graph
        self.adjacency = graph.adjacency_list()
        self.reverse_adjacency = self._build_reverse_adjacency()

    def _build_reverse_adjacency(self) -> Dict[str, List[str]]:
        """
        Build reverse adjacency map from the graph edges.
        """
        reverse: Dict[str, List[str]] = {}

        for source, targets in self.adjacency.items():
            for target in targets:
                reverse.setdefault(target, []).append(source)

        return reverse

    def traverse(
        self,
        start_node: str,
        direction: str = "downstream",
        max_depth: Optional[int] = None,
    ) -> List[str]:
        """
        Traverse the dependency graph using DFS.

        Parameters
        ----------
        start_node
            Starting module.

        direction
            downstream | upstream

        max_depth
            Optional traversal depth.

        Returns
        -------
        List[str]
            Ordered DFS traversal result.
        """

        if start_node not in self.graph.nodes.keys():
            return []

        if max_depth is not None and max_depth < 0:
            raise ValueError("max_depth must be >= 0")

        visited: Set[str] = set()
        traversal: List[str] = []

        def dfs(node: str, depth: int) -> None:
            if node in visited:
                return

            visited.add(node)
            traversal.append(node)

            if max_depth is not None and depth >= max_depth:
                return

            for neighbor in self._get_neighbors(node, direction):
                if neighbor not in visited:
                    dfs(neighbor, depth + 1)

        dfs(start_node, 0)

        return traversal

    def _get_neighbors(
        self,
        node: str,
        direction: str,
    ) -> List[str]:
        """
        Return neighboring nodes.
        """

        if direction.lower() == "upstream":
            return self.reverse_adjacency.get(node, [])

        return self.adjacency.get(node, [])

    def is_reachable(
        self,
        source: str,
        target: str,
        direction: str = "downstream",
    ) -> bool:
        """
        Determine whether the target node is reachable
        from the source node.
        """

        return target in self.traverse(
            source,
            direction=direction,
        )

    def reachable_nodes(
        self,
        start_node: str,
        direction: str = "downstream",
        max_depth: Optional[int] = None,
    ) -> Set[str]:
        """
        Return all reachable nodes as a set.
        """

        return set(
            self.traverse(
                start_node,
                direction=direction,
                max_depth=max_depth,
            )
        )
