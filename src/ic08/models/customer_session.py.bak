"""
customer_session.py

Customer session model for the Customer Usage Intelligence Engine.

Represents a single user session. A session groups multiple usage events
performed by a customer within a continuous interaction period.
"""

from dataclasses import dataclass, field
from datetime import datetime
from typing import Optional


@dataclass(slots=True)
class CustomerSession:
    """
    Represents a customer usage session.
    """

    session_id: str
    customer_id: str

    user_id: str
    user_name: str

    start_time: datetime

    end_time: Optional[datetime] = None

    device: str = "Unknown"
    browser: str = "Unknown"
    operating_system: str = "Unknown"
    ip_address: str = "Unknown"
    location: str = "Unknown"

    event_count: int = 0

    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    @property
    def duration_seconds(self) -> float:
        """
        Returns the session duration in seconds.
        """
        if self.end_time is None:
            return 0.0

        return (self.end_time - self.start_time).total_seconds()

    def increment_event_count(self) -> None:
        """
        Increments the number of usage events.
        """
        self.event_count += 1
        self.updated_at = datetime.utcnow()

    def close_session(self) -> None:
        """
        Marks the session as completed.
        """
        self.end_time = datetime.utcnow()
        self.updated_at = self.end_time
