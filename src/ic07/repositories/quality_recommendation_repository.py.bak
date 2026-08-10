"""
Repository for AI-assisted quality recommendations.
"""

from __future__ import annotations

from typing import List

from src.ic07.models.quality_recommendation import (
    QualityRecommendation,
)


class QualityRecommendationRepository:
    """
    Repository for quality recommendations.
    """

    def __init__(self) -> None:
        self._recommendations: List[
            QualityRecommendation
        ] = []

    # ------------------------------------------------------------------

    def add(
        self,
        recommendation: QualityRecommendation,
    ) -> None:
        """
        Add a recommendation.
        """
        self._recommendations.append(recommendation)

    # ------------------------------------------------------------------

    def list_all(
        self,
    ) -> List[QualityRecommendation]:
        """
        Return all recommendations.
        """
        return self._recommendations

    # ------------------------------------------------------------------

    def clear(self) -> None:
        """
        Remove all recommendations.
        """
        self._recommendations.clear()

    # ------------------------------------------------------------------

    def count(self) -> int:
        """
        Return recommendation count.
        """
        return len(self._recommendations)

    # ------------------------------------------------------------------

    def __len__(self) -> int:
        return self.count()

    def __iter__(self):
        return iter(self._recommendations)
