"""
usage_event_service.py

Service responsible for recording and querying usage events.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from src.ic08.models.usage_event import UsageEvent
from src.ic08.repositories.usage_repository import UsageRepository


class UsageEventService:
    """
    Service for managing customer usage events.
    """

    def __init__(
        self,
        usage_repository: UsageRepository,
    ) -> None:
        self._repository = usage_repository

    def record_event(
        self,
        event: UsageEvent,
    ) -> None:
        """
        Records a usage event.
        """
        self._repository.add_event(event)

    def get_event(
        self,
        event_id: str,
    ) -> Optional[UsageEvent]:
        """
        Returns an event by ID.
        """
        return self._repository.get_event(event_id)

    def get_customer_events(
        self,
        customer_id: str,
    ) -> List[UsageEvent]:
        """
        Returns events for a customer.
        """
        return self._repository.get_events_by_customer(customer_id)

    def get_session_events(
        self,
        session_id: str,
    ) -> List[UsageEvent]:
        """
        Returns events for a session.
        """
        return self._repository.get_events_by_session(session_id)

    def get_feature_events(
        self,
        feature_name: str,
    ) -> List[UsageEvent]:
        """
        Returns events for a feature.
        """
        return self._repository.get_events_by_feature(feature_name)

    def get_events_between(
        self,
        start_time: datetime,
        end_time: datetime,
    ) -> List[UsageEvent]:
        """
        Returns events within the specified time range.
        """
        return self._repository.get_events_between(
            start_time,
            end_time,
        )

    def get_successful_events(self) -> List[UsageEvent]:
        """
        Returns successful events.
        """
        return self._repository.get_successful_events()
    def get_failed_events(self) -> List[UsageEvent]:
        """
        Returns failed events.
        """
        return self._repository.get_failed_events()
    def total_events(self) -> int:
        """
        Returns the total number of recorded events.
        """
        return self._repository.total_events()
    def get_all_events(self,) -> List[UsageEvent]:
        """
        Returns all recorded usage events.
        """
        return self._repository.get_all_events()
