"""
pattern_repository.py

Adaptive Learning Engine

Repository for LearningPattern objects.

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

from src.ic06.models.learning_pattern import (
    LearningPattern,
    PatternStatus,
    PatternType,
)


class PatternRepository:
    """
    Repository for LearningPattern objects.
    """

    def __init__(self) -> None:

        self._patterns: Dict[str, LearningPattern] = {}

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def add(
        self,
        pattern: LearningPattern,
    ) -> None:
        """
        Adds a learning pattern.
        """
        self._patterns[pattern.pattern_id] = pattern

    def update(
        self,
        pattern: LearningPattern,
    ) -> None:
        """
        Updates an existing learning pattern.
        """
        self._patterns[pattern.pattern_id] = pattern

    def remove(
        self,
        pattern_id: str,
    ) -> bool:
        """
        Removes a learning pattern.

        Returns
        -------
        bool
            True if removed.
        """
        return (
            self._patterns.pop(pattern_id, None)
            is not None
        )

    def get(
        self,
        pattern_id: str,
    ) -> Optional[LearningPattern]:
        """
        Returns a learning pattern.
        """
        return self._patterns.get(pattern_id)

    def exists(
        self,
        pattern_id: str,
    ) -> bool:
        """
        Returns True if the pattern exists.
        """
        return pattern_id in self._patterns

    def clear(self) -> None:
        """
        Removes all patterns.
        """
        self._patterns.clear()

    # ------------------------------------------------------------------
    # Collection
    # ------------------------------------------------------------------

    def get_all(self) -> List[LearningPattern]:
        """
        Returns all learning patterns.
        """
        return list(self._patterns.values())

    def count(self) -> int:
        """
        Returns repository size.
        """
        return len(self._patterns)

    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------

    def find_by_type(
        self,
        pattern_type: PatternType,
    ) -> List[LearningPattern]:
        """
        Returns all patterns of the specified type.
        """
        return [
            pattern
            for pattern in self._patterns.values()
            if pattern.pattern_type == pattern_type
        ]

    def find_by_status(
        self,
        status: PatternStatus,
    ) -> List[LearningPattern]:
        """
        Returns all patterns with the specified status.
        """
        return [
            pattern
            for pattern in self._patterns.values()
            if pattern.status == status
        ]

    def find_active(self) -> List[LearningPattern]:
        """
        Returns all active patterns.
        """
        return self.find_by_status(
            PatternStatus.ACTIVE
        )

    def find_stable(self) -> List[LearningPattern]:
        """
        Returns all stable patterns.
        """
        return self.find_by_status(
            PatternStatus.STABLE
        )

    def find_high_confidence(
        self,
        minimum_confidence: float,
    ) -> List[LearningPattern]:
        """
        Returns all patterns with confidence greater than or equal
        to the specified threshold.
        """
        return [
            pattern
            for pattern in self._patterns.values()
            if pattern.confidence >= minimum_confidence
        ]

    # ------------------------------------------------------------------
    # Sorting
    # ------------------------------------------------------------------

    def sort_by_confidence(
        self,
        reverse: bool = True,
    ) -> List[LearningPattern]:
        """
        Returns patterns sorted by confidence.
        """
        return sorted(
            self._patterns.values(),
            key=lambda pattern: pattern.confidence,
            reverse=reverse,
        )

    def sort_by_occurrences(
        self,
        reverse: bool = True,
    ) -> List[LearningPattern]:
        """
        Returns patterns sorted by occurrence count.
        """
        return sorted(
            self._patterns.values(),
            key=lambda pattern: pattern.occurrences,
            reverse=reverse,
        )

    def sort_by_last_seen(
        self,
        reverse: bool = True,
    ) -> List[LearningPattern]:
        """
        Returns patterns sorted by last seen timestamp.
        """
        return sorted(
            self._patterns.values(),
            key=lambda pattern: pattern.last_seen,
            reverse=reverse,
        )

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def pattern_type_counts(self) -> Dict[str, int]:
        """
        Returns the number of patterns by type.
        """
        counts: Dict[str, int] = {}

        for pattern in self._patterns.values():
            pattern_type = pattern.pattern_type.value
            counts[pattern_type] = (
                counts.get(pattern_type, 0) + 1
            )

        return counts

    def status_counts(self) -> Dict[str, int]:
        """
        Returns the number of patterns by status.
        """
        counts: Dict[str, int] = {}

        for pattern in self._patterns.values():
            status = pattern.status.value
            counts[status] = (
                counts.get(status, 0) + 1
            )

        return counts

    def average_confidence(self) -> float:
        """
        Returns the average confidence score.
        """
        if not self._patterns:
            return 0.0

        total = sum(
            pattern.confidence
            for pattern in self._patterns.values()
        )

        return total / len(self._patterns)

    def total_occurrences(self) -> int:
        """
        Returns the total number of observed occurrences.
        """
        return sum(
            pattern.occurrences
            for pattern in self._patterns.values()
        )

    # ------------------------------------------------------------------
    # Import / Export
    # ------------------------------------------------------------------

    def export_to_json(
        self,
        file_path: str,
    ) -> None:
        """
        Exports all learning patterns to a JSON file.

        Args:
            file_path:
                Destination JSON file.
        """
        data = [
            pattern.to_dict()
            for pattern in self.get_all()
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
        Imports learning patterns from a JSON file.

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
            pattern = LearningPattern.from_dict(item)
            self.add(pattern)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(self) -> Dict[str, object]:
        """
        Returns repository summary statistics.
        """
        return {
            "total_patterns": self.count(),
            "active_patterns": len(
                self.find_active()
            ),
            "stable_patterns": len(
                self.find_stable()
            ),
            "average_confidence":
                self.average_confidence(),
            "total_occurrences":
                self.total_occurrences(),
            "pattern_type_counts":
                self.pattern_type_counts(),
            "status_counts":
                self.status_counts(),
        }

    # ------------------------------------------------------------------
    # Special Methods
    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """
        Returns the number of stored patterns.
        """
        return self.count()

    def __iter__(self):
        """
        Iterates over stored patterns.
        """
        return iter(
            self._patterns.values()
        )

    def __contains__(
        self,
        pattern_id: str,
    ) -> bool:
        """
        Returns True if the repository contains the pattern.
        """
        return self.exists(pattern_id)

    def __str__(self) -> str:
        """
        Human-readable representation.
        """
        return (
            f"PatternRepository("
            f"patterns={self.count()}, "
            f"average_confidence="
            f"{self.average_confidence():.2f}, "
            f"total_occurrences="
            f"{self.total_occurrences()})"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """
        return self.__str__()


