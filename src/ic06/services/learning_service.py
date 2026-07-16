"""
learning_service.py

Business service for managing learning events and analytics.

Responsibilities
----------------
* Record learning events
* Retrieve learning history
* Update confidence values
* Compute learning statistics
* Identify success/failure trends
* Measure learning velocity
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from src.ic06.models.learning_event import LearningEvent
from src.ic06.repositories.learning_repository import LearningRepository


class LearningService:
    """
    Business logic for adaptive learning events.
    """

    def __init__(self, repository: Optional[LearningRepository] = None):
        self._repository = repository or LearningRepository()

    # ------------------------------------------------------------------
    # CRUD Operations
    # ------------------------------------------------------------------

    def record_event(self, event: LearningEvent) -> LearningEvent:
        """
        Store a learning event.
        """
        self._repository.add(event)
        return event

    def get_event(self, event_id: str) -> Optional[LearningEvent]:
        """
        Retrieve a learning event.
        """
        return self._repository.get(event_id)

    def get_all_events(self) -> List[LearningEvent]:
        """
        Return every learning event.
        """
        return self._repository.get_all()

    def delete_event(self, event_id: str) -> bool:
        """
        Remove a learning event.
        """
        return self._repository.delete(event_id)

    # ------------------------------------------------------------------
    # Queries
    # ------------------------------------------------------------------

    def get_successful_events(self) -> List[LearningEvent]:
        return [
            e
            for e in self.get_all_events()
            if getattr(e, "success", False)
        ]

    def get_failed_events(self) -> List[LearningEvent]:
        return [
            e
            for e in self.get_all_events()
            if not getattr(e, "success", False)
        ]

    def find_by_source(self, source: str) -> List[LearningEvent]:
        return [
            e
            for e in self.get_all_events()
            if getattr(e, "source", None) == source
        ]

    # ------------------------------------------------------------------
    # Confidence
    # ------------------------------------------------------------------

    def update_confidence(
        self,
        event_id: str,
        confidence: float,
    ) -> bool:
        """
        Update confidence score for an event.
        """
        event = self.get_event(event_id)

        if event is None:
            return False

        event.confidence = max(0.0, min(1.0, confidence))

        if hasattr(event, "updated_at"):
            event.updated_at = datetime.utcnow()

        self._repository.update(event)

        return True

    # ------------------------------------------------------------------
    # Analytics
    # ------------------------------------------------------------------

    def learning_statistics(self) -> Dict:
        """
        Overall learning statistics.
        """
        events = self.get_all_events()

        total = len(events)

        successful = len(self.get_successful_events())
        failed = len(self.get_failed_events())

        success_rate = (
            successful / total if total else 0.0
        )

        average_confidence = (
            sum(getattr(e, "confidence", 0.0) for e in events)
            / total
            if total
            else 0.0
        )

        return {
            "total_events": total,
            "successful_events": successful,
            "failed_events": failed,
            "success_rate": round(success_rate, 3),
            "average_confidence": round(
                average_confidence,
                3,
            ),
        }

    def confidence_growth(self) -> List[float]:
        """
        Historical confidence progression.
        """
        events = sorted(
            self.get_all_events(),
            key=lambda e: getattr(
                e,
                "timestamp",
                datetime.min,
            ),
        )

        return [
            getattr(e, "confidence", 0.0)
            for e in events
        ]

    def learning_velocity(self) -> float:
        """
        Average learning events per day.
        """
        events = self.get_all_events()

        if len(events) < 2:
            return float(len(events))

        ordered = sorted(
            events,
            key=lambda e: getattr(
                e,
                "timestamp",
                datetime.utcnow(),
            ),
        )

        start = getattr(
            ordered[0],
            "timestamp",
            datetime.utcnow(),
        )

        end = getattr(
            ordered[-1],
            "timestamp",
            datetime.utcnow(),
        )

        days = max(
            (end - start).days,
            1,
        )

        return round(
            len(events) / days,
            2,
        )

    def success_trend(self) -> Dict[str, int]:
        """
        Success vs failure counts.
        """
        return {
            "success": len(self.get_successful_events()),
            "failure": len(self.get_failed_events()),
        }

    # ------------------------------------------------------------------
    # Reporting
    # ------------------------------------------------------------------

    def summary(self) -> Dict:
        """
        Consolidated learning summary.
        """
        return {
            "statistics": self.learning_statistics(),
            "confidence_growth": self.confidence_growth(),
            "learning_velocity": self.learning_velocity(),
            "trend": self.success_trend(),
        }
