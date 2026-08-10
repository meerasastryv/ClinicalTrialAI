"""
graph_relationship_builder.py

Builds graph relationships (edges) and stores them directly
in the Knowledge Graph via GraphRepository.
"""

from __future__ import annotations

from typing import Dict, Iterable, List, Optional

from src.ic05.repository.graph_repository import GraphRepository


class GraphRelationshipBuilder:
    """
    Responsible for creating graph edges.

    This class validates relationships, prevents duplicates,
    enriches edge properties and inserts edges into the graph.
    """

    DEFAULT_CONFIDENCE = {
        "CONTAINS": 1.00,
        "CALLS": 0.99,
        "IMPLEMENTS": 0.95,
        "USES": 0.85,
        "READS": 0.95,
        "WRITES": 0.95,
        "QUERIES": 0.98,
        "RETURNS": 0.95,
        "IMPORTS": 0.98,
        "EXTENDS": 1.00,
        "IMPLEMENTS_INTERFACE": 1.00,
        "DEPENDS_ON": 0.90,
        "EXECUTES": 0.95,
        "INVOKES_API": 0.98,
        "INVOKES_DB": 0.98,
        "GENERATES": 0.90,
        "BELONGS_TO": 1.00,
    }

    def __init__(
        self,
        graph_repository: Optional[GraphRepository] = None,
    ):
        self._graph_repository = (
            graph_repository
            if graph_repository is not None
            else GraphRepository()
        )

    # ---------------------------------------------------------

    @property
    def repository(self) -> GraphRepository:
        return self._graph_repository

    # ---------------------------------------------------------

    def build_relationship(
        self,
        source: str,
        target: str,
        relationship: str,
        properties: Optional[Dict] = None,
    ):
        """
        Build a single graph relationship.
        """

        self.validate_relationship(
            source,
            target,
            relationship,
        )

        if self.relationship_exists(
            source,
            target,
            relationship,
        ):
            return None

        edge_properties = dict(properties or {})

        edge_properties.setdefault(
            "confidence",
            self.default_confidence(relationship),
        )

        edge_properties.setdefault(
            "created_by",
            "GraphRelationshipBuilder",
        )

        return self._graph_repository.add_edge(
            source=source,
            target=target,
            relationship=relationship,
            properties=edge_properties,
        )

    # ---------------------------------------------------------

    def build_relationships(
        self,
        relationships: Iterable[Dict],
    ) -> List:

        edges = []

        for item in relationships:

            edge = self.build_relationship(
                source=item["source"],
                target=item["target"],
                relationship=item["relationship"],
                properties=item.get("properties"),
            )

            if edge is not None:
                edges.append(edge)

        return edges

    # ---------------------------------------------------------

    def validate_relationship(
        self,
        source: str,
        target: str,
        relationship: str,
    ):

        if not source:
            raise ValueError(
                "Source node cannot be empty."
            )

        if not target:
            raise ValueError(
                "Target node cannot be empty."
            )

        if source == target:
            raise ValueError(
                "Self relationships are not allowed."
            )

        if not relationship:
            raise ValueError(
                "Relationship type cannot be empty."
            )

        if not self._graph_repository.has_node(source):
            raise ValueError(
                f"Unknown source node: {source}"
            )

        if not self._graph_repository.has_node(target):
            raise ValueError(
                f"Unknown target node: {target}"
            )

    # ---------------------------------------------------------

    def relationship_exists(
        self,
        source: str,
        target: str,
        relationship: str,
    ) -> bool:

        return self._graph_repository.has_edge(
            source,
            target,
            relationship,
        )

    # ---------------------------------------------------------

    def default_confidence(
        self,
        relationship: str,
    ) -> float:

        return self.DEFAULT_CONFIDENCE.get(
            relationship,
            0.80,
        )

    # ---------------------------------------------------------

    def statistics(self):

        return self._graph_repository.statistics()
