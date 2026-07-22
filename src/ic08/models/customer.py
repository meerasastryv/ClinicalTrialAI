"""
customer.py

Customer model for the Customer Usage Intelligence Engine.

This model represents a customer organization that uses the Clinical Trial
platform. It stores customer profile information used for usage analytics,
customer segmentation, adoption analysis, and reporting.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Customer:
    """
    Represents a customer organization.
    """

    customer_id: str
    customer_name: str
    organization: str
    industry: str
    subscription_plan: str
    region: str

    is_active: bool = True

    created_at: datetime = field(default_factory=datetime.utcnow)
    updated_at: datetime = field(default_factory=datetime.utcnow)

    def deactivate(self) -> None:
        """
        Marks the customer as inactive.
        """
        self.is_active = False
        self.updated_at = datetime.utcnow()

    def activate(self) -> None:
        """
        Marks the customer as active.
        """
        self.is_active = True
        self.updated_at = datetime.utcnow()

    def update_timestamp(self) -> None:
        """
        Updates the modification timestamp.
        """
        self.updated_at = datetime.utcnow()
