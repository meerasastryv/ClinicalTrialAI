"""
usage_summary.py

Usage summary model for the Customer Usage Intelligence Engine.

Represents aggregated platform-wide customer usage statistics used
for dashboards, executive reporting, and trend analysis.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class UsageSummary:
    """
    Represents overall customer usage statistics.
    """

    total_customers: int = 0
    active_customers: int = 0

    total_sessions: int = 0
    active_sessions: int = 0

    total_usage_events: int = 0

    average_session_duration_ms: float = 0.0

    overall_adoption_percentage: float = 0.0

    top_features: list[str] = field(default_factory=list)

    generated_at: datetime = field(default_factory=datetime.utcnow)

    def add_top_feature(self, feature_name: str) -> None:
        """
        Adds a feature to the top features list.
        """
        if feature_name not in self.top_features:
            self.top_features.append(feature_name)

    @property
    def customer_activity_rate(self) -> float:
        """
        Returns the percentage of active customers.
        """
        if self.total_customers == 0:
            return 0.0

        return (self.active_customers / self.total_customers) * 100

    @property
    def average_events_per_session(self) -> float:
        """
        Returns the average number of events per session.
        """
        if self.total_sessions == 0:
            return 0.0

        return self.total_usage_events / self.total_sessions
