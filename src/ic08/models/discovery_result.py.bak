"""
discovery_result.py

Model representing the result of a machine learning
usage pattern discovery execution.
"""

from dataclasses import dataclass, field
from typing import List

from src.ic08.models.pattern_cluster import PatternCluster


@dataclass
class UsagePatternDiscoveryResult:
    """
    Represents the result of a usage pattern
    discovery operation.
    """

    # ------------------------------------------------------------------
    # Discovery Configuration
    # ------------------------------------------------------------------

    algorithm: str = "DBSCAN"

    eps: float = 0.5

    min_samples: int = 3

    # ------------------------------------------------------------------
    # Discovery Statistics
    # ------------------------------------------------------------------

    customer_count: int = 0

    feature_count: int = 0

    cluster_count: int = 0

    noise_count: int = 0

    execution_time: float = 0.0

    # ------------------------------------------------------------------
    # Discovery Output
    # ------------------------------------------------------------------

    clusters: List[PatternCluster] = field(
        default_factory=list
    )

    # ------------------------------------------------------------------
    # Helper Methods
    # ------------------------------------------------------------------

    def has_clusters(self) -> bool:
        """
        Return True if clusters were discovered.
        """
        return len(self.clusters) > 0

    def has_noise(self) -> bool:
        """
        Return True if noise points exist.
        """
        return self.noise_count > 0

    def summary(self) -> str:
        """
        Return a short textual summary.
        """
        return (
            f"{self.algorithm}: "
            f"{self.cluster_count} clusters, "
            f"{self.noise_count} noise points"
        )

    def __str__(self) -> str:
        return (
            f"UsagePatternDiscoveryResult("
            f"algorithm={self.algorithm}, "
            f"clusters={self.cluster_count}, "
            f"noise={self.noise_count}, "
            f"customers={self.customer_count})"
        )
