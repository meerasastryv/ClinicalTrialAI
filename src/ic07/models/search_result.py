"""
search_result.py

IC-07 - Test Data Intelligence Engine
Milestone 8 - Intelligent Test Data Search

Defines the SearchResult model representing a dataset returned
by the Intelligent Search Service.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from typing import Any, Dict, List, Optional


@dataclass
class SearchResult:
    """
    Represents a dataset returned by the Intelligent Search Engine.
    """

    dataset_name: str

    score: float

    confidence: float

    rank: int

    search_type: str

    reason: str = ""

    matched_fields: List[str] = field(default_factory=list)

    matched_keywords: List[str] = field(default_factory=list)

    recommendation_score: float = 0.0

    quality_score: float = 0.0

    metadata_score: float = 0.0

    similarity_score: float = 0.0

    synthetic_available: bool = False

    tags: List[str] = field(default_factory=list)

    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """
        Validate numeric fields.
        """

        self.score = max(0.0, min(100.0, float(self.score)))

        self.confidence = max(
            0.0,
            min(100.0, float(self.confidence)),
        )

        self.recommendation_score = max(
            0.0,
            min(100.0, float(self.recommendation_score)),
        )

        self.quality_score = max(
            0.0,
            min(100.0, float(self.quality_score)),
        )

        self.metadata_score = max(
            0.0,
            min(100.0, float(self.metadata_score)),
        )

        self.similarity_score = max(
            0.0,
            min(100.0, float(self.similarity_score)),
        )

        self.rank = max(1, int(self.rank))

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert SearchResult into a dictionary.
        """
        return asdict(self)

    @classmethod
    def from_dict(
        cls,
        data: Dict[str, Any],
    ) -> "SearchResult":
        """
        Create SearchResult from a dictionary.
        """
        return cls(**data)

    def summary(self) -> str:
        """
        Return a concise summary.
        """
        return (
            f"Rank #{self.rank}: "
            f"{self.dataset_name} "
            f"(Score={self.score:.2f}, "
            f"Confidence={self.confidence:.2f}%)"
        )

    def __str__(self) -> str:
        return self.summary()

    def __repr__(self) -> str:
        return (
            "SearchResult("
            f"dataset_name='{self.dataset_name}', "
            f"score={self.score:.2f}, "
            f"confidence={self.confidence:.2f}, "
            f"rank={self.rank})"
        )
