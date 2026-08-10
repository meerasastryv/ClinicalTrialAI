"""
usage_ingestion_service.py

Service responsible for ingesting customer usage events.
"""

from __future__ import annotations

from typing import List

from src.ic08.models.usage_event import UsageEvent
from src.ic08.repositories.usage_repository import UsageRepository


class UsageIngestionService:
    """
    Service for ingesting customer usage events.
    """

    def __init__(
        self,
        usage_repository: UsageRepository,
    ) -> None:
        self._repository = usage_repository

    def ingest_event(
        self,
        event: UsageEvent,
    ) -> bool:
        """
        Ingests a single usage event.

        Returns
        -------
        bool
            True if the event was successfully ingested.
        """
        if self._repository.event_exists(event.event_id):
            return False

        self._repository.add_event(event)
        return True

    def ingest_events(
        self,
        events: List[UsageEvent],
    ) -> int:
        """
        Ingests multiple usage events.

        Returns
        -------
        int
            Number of successfully ingested events.
        """
        ingested = 0

        for event in events:
            if self.ingest_event(event):
                ingested += 1

        return ingested

    def duplicate_count(
        self,
        events: List[UsageEvent],
    ) -> int:
        """
        Returns the number of duplicate events.
        """
        return sum(
            1
            for event in events
            if self._repository.event_exists(event.event_id)
        )

    def ingestion_summary(
        self,
        events: List[UsageEvent],
    ) -> dict[str, int]:
        """
        Returns an ingestion summary.
        """
        total = len(events)
        duplicates = self.duplicate_count(events)
        ingested = total - duplicates

        return {
            "total_events": total,
            "ingested_events": ingested,
            "duplicate_events": duplicates,
        }
