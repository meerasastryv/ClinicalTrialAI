"""
Relationship Service

Provides graph traversal utilities for impact analysis.

Author: ClinicalTrialAI
"""

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
        results: List[ImpactNode]
    ) -> None:
        """
        Recursive depth-first traversal.
        """
        if node_id in visited:
            return

        visited.add(node_id)

        for node in self._repository.get_connected_nodes(node_id):
            results.append(node)
            self._dfs(node.node_id, visited, results)
