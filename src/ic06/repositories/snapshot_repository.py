"""
snapshot_repository.py

Adaptive Learning Engine

Repository for KnowledgeSnapshot objects.

Provides:

- Storage
- CRUD operations
- Search
- Statistics
- Import/Export
- Filtering

Author: Meera Sastry
Project: ClinicalTrialAI
"""

from __future__ import annotations

import json

from pathlib import Path
from typing import Dict, List, Optional

from src.ic06.models.knowledge_snapshot import (
    KnowledgeSnapshot,
    SnapshotStatus,
    SnapshotType,
)


class SnapshotRepository:
    """
    Repository for KnowledgeSnapshot objects.
    """

    def __init__(self) -> None:

        self._snapshots: Dict[str, KnowledgeSnapshot] = {}

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def add(
        self,
        snapshot: KnowledgeSnapshot,
    ) -> None:
        """
        Adds a knowledge snapshot.
        """
        self._snapshots[snapshot.snapshot_id] = snapshot

    def update(
        self,
        snapshot: KnowledgeSnapshot,
    ) -> None:
        """
        Updates an existing knowledge snapshot.
        """
        self._snapshots[snapshot.snapshot_id] = snapshot

    def remove(
        self,
        snapshot_id: str,
    ) -> bool:
        """
        Removes a knowledge snapshot.

        Returns
        -------
        bool
            True if removed.
        """
        return (
            self._snapshots.pop(snapshot_id, None)
            is not None
        )

    def get(
        self,
        snapshot_id: str,
    ) -> Optional[KnowledgeSnapshot]:
        """
        Returns a knowledge snapshot.
        """
        return self._snapshots.get(snapshot_id)

    def exists(
        self,
        snapshot_id: str,
    ) -> bool:
        """
        Returns True if the snapshot exists.
        """
        return snapshot_id in self._snapshots

    def clear(self) -> None:
        """
        Removes all snapshots.
        """
        self._snapshots.clear()

    # ------------------------------------------------------------------
    # Collection
    # ------------------------------------------------------------------

    def get_all(self) -> List[KnowledgeSnapshot]:
        """
        Returns all knowledge snapshots.
        """
        return list(self._snapshots.values())

    def count(self) -> int:
        """
        Returns repository size.
        """
        return len(self._snapshots)


    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------

    def find_by_type(
        self,
        snapshot_type: SnapshotType,
    ) -> List[KnowledgeSnapshot]:
        """
        Returns all snapshots of the specified type.
        """
        return [
            snapshot
            for snapshot in self._snapshots.values()
            if snapshot.snapshot_type == snapshot_type
        ]

    def find_by_status(
        self,
        status: SnapshotStatus,
    ) -> List[KnowledgeSnapshot]:
        """
        Returns all snapshots with the specified status.
        """
        return [
            snapshot
            for snapshot in self._snapshots.values()
            if snapshot.status == status
        ]

    def find_by_version(
        self,
        version: str,
    ) -> List[KnowledgeSnapshot]:
        """
        Returns all snapshots matching the specified version.
        """
        return [
            snapshot
            for snapshot in self._snapshots.values()
            if snapshot.version == version
        ]

    def find_latest(self) -> Optional[KnowledgeSnapshot]:
        """
        Returns the most recently created snapshot.
        """
        if not self._snapshots:
            return None

        return max(
            self._snapshots.values(),
            key=lambda snapshot: snapshot.created_at,
        )

    def find_latest_active(self) -> Optional[KnowledgeSnapshot]:
        """
        Returns the latest active snapshot.
        """
        active_snapshots = self.find_by_status(
            SnapshotStatus.ACTIVE
        )

        if not active_snapshots:
            return None

        return max(
            active_snapshots,
            key=lambda snapshot: snapshot.created_at,
        )

    # ------------------------------------------------------------------
    # Sorting
    # ------------------------------------------------------------------

    def sort_by_created_at(
        self,
        reverse: bool = True,
    ) -> List[KnowledgeSnapshot]:
        """
        Returns snapshots sorted by creation time.
        """
        return sorted(
            self._snapshots.values(),
            key=lambda snapshot: snapshot.created_at,
            reverse=reverse,
        )

    def sort_by_learning_score(
        self,
        reverse: bool = True,
    ) -> List[KnowledgeSnapshot]:
        """
        Returns snapshots sorted by learning score.
        """
        return sorted(
            self._snapshots.values(),
            key=lambda snapshot: snapshot.learning_score,
            reverse=reverse,
        )

    def sort_by_confidence(
        self,
        reverse: bool = True,
    ) -> List[KnowledgeSnapshot]:
        """
        Returns snapshots sorted by average confidence.
        """
        return sorted(
            self._snapshots.values(),
            key=lambda snapshot: snapshot.average_confidence,
            reverse=reverse,
        )

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def snapshot_type_counts(self) -> Dict[str, int]:
        """
        Returns the number of snapshots by type.
        """
        counts: Dict[str, int] = {}

        for snapshot in self._snapshots.values():
            snapshot_type = snapshot.snapshot_type.value
            counts[snapshot_type] = (
                counts.get(snapshot_type, 0) + 1
            )

        return counts

    def status_counts(self) -> Dict[str, int]:
        """
        Returns the number of snapshots by status.
        """
        counts: Dict[str, int] = {}

        for snapshot in self._snapshots.values():
            status = snapshot.status.value
            counts[status] = (
                counts.get(status, 0) + 1
            )

        return counts

    def average_learning_score(self) -> float:
        """
        Returns the average learning score.
        """
        if not self._snapshots:
            return 0.0

        total = sum(
            snapshot.learning_score
            for snapshot in self._snapshots.values()
        )

        return total / len(self._snapshots)

    def average_confidence(self) -> float:
        """
        Returns the average confidence score.
        """
        if not self._snapshots:
            return 0.0

        total = sum(
            snapshot.average_confidence
            for snapshot in self._snapshots.values()
        )

        return total / len(self._snapshots)


    # ------------------------------------------------------------------
    # Import / Export
    # ------------------------------------------------------------------

    def export_to_json(
        self,
        file_path: str,
    ) -> None:
        """
        Exports all knowledge snapshots to a JSON file.

        Args:
            file_path:
                Destination JSON file.
        """
        data = [
            snapshot.to_dict()
            for snapshot in self.get_all()
        ]

        with open(
            file_path,
            "w",
            encoding="utf-8",
        ) as file:
            json.dump(
                data,
                file,
                indent=4,
                ensure_ascii=False,
            )

    def import_from_json(
        self,
        file_path: str,
    ) -> None:
        """
        Imports knowledge snapshots from a JSON file.

        Args:
            file_path:
                Source JSON file.
        """
        path = Path(file_path)

        if not path.exists():
            raise FileNotFoundError(file_path)

        with open(
            path,
            "r",
            encoding="utf-8",
        ) as file:
            data = json.load(file)

        self.clear()

        for item in data:
            snapshot = KnowledgeSnapshot.from_dict(item)
            self.add(snapshot)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(self) -> Dict[str, object]:
        """
        Returns repository summary statistics.
        """
        latest = self.find_latest()

        return {
            "total_snapshots": self.count(),
            "latest_snapshot":
                latest.name if latest else None,
            "average_learning_score":
                self.average_learning_score(),
            "average_confidence":
                self.average_confidence(),
            "snapshot_type_counts":
                self.snapshot_type_counts(),
            "status_counts":
                self.status_counts(),
        }

    # ------------------------------------------------------------------
    # Special Methods
    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """
        Returns the number of stored snapshots.
        """
        return self.count()

    def __iter__(self):
        """
        Iterates over stored snapshots.
        """
        return iter(
            self._snapshots.values()
        )

    def __contains__(
        self,
        snapshot_id: str,
    ) -> bool:
        """
        Returns True if the repository contains the snapshot.
        """
        return self.exists(snapshot_id)

    def __str__(self) -> str:
        """
        Human-readable representation.
        """
        return (
            f"SnapshotRepository("
            f"snapshots={self.count()}, "
            f"average_learning_score="
            f"{self.average_learning_score():.2f}, "
            f"average_confidence="
            f"{self.average_confidence():.2f})"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """
        return self.__str__()


