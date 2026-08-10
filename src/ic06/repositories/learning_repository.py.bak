"""
learning_repository.py

Adaptive Learning Engine

Repository for LearningEvent objects.

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

from src.ic06.models.learning_event import (
    LearningEvent,
    LearningEventType,
)


class LearningRepository:
    """
    Repository for LearningEvent objects.
    """

    def __init__(self) -> None:

        self._events: Dict[str, LearningEvent] = {}

    # ------------------------------------------------------------------
    # CRUD
    # ------------------------------------------------------------------

    def add(
        self,
        event: LearningEvent,
    ) -> None:
        """
        Adds a learning event.
        """
        self._events[event.event_id] = event

    def update(
        self,
        event: LearningEvent,
    ) -> None:
        """
        Updates an existing event.
        """
        self._events[event.event_id] = event

    def remove(
        self,
        event_id: str,
    ) -> bool:
        """
        Removes an event.

        Returns
        -------
        bool
            True if removed.
        """
        return (
            self._events.pop(event_id, None)
            is not None
        )
    def delete(self,event_id: str,) -> bool:
        """
        Alias for remove().
        """
        return self.remove(event_id)
    def get(
        self,
        event_id: str,
    ) -> Optional[LearningEvent]:
        """
        Returns an event.
        """
        return self._events.get(event_id)

    def exists(
        self,
        event_id: str,
    ) -> bool:
        """
        Returns True if the event exists.
        """
        return event_id in self._events

    def clear(self) -> None:
        """
        Removes all events.
        """
        self._events.clear()

    # ------------------------------------------------------------------
    # Collection
    # ------------------------------------------------------------------

    def get_all(self) -> List[LearningEvent]:
        """
        Returns all events.
        """
        return list(self._events.values())

    def count(self) -> int:
        """
        Returns repository size.
        """
        return len(self._events)


    # ------------------------------------------------------------------
    # Search
    # ------------------------------------------------------------------

    def find_by_type(
        self,
        event_type: LearningEventType,
    ) -> List[LearningEvent]:
        """
        Returns all events of the specified type.
        """
        return [
            event
            for event in self._events.values()
            if event.event_type == event_type
        ]

    def find_by_source(
        self,
        source: str,
    ) -> List[LearningEvent]:
        """
        Returns all events from the specified source.
        """
        return [
            event
            for event in self._events.values()
            if event.source.lower() == source.lower()
        ]

    def find_successful(self) -> List[LearningEvent]:
        """
        Returns all successful learning events.
        """
        return [
            event
            for event in self._events.values()
            if event.success
        ]

    def find_failed(self) -> List[LearningEvent]:
        """
        Returns all failed learning events.
        """
        return [
            event
            for event in self._events.values()
            if not event.success
        ]

    def find_by_confidence(
        self,
        minimum_confidence: float,
    ) -> List[LearningEvent]:
        """
        Returns all events with confidence greater than or equal
        to the specified threshold.
        """
        return [
            event
            for event in self._events.values()
            if event.confidence >= minimum_confidence
        ]

    # ------------------------------------------------------------------
    # Sorting
    # ------------------------------------------------------------------

    def sort_by_timestamp(
        self,
        reverse: bool = False,
    ) -> List[LearningEvent]:
        """
        Returns events sorted by timestamp.
        """
        return sorted(
            self._events.values(),
            key=lambda event: event.timestamp,
            reverse=reverse,
        )

    def sort_by_confidence(
        self,
        reverse: bool = True,
    ) -> List[LearningEvent]:
        """
        Returns events sorted by confidence.
        """
        return sorted(
            self._events.values(),
            key=lambda event: event.confidence,
            reverse=reverse,
        )

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def event_type_counts(self) -> Dict[str, int]:
        """
        Returns the number of events by event type.
        """
        counts: Dict[str, int] = {}

        for event in self._events.values():
            event_type = event.event_type.value
            counts[event_type] = counts.get(event_type, 0) + 1

        return counts

    def average_confidence(self) -> float:
        """
        Returns the average confidence score.
        """
        if not self._events:
            return 0.0

        total = sum(
            event.confidence
            for event in self._events.values()
        )

        return total / len(self._events)

    def success_rate(self) -> float:
        """
        Returns the percentage of successful events.
        """
        if not self._events:
            return 0.0

        successful = sum(
            1
            for event in self._events.values()
            if event.success
        )

        return (
            successful / len(self._events)
        ) * 100.0


    # ------------------------------------------------------------------
    # Import / Export
    # ------------------------------------------------------------------

    def export_to_json(
        self,
        file_path: str,
    ) -> None:
        """
        Exports all learning events to a JSON file.

        Args:
            file_path:
                Destination JSON file.
        """
        data = [
            event.to_dict()
            for event in self.get_all()
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
        Imports learning events from a JSON file.

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
            event = LearningEvent.from_dict(item)
            self.add(event)

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(self) -> Dict[str, object]:
        """
        Returns repository summary statistics.
        """
        return {
            "total_events": self.count(),
            "successful_events": len(
                self.find_successful()
            ),
            "failed_events": len(
                self.find_failed()
            ),
            "average_confidence":
                self.average_confidence(),
            "success_rate":
                self.success_rate(),
            "event_type_counts":
                self.event_type_counts(),
        }

    # ------------------------------------------------------------------
    # Special Methods
    # ------------------------------------------------------------------

    def __len__(self) -> int:
        """
        Returns the number of stored events.
        """
        return self.count()

    def __iter__(self):
        """
        Iterates over stored events.
        """
        return iter(
            self._events.values()
        )

    def __contains__(
        self,
        event_id: str,
    ) -> bool:
        """
        Returns True if the repository contains the event.
        """
        return self.exists(event_id)

    def __str__(self) -> str:
        """
        Human-readable representation.
        """
        return (
            f"LearningRepository("
            f"events={self.count()}, "
            f"success_rate={self.success_rate():.2f}%, "
            f"average_confidence="
            f"{self.average_confidence():.2f})"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """
        return self.__str__()


