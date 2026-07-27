"""
usage_pattern.py

Model representing a discovered customer usage pattern.
"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class UsagePattern:
    """
    Represents a customer usage pattern discovered using
    machine learning clustering algorithms such as DBSCAN.
    """

    pattern_id: str
    pattern_name: str

    customer_count: int = 0

    average_sessions: float = 0.0
    average_session_duration: float = 0.0

    average_features_used: float = 0.0
    average_workflows_completed: float = 0.0

    confidence_score: float = 0.0

    created_at: datetime = field(default_factory=datetime.now)

    description: str = ""

    def __str__(self) -> str:
        return (
            f"UsagePattern("
            f"id={self.pattern_id}, "
            f"name={self.pattern_name}, "
            f"customers={self.customer_count}, "
            f"confidence={self.confidence_score:.2f})"
        )
