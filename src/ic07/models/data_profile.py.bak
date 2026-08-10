"""
IC-07 Data Profile Model

Represents profiling statistics and quality metrics for a dataset.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any, Dict


@dataclass
class DataProfile:
    """
    Represents profiling information for a dataset.
    """

    # ------------------------------------------------------------------
    # Identification
    # ------------------------------------------------------------------

    profile_id: str

    dataset_id: str

    # ------------------------------------------------------------------
    # Dataset Statistics
    # ------------------------------------------------------------------

    total_records: int = 0

    total_fields: int = 0

    null_values: int = 0

    duplicate_records: int = 0

    unique_records: int = 0

    # ------------------------------------------------------------------
    # Quality Metrics
    # ------------------------------------------------------------------

    completeness: float = 0.0

    uniqueness: float = 0.0

    consistency: float = 0.0

    validity: float = 0.0

    accuracy: float = 0.0

    overall_score: float = 0.0

    # ------------------------------------------------------------------
    # Additional Metrics
    # ------------------------------------------------------------------

    metrics: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    profiled_by: str = "System"

    profiled_at: datetime = field(default_factory=datetime.utcnow)

    # ------------------------------------------------------------------
    # Utility Methods
    # ------------------------------------------------------------------

    def add_metric(self, name: str, value: Any) -> None:
        """Add or update a custom metric."""
        self.metrics[name] = value

    def get_metric(self, name: str) -> Any:
        """Retrieve a custom metric."""
        return self.metrics.get(name)

    def calculate_overall_score(self) -> float:
        """
        Calculate an overall quality score.
        """

        scores = [
            self.completeness,
            self.uniqueness,
            self.consistency,
            self.validity,
            self.accuracy,
        ]

        self.overall_score = sum(scores) / len(scores)

        return self.overall_score

    def to_dict(self) -> Dict[str, Any]:
        """Convert the model to a dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataProfile":
        """Create a DataProfile from a dictionary."""
        return cls(**data)
