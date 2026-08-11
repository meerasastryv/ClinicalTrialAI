"""
Breadth First Graph Traversal Service

Provides graph traversal utilities for the Impact Analysis Engine.

Capabilities
------------
- Downstream traversal
- Upstream traversal
- Level-order traversal
- Maximum depth support
- Traversal statistics
"""

from __future__ import annotations

from collections import deque
from typing import Dict, List, Set, Optional, Iterable

#from src.ic09.models.dependency_graph import DependencyGraph
from ct_platform.graph.dependency_graph import DependencyGraph
class BFSTraversalService:
    """
    Breadth First Search traversal over a DependencyGraph.
    """

    def __init__(self, graph: DependencyGraph):
        self.graph = graph
        self.adjacency = graph.adjacency_list()
        self.reverse_adjacency = self._build_reverse_adjacency()
    def _build_reverse_adjacency(self) -> Dict[str, List[str]]:
        """
        Build reverse adjacency map from the graph edges.
        """
        reverse = {}
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
        Traverse the dependency graph using BFS.

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
            Ordered traversal result.
        """

        if start_node not in self.graph.nodes.keys():
            return []
        if max_depth is not None and max_depth < 0:
            raise ValueError("max_depth must be non-negative")
        visited: Set[str] = set()
        traversal: List[str] = []

        queue = deque([(start_node, 0)])
        visited.add(start_node)

        while queue:

            current, depth = queue.popleft()

            traversal.append(current)

            if max_depth is not None and depth >= max_depth:
                continue

            neighbors = self._get_neighbors(current, direction)

            for node in neighbors:

                if node not in visited:
                    visited.add(node)
                    queue.append((node, depth + 1))

        return traversal

    def _get_neighbors(self,node: str,direction: str,):
        """
        Return neighboring nodes.
        """
        if direction.lower() == "upstream":
            return self.reverse_adjacency.get(node, [])
        return self.adjacency.get(node, [])

    def get_levels(
        self,
        start_node: str,
        direction: str = "downstream",
        max_depth: Optional[int] = None,
    ) -> Dict[int, List[str]]:
        """
        Return nodes grouped by BFS level.

        Example
        -------
        Level 0 : A
        Level 1 : B C
        Level 2 : D E
        """

        if start_node not in self.graph.nodes.keys():
            return {}

        visited: Set[str] = {start_node}
        queue = deque([(start_node, 0)])

        levels: Dict[int, List[str]] = {}

        while queue:

            node, depth = queue.popleft()

            levels.setdefault(depth, []).append(node)

            if max_depth is not None and depth >= max_depth:
                continue

            for neighbor in self._get_neighbors(node, direction):

                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, depth + 1))

        return levels


    def get_distances(
        self,
        start_node: str,
        direction: str = "downstream",
    ) -> Dict[str, int]:
        """
        Return shortest BFS distance from the start node
        to every reachable node.
        """

        if start_node not in self.graph.nodes.keys():
            return {}

        visited = {start_node}
        queue = deque([(start_node, 0)])

        distances = {
            start_node: 0
        }

        while queue:

            node, depth = queue.popleft()

            for neighbor in self._get_neighbors(node, direction):

                if neighbor not in visited:

                    visited.add(neighbor)

                    distances[neighbor] = depth + 1

                    queue.append((neighbor, depth + 1))

        return distances


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
    def find_path(
        self,
        source: str,
        target: str,
        direction: str = "downstream",
    ) -> List[str]:
        """
        Find the shortest path from source to target using BFS.

        Returns an empty list if either node is unknown
        or if no path exists.
        """

        if source not in self.graph.nodes.keys():
            return []

        if target not in self.graph.nodes.keys():
            return []

        visited: Set[str] = {source}
        queue = deque([(source, [source])])

        while queue:
            node, path = queue.popleft()

            if node == target:
                return path

            for neighbor in self._get_neighbors(node, direction):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(
                        (neighbor, path + [neighbor])
                    )

        return []

    def traversal_statistics(
        self,
        start_node: str,
        direction: str = "downstream",
        max_depth: Optional[int] = None,
    ) -> Dict:
        """
        Return traversal summary statistics.
        """

        traversal = self.traverse(
            start_node,
            direction,
            max_depth,
        )

        levels = self.get_levels(
            start_node,
            direction,
            max_depth,
        )

        return {
            "start_node": start_node,
            "direction": direction,
            "visited_nodes": len(traversal),
            "max_level": max(levels.keys()) if levels else 0,
            "levels": len(levels),
            "traversal": traversal,
        }


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
