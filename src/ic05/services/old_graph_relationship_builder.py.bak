"""
graph_relationship_builder.py

Creates validated Relationship objects and stores them in the
RelationshipRepository.

This builder is responsible for:

- Relationship creation
- Validation
- Duplicate prevention
- Confidence assignment
- Deterministic relationship IDs
"""

from __future__ import annotations

import hashlib
from datetime import datetime
from typing import Iterable, List, Optional

from src.ic05.models.relationship import Relationship
from src.ic05.services.relationship_repository import RelationshipRepository


class GraphRelationshipBuilder:
    """
    Builds graph relationships from detected graph connections.
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

    def __init__(self,
                 repository: Optional[RelationshipRepository] = None):
        self._repository = repository or RelationshipRepository()

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    @property
    def repository(self) -> RelationshipRepository:
        return self._repository

    def build_relationship(
        self,
        source_id: str,
        target_id: str,
        relationship_type: str,
        description: str = "",
        confidence: Optional[float] = None,
    ) -> Relationship:
        """
        Build and store a single relationship.
        """

        self.validate_relationship(
            source_id,
            target_id,
            relationship_type,
        )

        relationship_id = self.generate_relationship_id(
            source_id,
            target_id,
            relationship_type,
        )

        existing = self._repository.get_relationship(relationship_id)
        if existing:
            return existing

        relationship = Relationship(
            id=relationship_id,
            source_id=source_id,
            target_id=target_id,
            relationship_type=relationship_type,
            confidence=(
                confidence
                if confidence is not None
                else self.default_confidence(relationship_type)
            ),
            description=description,
            created_at=datetime.utcnow(),
        )

        self._repository.add_relationship(relationship)

        return relationship

    def build_relationships(
        self,
        relationships: Iterable[dict],
    ) -> List[Relationship]:
        """
        Build multiple relationships.
        """

        built = []

        for item in relationships:

            relationship = self.build_relationship(
                source_id=item["source_id"],
                target_id=item["target_id"],
                relationship_type=item["relationship_type"],
                description=item.get("description", ""),
                confidence=item.get("confidence"),
            )

            built.append(relationship)

        return built

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def validate_relationship(
        self,
        source_id: str,
        target_id: str,
        relationship_type: str,
    ) -> None:

        if not source_id:
            raise ValueError("Source ID cannot be empty.")

        if not target_id:
            raise ValueError("Target ID cannot be empty.")

        if source_id == target_id:
            raise ValueError(
                "Source and Target cannot be identical."
            )

        if not relationship_type:
            raise ValueError(
                "Relationship type cannot be empty."
            )

    # ------------------------------------------------------------------
    # Duplicate Detection
    # ------------------------------------------------------------------

    def relationship_exists(
        self,
        source_id: str,
        target_id: str,
        relationship_type: str,
    ) -> bool:

        relationship_id = self.generate_relationship_id(
            source_id,
            target_id,
            relationship_type,
        )

        return (
            self._repository.get_relationship(
                relationship_id
            )
            is not None
        )

    # ------------------------------------------------------------------
    # ID Generation
    # ------------------------------------------------------------------

    @staticmethod
    def generate_relationship_id(
        source_id: str,
        target_id: str,
        relationship_type: str,
    ) -> str:
        """
        Generate deterministic relationship ID.
        """

        key = (
            f"{source_id}|"
            f"{relationship_type}|"
            f"{target_id}"
        )

        digest = hashlib.sha1(
            key.encode("utf-8")
        ).hexdigest()[:12]

        return f"REL-{digest.upper()}"

    # ------------------------------------------------------------------
    # Confidence
    # ------------------------------------------------------------------

    def default_confidence(
        self,
        relationship_type: str,
    ) -> float:

        return self.DEFAULT_CONFIDENCE.get(
            relationship_type,
            0.80,
        )

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def statistics(self):

        return self._repository.get_statistics()
