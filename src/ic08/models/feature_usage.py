"""
feature_usage.py

Feature usage model for the Customer Usage Intelligence Engine.

Represents aggregated usage statistics for an application feature.
These statistics are derived from usage events and are used for
analytics, reporting, and recommendation generation.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class FeatureUsage:
    """
    Represents usage statistics for a feature.
    """

    feature_name: str

    total_usage: int = 0
    unique_users: int = 0
    unique_sessions: int = 0

    total_duration_ms: int = 0

    average_duration_ms: float = 0.0

    successful_events: int = 0
    failed_events: int = 0

    last_used: datetime = field(default_factory=datetime.utcnow)

    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    @property
    def success_rate(self) -> float:
        """
        Returns the success percentage for this feature.
        """
        total = self.successful_events + self.failed_events

        if total == 0:
            return 0.0

        return (self.successful_events / total) * 100

    def record_success(self, duration_ms: int) -> None:
        """
        Records a successful feature usage.
        """
        self.total_usage += 1
        self.successful_events += 1
        self.total_duration_ms += duration_ms

        self.average_duration_ms = (
            self.total_duration_ms / self.total_usage
        )

        self.last_used = datetime.utcnow()
        self.updated_at = self.last_used

    def record_failure(self) -> None:
        """
        Records a failed feature usage.
        """
        self.total_usage += 1
        self.failed_events += 1

        self.updated_at = datetime.utcnow()
