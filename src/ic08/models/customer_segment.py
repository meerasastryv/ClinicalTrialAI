"""
customer_segment.py

Customer segment model for the Customer Usage Intelligence Engine.

Represents a logical grouping of customers based on shared
characteristics such as subscription plan, industry, usage
patterns, or engagement level.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class CustomerSegment:
    """
    Represents a customer segment.
    """

    segment_id: str
    segment_name: str
    description: str

    criteria: list[str] = field(default_factory=list)

    customer_count: int = 0

    average_sessions_per_customer: float = 0.0

    average_feature_usage: float = 0.0

    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def add_criterion(self, criterion: str) -> None:
        """
        Adds a segmentation criterion.
        """
        if criterion not in self.criteria:
            self.criteria.append(criterion)
            self.updated_at = datetime.utcnow()

    def increment_customer_count(self) -> None:
        """
        Increments the number of customers in the segment.
        """
        self.customer_count += 1
        self.updated_at = datetime.utcnow()

    def update_usage_metrics(
        self,
        average_sessions: float,
        average_feature_usage: float,
    ) -> None:
        """
        Updates aggregate usage metrics for the segment.
        """
        self.average_sessions_per_customer = average_sessions
        self.average_feature_usage = average_feature_usage
        self.updated_at = datetime.utcnow()
