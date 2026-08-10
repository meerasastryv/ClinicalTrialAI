"""
usage_event.py

Usage event model for the Customer Usage Intelligence Engine.

Represents a single customer interaction with the application.
Usage events form the foundation for customer analytics,
feature usage analysis, workflow discovery, and journey analysis.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Any


@dataclass(slots=True)
class UsageEvent:
    """
    Represents a single customer usage event.
    """

    event_id: str
    session_id: str
    customer_id: str

    feature_name: str
    event_type: str

    timestamp: datetime = field(default_factory=datetime.utcnow)

    page_name: str = ""
    action_name: str = ""

    duration_ms: int = 0

    success: bool = True

    metadata: dict[str, Any] = field(default_factory=dict)

    created_at: datetime = field(default_factory=datetime.utcnow)

    def mark_failed(self) -> None:
        """
        Marks the event as failed.
        """
        self.success = False

    def add_metadata(self, key: str, value: Any) -> None:
        """
        Adds metadata to the event.
        """
        self.metadata[key] = value
