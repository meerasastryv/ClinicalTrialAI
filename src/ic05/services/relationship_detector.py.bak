"""
relationship_detector.py

Discovers graph relationships from the Knowledge Graph.

The detector never creates graph edges directly.
Instead it returns relationship dictionaries that are
consumed by GraphRelationshipBuilder.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List

from src.ic05.repository.graph_repository import GraphRepository


class RelationshipDetector:
    """
    Detects inferred relationships from graph nodes.
    """

    """
    DETECTION_RULES = [
        ("Requirement", "Method", "IMPLEMENTS"),
        ("Class", "Method", "CONTAINS"),
        ("Method", "API", "INVOKES_API"),
        ("Method", "Database", "INVOKES_DB"),
        ("Runtime", "Method", "EXECUTES"),
    ]
    """
    DETECTION_RULES = [
        ("Method", "Requirement", "IMPLEMENTS"),
        ("Method", "Class", "CONTAINS"),
        ("Method", "API", "INVOKES_API"),
        ("Method", "Database", "INVOKES_DB"),
        ("Runtime", "Method", "EXECUTES"),
    ]

    def __init__(self, graph_repository: GraphRepository):
        self.graph_repository = graph_repository

    # ---------------------------------------------------------

    def detect_all_relationships(self) -> List[Dict]:
        """
        Execute all configured relationship detection rules.
        """

        grouped_nodes = self._group_nodes_by_type()

        relationships = []

        for source_type, target_type, relationship in self.DETECTION_RULES:

            source_nodes = grouped_nodes.get(source_type, [])
            target_nodes = grouped_nodes.get(target_type, [])

            relationships.extend(
                self._detect_relationships(
                    source_nodes,
                    target_nodes,
                    relationship,
                )
            )

        return relationships

    # ---------------------------------------------------------

    def _group_nodes_by_type(self):

        grouped = defaultdict(list)

        for node in self.graph_repository.get_all_nodes():
            grouped[node.node_type].append(node)

        return grouped

    # ---------------------------------------------------------

    def _detect_relationships(
        self,
        source_nodes,
        target_nodes,
        relationship,
    ):

        detected = []

        for source in source_nodes:

            for target in target_nodes:

                if source.node_id == target.node_id:
                    continue

                if self._is_related(
                    source,
                    target,
                    relationship,
                ):

                    detected.append(
                        {
                            "source": source.node_id,
                            "target": target.node_id,
                            "relationship": relationship,
                            "properties": {
                                "confidence": 0.95,
                                "created_by": "RelationshipDetector",
                                "description": self._description(
                                    relationship,
                                    source.name,
                                    target.name,
                                ),
                            },
                        }
                    )

        return detected

    # ---------------------------------------------------------

    def _is_related(
        self,
        source,
        target,
        relationship,
    ):
        """
        Determine whether two nodes are related.

        Detection strategy (highest confidence first):

        1. Explicit property references
        2. Labels
        3. Tags
        4. Metadata matching
        """

        #
        # -----------------------------------------------------
        # Strategy 1 : Explicit property references
        # -----------------------------------------------------
        #

        property_map = {
            "IMPLEMENTS": "requirement",
            "CONTAINS": "class",
            "INVOKES_API": "api",
            "INVOKES_DB": "database",
            "EXECUTES": "runtime",
        }

        property_name = property_map.get(relationship)

        if property_name:

            property_value = source.properties.get(property_name)

            if property_value:

                if property_value == target.node_id:
                    return True

                if str(property_value).lower() == target.name.lower():
                    return True

        #
        # -----------------------------------------------------
        # Strategy 2 : Labels
        # -----------------------------------------------------
        #

        if target.name in source.labels:
            return True

        #
        # -----------------------------------------------------
        # Strategy 3 : Tags
        # -----------------------------------------------------
        #

        if target.name in source.tags:
            return True

        #
        # -----------------------------------------------------
        # Strategy 4 : Metadata matching
        # -----------------------------------------------------
        #

        values = []

        values.append(source.name)

        values.extend(source.labels)

        values.extend(source.tags)

        values.extend(
            str(v)
            for v in source.properties.values()
        )

        target_name = target.name.lower()

        for value in values:

            if target_name in str(value).lower():
                return True

        return False

    # ---------------------------------------------------------

    @staticmethod
    def _description(
        relationship,
        source_name,
        target_name,
    ):

        return (
            f"{relationship}: "
            f"{source_name} -> {target_name}"
        )

    # ---------------------------------------------------------

    def statistics(self) -> Dict:
        """
        Returns simple detector statistics.
        """

        grouped = self._group_nodes_by_type()

        return {
            "node_types": {
                key: len(value)
                for key, value in grouped.items()
            },
            "rules": len(self.DETECTION_RULES),
        }
