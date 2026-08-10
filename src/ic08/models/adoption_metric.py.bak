"""
adoption_metric.py

Adoption metric model for the Customer Usage Intelligence Engine.

Represents adoption and engagement metrics for an application feature.
These metrics help measure how widely a feature is used across the
customer base and identify opportunities to improve adoption.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class AdoptionMetric:
    """
    Represents feature adoption metrics.
    """

    feature_name: str

    total_customers: int = 0
    adopted_customers: int = 0

    active_users: int = 0
    inactive_users: int = 0

    adoption_percentage: float = 0.0

    first_adopted_at: datetime | None = None
    last_updated: datetime = field(default_factory=datetime.utcnow)

    def calculate_adoption_percentage(self) -> None:
        """
        Calculates the feature adoption percentage.
        """
        if self.total_customers == 0:
            self.adoption_percentage = 0.0
        else:
            self.adoption_percentage = (
                self.adopted_customers / self.total_customers
            ) * 100

        self.last_updated = datetime.utcnow()

    def increment_adopted_customers(self) -> None:
        """
        Increments the number of customers who adopted the feature.
        """
        self.adopted_customers += 1

        if self.first_adopted_at is None:
            self.first_adopted_at = datetime.utcnow()

        self.calculate_adoption_percentage()

    def update_user_counts(
        self,
        active_users: int,
        inactive_users: int,
    ) -> None:
        """
        Updates active and inactive user counts.
        """
        self.active_users = active_users
        self.inactive_users = inactive_users
        self.last_updated = datetime.utcnow()
