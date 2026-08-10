"""
feature_usage.py

Feature usage model for the Customer Usage Intelligence Engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, Any


@dataclass(slots=True)
class FeatureUsage:
    """
    Represents aggregated usage statistics for a feature.
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
        Returns success percentage.
        """

        total = self.successful_events + self.failed_events

        if total == 0:
            return 0.0

        return round(
            (self.successful_events / total) * 100,
            2,
        )

    def refresh_statistics(self) -> None:
        """
        Recalculates derived statistics.
        """

        if self.total_usage > 0:
            self.average_duration_ms = (
                self.total_duration_ms /
                self.total_usage
            )
        else:
            self.average_duration_ms = 0.0

        self.updated_at = datetime.utcnow()

    def touch(self) -> None:
        """
        Updates timestamps.
        """

        now = datetime.utcnow()

        self.last_used = now
        self.updated_at = now

    def to_dict(self) -> Dict[str, Any]:

        return {
            "feature_name": self.feature_name,
            "total_usage": self.total_usage,
            "unique_users": self.unique_users,
            "unique_sessions": self.unique_sessions,
            "total_duration_ms": self.total_duration_ms,
            "average_duration_ms": self.average_duration_ms,
            "successful_events": self.successful_events,
            "failed_events": self.failed_events,
            "success_rate": self.success_rate,
            "last_used": self.last_used.isoformat(),
            "created_at": self.created_at.isoformat(),
            "updated_at": self.updated_at.isoformat(),
        }

    @classmethod
    def from_dict(
        cls,
        data: Dict[str, Any],
    ) -> "FeatureUsage":

        feature = cls(
            feature_name=data["feature_name"],
            total_usage=data.get("total_usage", 0),
            unique_users=data.get("unique_users", 0),
            unique_sessions=data.get("unique_sessions", 0),
            total_duration_ms=data.get(
                "total_duration_ms",
                0,
            ),
            successful_events=data.get(
                "successful_events",
                0,
            ),
            failed_events=data.get(
                "failed_events",
                0,
            ),
        )

        feature.refresh_statistics()

        return feature

    def __str__(self) -> str:

        return (
            f"FeatureUsage("
            f"{self.feature_name}, "
            f"usage={self.total_usage}, "
            f"success={self.success_rate:.2f}%)"
        )
