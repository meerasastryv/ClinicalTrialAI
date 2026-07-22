"""
usage_repository.py

Repository for managing UsageEvent objects.
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from src.ic08.models.usage_event import UsageEvent


class UsageRepository:
    """
    Repository for storing and querying customer usage events.
    """

    def __init__(self) -> None:
        """
        Initialize the repository.
        """
        self._events: Dict[str, UsageEvent] = {}

    def add_event(
        self,
        event: UsageEvent,
    ) -> None:
        """
        Adds a usage event.
        """
        self._events[event.event_id] = event

    def get_event(
        self,
        event_id: str,
    ) -> Optional[UsageEvent]:
        """
        Returns an event by ID.
        """
        return self._events.get(event_id)

    def update_event(
        self,
        event: UsageEvent,
    ) -> None:
        """
        Updates an existing usage event.
        """
        self._events[event.event_id] = event

    def remove_event(
        self,
        event_id: str,
    ) -> bool:
        """
        Removes a usage event.
        """
        return self._events.pop(event_id, None) is not None

    def get_all_events(self) -> List[UsageEvent]:
        """
        Returns all usage events.
        """
        return list(self._events.values())

    def get_events_by_customer(
        self,
        customer_id: str,
    ) -> List[UsageEvent]:
        """
        Returns all events for a customer.
        """
        return [
            event
            for event in self._events.values()
            if event.customer_id == customer_id
        ]

    def get_events_by_session(
        self,
        session_id: str,
    ) -> List[UsageEvent]:
        """
        Returns all events for a session.
        """
        return [
            event
            for event in self._events.values()
            if event.session_id == session_id
        ]

    def get_events_by_feature(
        self,
        feature_name: str,
    ) -> List[UsageEvent]:
        """
        Returns all events for a feature.
        """
        return [
            event
            for event in self._events.values()
            if event.feature_name.lower() == feature_name.lower()
        ]

    def get_events_by_type(
        self,
        event_type: str,
    ) -> List[UsageEvent]:
        """
        Returns all events of the specified type.
        """
        return [
            event
            for event in self._events.values()
            if event.event_type.lower() == event_type.lower()
        ]

    def get_events_between(
        self,
        start_time: datetime,
        end_time: datetime,
    ) -> List[UsageEvent]:
        """
        Returns events within a time range.
        """
        return [
            event
            for event in self._events.values()
            if start_time <= event.timestamp <= end_time
        ]

    def get_successful_events(self) -> List[UsageEvent]:
        """
        Returns successful events.
        """
        return [
            event
            for event in self._events.values()
            if event.success
        ]

    def get_failed_events(self) -> List[UsageEvent]:
        """
        Returns failed events.
        """
        return [
            event
            for event in self._events.values()
            if not event.success
        ]

    def event_exists(
        self,
        event_id: str,
    ) -> bool:
        """
        Checks whether an event exists.
        """
        return event_id in self._events

    def total_events(self) -> int:
        """
        Returns the total number of events.
        """
        return len(self._events)

    def clear(self) -> None:
        """
        Removes all events.
        """
        self._events.clear()
