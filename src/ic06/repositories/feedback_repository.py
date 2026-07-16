"""
feedback_repository.py

Adaptive Learning Engine

Repository for FeedbackRecord objects.

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

from src.ic06.models.feedback_record import (
    FeedbackOutcome,
    FeedbackRecord,
    FeedbackStatus,
    FeedbackType,
)


class FeedbackRepository:
    """
    Repository for FeedbackRecord objects.
    """

    def __init__(self) -> None:

        self._feedback_records: Dict[str, FeedbackRecord] = {}

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def add(
        self,
        feedback: FeedbackRecord,
    ) -> None:
        """
        Adds a feedback record.
        """
        self._feedback_records[feedback.feedback_id] = feedback

    def update(
        self,
        feedback: FeedbackRecord,
    ) -> None:
        """
        Updates an existing feedback record.
        """
        self._feedback_records[feedback.feedback_id] = feedback

    def remove(
        self,
        feedback_id: str,
    ) -> bool:
        """
        Removes a feedback record.

        Returns
        -------
        bool
            True if removed.
        """
        return (
            self._feedback_records.pop(
                feedback_id,
                None,
            )
            is not None
        )

    def get(
        self,
        feedback_id: str,
    ) -> Optional[FeedbackRecord]:
        """
        Returns a feedback record.
        """
        return self._feedback_records.get(
            feedback_id
        )

    def exists(
        self,
        feedback_id: str,
    ) -> bool:
        """
        Returns True if the feedback record exists.
        """
        return (
            feedback_id
            in self._feedback_records
        )

    def clear(self) -> None:
        """
        Removes all feedback records.
        """
        self._feedback_records.clear()

    # ------------------------------------------------------------------
    # Collection
    # ------------------------------------------------------------------

    def get_all(self) -> List[FeedbackRecord]:
        """
        Returns all feedback records.
        """
        return list(
            self._feedback_records.values()
        )

    def count(self) -> int:
        """
        Returns repository size.
        """
        return len(
            self._feedback_records
        )

    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------

    def find_by_type(
        self,
        feedback_type: FeedbackType,
    ) -> List[FeedbackRecord]:
        """
        Returns all feedback records of the specified type.
        """
        return [
            feedback
            for feedback in self._feedback_records.values()
            if feedback.feedback_type == feedback_type
        ]

    def find_by_status(
        self,
        status: FeedbackStatus,
    ) -> List[FeedbackRecord]:
        """
        Returns all feedback records with the specified status.
        """
        return [
            feedback
            for feedback in self._feedback_records.values()
            if feedback.status == status
        ]

    def find_by_outcome(
        self,
        outcome: FeedbackOutcome,
    ) -> List[FeedbackRecord]:
        """
        Returns all feedback records with the specified outcome.
        """
        return [
            feedback
            for feedback in self._feedback_records.values()
            if feedback.outcome == outcome
        ]

    def find_positive(self) -> List[FeedbackRecord]:
        """
        Returns all positive feedback records.
        """
        return self.find_by_outcome(
            FeedbackOutcome.POSITIVE
        )

    def find_negative(self) -> List[FeedbackRecord]:
        """
        Returns all negative feedback records.
        """
        return self.find_by_outcome(
            FeedbackOutcome.NEGATIVE
        )

    def find_neutral(self) -> List[FeedbackRecord]:
        """
        Returns all neutral feedback records.
        """
        return self.find_by_outcome(
            FeedbackOutcome.NEUTRAL
        )

    def find_processed(self) -> List[FeedbackRecord]:
        """
        Returns all processed feedback records.
        """
        return self.find_by_status(
            FeedbackStatus.PROCESSED
        )

    # ------------------------------------------------------------------
    # Sorting
    # ------------------------------------------------------------------

    def sort_by_timestamp(
        self,
        reverse: bool = True,
    ) -> List[FeedbackRecord]:
        """
        Returns feedback records sorted by timestamp.
        """
        return sorted(
            self._feedback_records.values(),
            key=lambda feedback: feedback.timestamp,
            reverse=reverse,
        )

    def sort_by_rating(
        self,
        reverse: bool = True,
    ) -> List[FeedbackRecord]:
        """
        Returns feedback records sorted by rating.
        """
        return sorted(
            self._feedback_records.values(),
            key=lambda feedback: feedback.rating,
            reverse=reverse,
        )

    def sort_by_learning_delta(
        self,
        reverse: bool = True,
    ) -> List[FeedbackRecord]:
        """
        Returns feedback records sorted by learning delta.
        """
        return sorted(
            self._feedback_records.values(),
            key=lambda feedback: feedback.learning_delta,
            reverse=reverse,
        )

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def feedback_type_counts(self) -> Dict[str, int]:
        """
        Returns the number of feedback records by type.
        """
        counts: Dict[str, int] = {}

        for feedback in self._feedback_records.values():
            feedback_type = feedback.feedback_type.value
            counts[feedback_type] = (
                counts.get(feedback_type, 0) + 1
            )

        return counts

    def outcome_counts(self) -> Dict[str, int]:
        """
        Returns the number of feedback records by outcome.
        """
        counts: Dict[str, int] = {}

        for feedback in self._feedback_records.values():
            outcome = feedback.outcome.value
            counts[outcome] = (
                counts.get(outcome, 0) + 1
            )

        return counts

    def average_rating(self) -> float:
        """
        Returns the average feedback rating.
        """
        if not self._feedback_records:
            return 0.0

        total = sum(
            feedback.rating
            for feedback in self._feedback_records.values()
        )

        return total / len(self._feedback_records)

    def average_learning_delta(self) -> float:
        """
        Returns the average learning delta.
        """
        if not self._feedback_records:
            return 0.0

        total = sum(
            feedback.learning_delta
            for feedback in self._feedback_records.values()
        )

        return total / len(self._feedback_records)

    def average_confidence_improvement(self) -> float:
        """
        Returns the average confidence improvement.
        """
        if not self._feedback_records:
            return 0.0

        total = sum(
            feedback.confidence_after
            - feedback.confidence_before
            for feedback in self._feedback_records.values()
        )

        return total / len(self._feedback_records)

    # ------------------------------------------------------------------
    # Import / Export
    # ------------------------------------------------------------------

    def export_to_json(
        self,
        file_path: str,
    ) -> None:
        """
        Exports all feedback records to a JSON file.

        Args:
            file_path:
                Destination JSON file.
        """
        data = [
            feedback.to_dict()
            for feedback in self.get_all()
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
        Imports feedback records from a JSON file.

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
            feedback = FeedbackRecord.from_dict(item)
            self.add(feedback)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(self) -> Dict[str, object]:
        """
        Returns repository summary statistics.
        """
        return {
            "total_feedback": self.count(),
            "positive_feedback": len(
                self.find_positive()
            ),
            "negative_feedback": len(
                self.find_negative()
            ),
            "neutral_feedback": len(
                self.find_neutral()
            ),
            "processed_feedback": len(
                self.find_processed()
            ),
            "average_rating":
                self.average_rating(),
            "average_learning_delta":
                self.average_learning_delta(),
            "average_confidence_improvement":
                self.average_confidence_improvement(),
            "feedback_type_counts":
                self.feedback_type_counts(),
            "outcome_counts":
                self.outcome_counts(),
        }

    # ------------------------------------------------------------------
    # Special Methods
    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """
        Returns the number of stored feedback records.
        """
        return self.count()

    def __iter__(self):
        """
        Iterates over stored feedback records.
        """
        return iter(
            self._feedback_records.values()
        )

    def __contains__(
        self,
        feedback_id: str,
    ) -> bool:
        """
        Returns True if the repository contains the feedback record.
        """
        return self.exists(feedback_id)

    def __str__(self) -> str:
        """
        Human-readable representation.
        """
        return (
            f"FeedbackRepository("
            f"feedback={self.count()}, "
            f"average_rating="
            f"{self.average_rating():.2f}, "
            f"average_learning_delta="
            f"{self.average_learning_delta():.2f})"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """
        return self.__str__()
