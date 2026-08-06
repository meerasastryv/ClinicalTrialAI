"""
Impact Repository

Repository for managing impact graph nodes and relationships.

Author: ClinicalTrialAI
"""

from typing import Dict, List, Optional

from src.ic09.models.impact_node import ImpactNode
from src.ic09.models.impact_edge import ImpactEdge


class ImpactRepository:
    """
    Repository for impact graph data.
    """

    def __init__(self) -> None:
        self._nodes: Dict[str, ImpactNode] = {}
        self._edges: List[ImpactEdge] = []

    def add_node(self, node: ImpactNode) -> None:
        """
        Add or update a node.
        """
        self._nodes[node.node_id] = node

    def get_node(self, node_id: str) -> Optional[ImpactNode]:
        """
        Retrieve a node by its identifier.
        """
        return self._nodes.get(node_id)

    def get_all_nodes(self) -> List[ImpactNode]:
        """
        Return all nodes.
        """
        return list(self._nodes.values())

    def add_edge(self, edge: ImpactEdge) -> None:
        """
        Add a relationship.
        """
        self._edges.append(edge)

    def get_all_edges(self) -> List[ImpactEdge]:
        """
        Return all relationships.
        """
        return list(self._edges)

    def get_outgoing_edges(self, source_id: str) -> List[ImpactEdge]:
        """
        Return all outgoing relationships.
        """
        return [
            edge
            for edge in self._edges
            if edge.source_id == source_id
        ]

    def get_incoming_edges(self, target_id: str) -> List[ImpactEdge]:
        """
        Return all incoming relationships.
        """
        return [
            edge
            for edge in self._edges
            if edge.target_id == target_id
        ]

    def get_connected_nodes(self, node_id: str) -> List[ImpactNode]:
        """
        Return directly connected nodes.
        """
        connected = []

        for edge in self.get_outgoing_edges(node_id):
            node = self.get_node(edge.target_id)
            if node:
                connected.append(node)

        return connected

    def clear(self) -> None:
        """
        Clear the repository.
        """
        self._nodes.clear()
        self._edges.clear()
