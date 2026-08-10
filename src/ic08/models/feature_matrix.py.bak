"""
feature_matrix.py

Model representing the machine learning feature matrix
used by Customer Usage Intelligence.
"""

from dataclasses import dataclass, field
from typing import List

from src.ic08.models.feature_definition import FeatureDefinition


@dataclass
class FeatureMatrix:
    """
    Represents the feature matrix generated from
    customer usage analytics.
    """

    customer_ids: List[str] = field(default_factory=list)

    feature_definitions: List[FeatureDefinition] = field(
        default_factory=list
    )

    feature_values: List[List[float]] = field(default_factory=list)

    def row_count(self) -> int:
        """Return number of customers."""
        return len(self.feature_values)

    def column_count(self) -> int:
        """Return number of features."""
        return len(self.feature_definitions)

    def is_empty(self) -> bool:
        """Return True if no feature data exists."""
        return len(self.feature_values) == 0

    def feature_names(self) -> List[str]:
        """Return feature names."""
        return [
            feature.name
            for feature in self.feature_definitions
        ]

    def __str__(self) -> str:
        return (
            f"FeatureMatrix("
            f"rows={self.row_count()}, "
            f"columns={self.column_count()})"
        )
