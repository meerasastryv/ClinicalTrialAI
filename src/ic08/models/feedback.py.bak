"""
feedback.py

Customer feedback model for the Customer Usage Intelligence Engine.

Represents feedback submitted by customers for application features.
This information is used alongside usage analytics to identify
improvement opportunities and customer satisfaction trends.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(slots=True)
class Feedback:
    """
    Represents customer feedback.
    """

    feedback_id: str
    customer_id: str
    session_id: str

    feature_name: str

    rating: int

    comments: str = ""

    category: str = "General"

    submitted_at: datetime = field(default_factory=datetime.utcnow)

    resolved: bool = False

    resolution_notes: str = ""

    updated_at: datetime = field(default_factory=datetime.utcnow)

    def mark_resolved(
        self,
        resolution_notes: str,
    ) -> None:
        """
        Marks the feedback as resolved.
        """
        self.resolved = True
        self.resolution_notes = resolution_notes
        self.updated_at = datetime.utcnow()

    @property
    def is_positive(self) -> bool:
        """
        Returns True if the feedback is considered positive.
        """
        return self.rating >= 4

    @property
    def is_negative(self) -> bool:
        """
        Returns True if the feedback is considered negative.
        """
        return self.rating <= 2
