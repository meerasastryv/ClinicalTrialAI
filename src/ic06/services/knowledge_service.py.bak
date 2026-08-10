"""
knowledge_service.py

Business service responsible for managing knowledge snapshots
and tracking knowledge evolution.
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from src.ic06.models.knowledge_snapshot import KnowledgeSnapshot
from src.ic06.repositories.learning_model_repository import (
    LearningModelRepository,
)


class KnowledgeService:
    """
    Service responsible for knowledge management.
    """

    def __init__(
        self,
        repository: Optional[LearningModelRepository] = None,
    ):
        self._repository = repository or LearningModelRepository()

    # ------------------------------------------------------------------
    # CRUD Operations
    # ------------------------------------------------------------------

    def save_snapshot(
        self,
        snapshot: KnowledgeSnapshot,
    ) -> KnowledgeSnapshot:
        """
        Store a knowledge snapshot.
        """
        self._repository.add(snapshot)
        return snapshot

    def get_snapshot(
        self,
        snapshot_id: str,
    ) -> Optional[KnowledgeSnapshot]:
        """
        Retrieve a snapshot by ID.
        """
        return self._repository.get(snapshot_id)

    def get_all_snapshots(self) -> List[KnowledgeSnapshot]:
        """
        Return all stored knowledge snapshots.
        """
        return self._repository.get_all()

    def delete_snapshot(
        self,
        snapshot_id: str,
    ) -> bool:
        """
        Delete a knowledge snapshot.
        """
        return self._repository.delete(snapshot_id)

    # ------------------------------------------------------------------
    # Version Management
    # ------------------------------------------------------------------

    def latest_snapshot(self) -> Optional[KnowledgeSnapshot]:
        """
        Return the most recent snapshot.
        """
        snapshots = self.get_all_snapshots()

        if not snapshots:
            return None

        return max(
            snapshots,
            key=lambda s: getattr(
                s,
                "timestamp",
                datetime.min,
            ),
        )

    # ------------------------------------------------------------------
    # Knowledge Evolution
    # ------------------------------------------------------------------

    def evolution(self) -> List[Dict]:
        """
        Return historical knowledge evolution.
        """

        snapshots = sorted(
            self.get_all_snapshots(),
            key=lambda s: getattr(
                s,
                "timestamp",
                datetime.min,
            ),
        )

        evolution = []

        for snapshot in snapshots:

            evolution.append(
                {
                    "snapshot_id": getattr(snapshot, "snapshot_id", None),
                    "timestamp": getattr(snapshot, "timestamp", None),
                    "confidence": getattr(snapshot, "confidence", 0.0),
                    "knowledge_size": getattr(
                        snapshot,
                        "knowledge_size",
                        0,
                    ),
                }
            )

        return evolution

    # ------------------------------------------------------------------
    # Knowledge Growth
    # ------------------------------------------------------------------

    def growth(self) -> Dict:
        """
        Calculate knowledge growth between first and latest snapshots.
        """

        snapshots = sorted(
            self.get_all_snapshots(),
            key=lambda s: getattr(
                s,
                "timestamp",
                datetime.min,
            ),
        )

        if len(snapshots) < 2:
            return {
                "knowledge_growth": 0,
                "confidence_growth": 0.0,
            }

        first = snapshots[0]
        last = snapshots[-1]

        return {
            "knowledge_growth": (
                getattr(last, "knowledge_size", 0)
                - getattr(first, "knowledge_size", 0)
            ),
            "confidence_growth": round(
                getattr(last, "confidence", 0.0)
                - getattr(first, "confidence", 0.0),
                3,
            ),
        }

    # ------------------------------------------------------------------
    # Knowledge Maturity
    # ------------------------------------------------------------------

    def maturity_score(self) -> float:
        """
        Estimate overall maturity.
        """

        snapshots = self.get_all_snapshots()

        if not snapshots:
            return 0.0

        return round(
            sum(
                getattr(
                    snapshot,
                    "confidence",
                    0.0,
                )
                for snapshot in snapshots
            )
            / len(snapshots),
            3,
        )

    # ------------------------------------------------------------------
    # Snapshot Comparison
    # ------------------------------------------------------------------

    def compare(
        self,
        first_id: str,
        second_id: str,
    ) -> Dict:
        """
        Compare two knowledge snapshots.
        """

        first = self.get_snapshot(first_id)
        second = self.get_snapshot(second_id)

        if first is None or second is None:
            return {}

        return {
            "knowledge_delta": (
                getattr(second, "knowledge_size", 0)
                - getattr(first, "knowledge_size", 0)
            ),
            "confidence_delta": round(
                getattr(second, "confidence", 0.0)
                - getattr(first, "confidence", 0.0),
                3,
            ),
        }

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(self) -> Dict:
        """
        Consolidated knowledge summary.
        """

        return {
            "total_snapshots": len(
                self.get_all_snapshots()
            ),
            "latest_snapshot": self.latest_snapshot(),
            "maturity_score": self.maturity_score(),
            "growth": self.growth(),
            "evolution": self.evolution(),
        }
