"""
recommendation.py

Recommendation model for the Customer Usage Intelligence Engine.

Represents an actionable recommendation generated from customer
usage analytics, adoption metrics, workflow analysis, and
customer feedback.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Recommendation:
    """
    Represents an actionable recommendation.
    """

    recommendation_id: str

    title: str
    description: str

    category: str

    priority: str

    confidence_score: float = 0.0

    affected_feature: str = ""

    affected_customer_segment: str = ""

    generated_by: str = "Customer Usage Intelligence Engine"

    created_at: datetime = field(default_factory=datetime.utcnow)

    implemented: bool = False

    implementation_notes: str = ""

    updated_at: datetime = field(default_factory=datetime.utcnow)

    def mark_implemented(
        self,
        implementation_notes: str,
    ) -> None:
        """
        Marks the recommendation as implemented.
        """
        self.implemented = True
        self.implementation_notes = implementation_notes
        self.updated_at = datetime.utcnow()

    @property
    def is_high_priority(self) -> bool:
        """
        Returns True if the recommendation is high priority.
        """
        return self.priority.lower() == "high"

    @property
    def confidence_percentage(self) -> float:
        """
        Returns the confidence score as a percentage.
        """
        return self.confidence_score * 100
