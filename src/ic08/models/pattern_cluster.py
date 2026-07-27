"""
pattern_cluster.py

Model representing a customer's cluster assignment.
"""

from dataclasses import dataclass


@dataclass
class PatternCluster:
    """
    Represents the cluster assignment of a customer.
    """

    customer_id: str

    cluster_id: int

    is_noise: bool = False

    similarity_score: float = 0.0

    def __str__(self) -> str:
        return (
            f"PatternCluster("
            f"customer={self.customer_id}, "
            f"cluster={self.cluster_id}, "
            f"noise={self.is_noise})"
        )
