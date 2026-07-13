"""
relationship_repository.py

Repository for storing and querying graph relationships.
"""

from __future__ import annotations

from collections import defaultdict
from typing import Dict, List, Optional


class RelationshipRepository:
    """
    Repository that stores all graph relationships.

    Relationships are expected to expose at least:
        - id
        - source_id
        - target_id
        - relationship_type
    """

    def __init__(self):
        self._relationships: Dict[str, object] = {}

        self._by_source = defaultdict(list)
        self._by_target = defaultdict(list)
        self._by_type = defaultdict(list)

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def add_relationship(self, relationship) -> None:
        """
        Add a relationship to the repository.
        """

        if relationship.id in self._relationships:
            return

        self._relationships[relationship.id] = relationship

        self._by_source[relationship.source_id].append(relationship)

        self._by_target[relationship.target_id].append(relationship)

        self._by_type[relationship.relationship_type].append(relationship)

    def remove_relationship(self, relationship_id: str) -> bool:
        """
        Remove a relationship from the repository.
        """

        relationship = self._relationships.pop(relationship_id, None)

        if relationship is None:
            return False

        if relationship in self._by_source.get(relationship.source_id, []):
            self._by_source[relationship.source_id].remove(relationship)

        if relationship in self._by_target.get(relationship.target_id, []):
            self._by_target[relationship.target_id].remove(relationship)

        if relationship in self._by_type.get(relationship.relationship_type, []):
            self._by_type[relationship.relationship_type].remove(relationship)

        return True

    # ------------------------------------------------------------------
    # Getters
    # ------------------------------------------------------------------

    def get_relationship(self, relationship_id: str):
        return self._relationships.get(relationship_id)

    def get_all_relationships(self) -> List:
        return list(self._relationships.values())

    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------

    def find_by_source(self, source_id: str) -> List:
        return list(self._by_source.get(source_id, []))

    def find_by_target(self, target_id: str) -> List:
        return list(self._by_target.get(target_id, []))

    def find_by_type(self, relationship_type: str) -> List:
        return list(self._by_type.get(relationship_type, []))

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def relationship_count(self) -> int:
        return len(self._relationships)

    def relationship_type_counts(self) -> Dict[str, int]:
        return {
            relationship_type: len(relationships)
            for relationship_type, relationships in self._by_type.items()
        }

    def get_statistics(self) -> Dict:
        return {
            "total_relationships": self.relationship_count(),
            "relationship_types": self.relationship_type_counts(),
            "unique_sources": len(self._by_source),
            "unique_targets": len(self._by_target),
        }

    # ------------------------------------------------------------------
    # Utility
    # ------------------------------------------------------------------

    def clear(self) -> None:
        self._relationships.clear()
        self._by_source.clear()
        self._by_target.clear()
        self._by_type.clear()

    def __len__(self):
        return len(self._relationships)

    def __contains__(self, relationship_id: str):
        return relationship_id in self._relationships
