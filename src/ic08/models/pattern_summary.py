"""
pattern_summary.py

Summary statistics for a discovered customer usage pattern.
"""

from dataclasses import dataclass


@dataclass
class PatternSummary:
    """
    Statistical summary of a discovered customer behaviour pattern.
    """

    cluster_id: int

    customer_count: int

    average_sessions: float

    average_session_duration: float

    average_features_used: float

    dominant_workflow: str

    confidence_score: float

    def __str__(self) -> str:
        return (
            f"PatternSummary("
            f"cluster={self.cluster_id}, "
            f"customers={self.customer_count}, "
            f"workflow={self.dominant_workflow})"
        )
