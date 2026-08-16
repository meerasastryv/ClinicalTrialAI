"""
Relationship Service

Provides graph traversal utilities for impact analysis.

Author: ClinicalTrialAI
"""

from collections import deque
from typing import List, Set

from src.ic09.models.impact_node import ImpactNode
from src.ic09.repositories.impact_repository import ImpactRepository


class RelationshipService:
    """
    Performs graph traversal operations on the impact graph.
    """

    def __init__(self, repository: ImpactRepository) -> None:
        self._repository = repository

    def get_direct_impacts(self, node_id: str) -> List[ImpactNode]:
        """
        Return nodes directly connected to the given node.
        """
        return self._repository.get_connected_nodes(node_id)

    def get_upstream_impacts(self, node_id: str) -> List[ImpactNode]:
        """
        Return all upstream nodes that directly or transitively
        depend on the given node.
        """
        visited: Set[str] = set()
        results: List[ImpactNode] = []

        self._dfs_upstream(node_id, visited, results)

        return results

    def _dfs_upstream(
        self,
        node_id: str,
        visited: Set[str],
        results: List[ImpactNode],
    ) -> None:
        """
        Recursive upstream depth-first traversal.
        """
        if node_id in visited:
            return

        visited.add(node_id)

        for edge in self._repository.get_incoming_edges(node_id):
            source_node = self._repository.get_node(edge.source_id)

            if source_node is None:
                continue

            if source_node.node_id in visited:
                continue

            results.append(source_node)

            self._dfs_upstream(
                source_node.node_id,
                visited,
                results,
            )

    def get_transitive_impacts(self, node_id: str) -> List[ImpactNode]:
        """
        Return all reachable nodes using depth-first traversal.
        """
        visited: Set[str] = set()
        results: List[ImpactNode] = []

        self._dfs(node_id, visited, results)

        return results

    def _dfs(
        self,
        node_id: str,
        visited: Set[str],
        results: List[ImpactNode],
    ) -> None:
        """
        Recursive downstream depth-first traversal.
        """
        if node_id in visited:
            return

        visited.add(node_id)

        for node in self._repository.get_connected_nodes(node_id):
            if node.node_id in visited:
                continue

            results.append(node)

            self._dfs(
                node.node_id,
                visited,
                results,
            )

    def find_impact_path(
        self,
        source_id: str,
        target_id: str,
        direction: str = "downstream",
    ) -> List[str]:
        """
        Return the shortest impact path between two nodes.

        Parameters
        ----------
        source_id:
            Identifier of the starting node.

        target_id:
            Identifier of the destination node.

        direction:
            Traversal direction. Supported values are:
            "downstream" and "upstream".

        Returns
        -------
        List[str]
            Node identifiers representing the shortest path,
            including the source and target.

            Returns an empty list when:
            - the source node does not exist,
            - the target node does not exist, or
            - no path exists between the nodes.

        Raises
        ------
        ValueError
            If an unsupported direction is supplied.
        """
        source_node = self._repository.get_node(source_id)
        target_node = self._repository.get_node(target_id)

        if source_node is None or target_node is None:
            return []

        if source_id == target_id:
            return [source_id]

        if direction not in {"downstream", "upstream"}:
            raise ValueError(
                f"Unsupported impact direction: {direction}"
            )

        queue = deque([[source_id]])
        visited: Set[str] = {source_id}

        while queue:
            path = queue.popleft()
            current_id = path[-1]

            if direction == "downstream":
                edges = self._repository.get_outgoing_edges(current_id)

                next_ids = [
                    edge.target_id
                    for edge in edges
                ]

            else:
                edges = self._repository.get_incoming_edges(current_id)

                next_ids = [
                    edge.source_id
                    for edge in edges
                ]

            for next_id in next_ids:
                if next_id in visited:
                    continue

                next_node = self._repository.get_node(next_id)

                if next_node is None:
                    continue

                new_path = path + [next_id]

                if next_id == target_id:
                    return new_path

                visited.add(next_id)
                queue.append(new_path)

        return []
