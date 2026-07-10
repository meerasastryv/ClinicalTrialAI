from typing import List

from src.ic04.models.runtime_event import RuntimeEvent


class RuntimeRepository:
    """
    Stores runtime events captured during execution.
    """

    def __init__(self):
        self._events: List[RuntimeEvent] = []

    def add_event(self, event: RuntimeEvent):
        """
        Store a runtime event.
        """
        self._events.append(event)

    def get_all_events(self) -> List[RuntimeEvent]:
        """
        Return all captured events.
        """
        return list(self._events)

    def get_events_by_type(self, event_type: str) -> List[RuntimeEvent]:
        """
        Return events matching a specific type.
        """
        return [
            event
            for event in self._events
            if event.event_type == event_type
        ]

    def clear(self):
        """
        Remove all stored events.
        """
        self._events.clear()

    def size(self) -> int:
        """
        Number of stored events.
        """
        return len(self._events)
