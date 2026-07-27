"""
usage_pattern_repository.py

Repository for storing and retrieving customer usage patterns
discovered through machine learning.
"""

from typing import Dict, List, Optional

from src.ic08.models.pattern_cluster import PatternCluster
from src.ic08.models.pattern_summary import PatternSummary
from src.ic08.models.usage_pattern import UsagePattern


class UsagePatternRepository:
    """
    Repository for discovered usage patterns, cluster assignments,
    and pattern summaries.
    """

    def __init__(self):
        """Initialize repository."""
        self._patterns: Dict[str, UsagePattern] = {}
        self._clusters: Dict[int, List[PatternCluster]] = {}
        self._summaries: Dict[int, PatternSummary] = {}

    # ------------------------------------------------------------------
    # Usage Pattern Operations
    # ------------------------------------------------------------------

    def save_pattern(self, pattern: UsagePattern) -> None:
        """Save or update a usage pattern."""
        self._patterns[pattern.pattern_id] = pattern

    def get_pattern(self, pattern_id: str) -> Optional[UsagePattern]:
        """Retrieve a usage pattern by ID."""
        return self._patterns.get(pattern_id)

    def get_all_patterns(self) -> List[UsagePattern]:
        """Return all discovered usage patterns."""
        return list(self._patterns.values())

    def delete_pattern(self, pattern_id: str) -> bool:
        """Delete a usage pattern."""
        if pattern_id in self._patterns:
            del self._patterns[pattern_id]
            return True
        return False

    # ------------------------------------------------------------------
    # Cluster Operations
    # ------------------------------------------------------------------

    def save_cluster_assignment(self, assignment: PatternCluster) -> None:
        """Save a customer cluster assignment."""
        self._clusters.setdefault(
            assignment.cluster_id,
            []
        ).append(assignment)

    def get_cluster(
        self,
        cluster_id: int,
    ) -> List[PatternCluster]:
        """Return all customers in a cluster."""
        return self._clusters.get(cluster_id, [])

    def get_cluster_ids(self) -> List[int]:
        """Return all discovered cluster IDs."""
        return sorted(self._clusters.keys())

    # ------------------------------------------------------------------
    # Pattern Summary Operations
    # ------------------------------------------------------------------

    def save_summary(self, summary: PatternSummary) -> None:
        """Save a cluster summary."""
        self._summaries[summary.cluster_id] = summary

    def get_summary(
        self,
        cluster_id: int,
    ) -> Optional[PatternSummary]:
        """Retrieve summary for a cluster."""
        return self._summaries.get(cluster_id)

    def get_all_summaries(self) -> List[PatternSummary]:
        """Return all pattern summaries."""
        return list(self._summaries.values())

    # ------------------------------------------------------------------
    # Repository Statistics
    # ------------------------------------------------------------------

    def pattern_count(self) -> int:
        """Return number of stored patterns."""
        return len(self._patterns)

    def cluster_count(self) -> int:
        """Return number of discovered clusters."""
        return len(self._clusters)

    def summary_count(self) -> int:
        """Return number of stored summaries."""
        return len(self._summaries)

    def clear(self) -> None:
        """Clear the repository."""
        self._patterns.clear()
        self._clusters.clear()
        self._summaries.clear()
