"""
recommendation_engine.py

IC-07 - Test Data Intelligence Engine
Milestone 7 - Test Data Recommendation Engine

Provides intelligent recommendation and ranking of datasets
based on metadata, quality, similarity, coverage, usage,
and synthetic availability.
"""

from __future__ import annotations

import time
from typing import Dict, List, Optional

from src.ic07.models.recommendation import Recommendation
from src.ic07.repositories.recommendation_repository import (
    RecommendationRepository,
)


class RecommendationEngine:
    """
    Intelligent recommendation engine for test datasets.
    """

    METADATA_WEIGHT = 0.25
    QUALITY_WEIGHT = 0.20
    COVERAGE_WEIGHT = 0.20
    SIMILARITY_WEIGHT = 0.15
    USAGE_WEIGHT = 0.10
    SYNTHETIC_WEIGHT = 0.10

    def __init__(self) -> None:
        self.repository = RecommendationRepository()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def recommend(
        self,
        datasets: List[Dict],
        filters: Optional[Dict] = None,
        top_n: int = 10,
    ) -> List[Recommendation]:
        """
        Generate recommendations.
        """

        self.repository.clear()

        filters = filters or {}

        start_time = time.time()

        for dataset in datasets:

            recommendation = self._evaluate_dataset(
                dataset,
                filters,
            )

            if recommendation:
                self.repository.add(recommendation)

        ranked = self.repository.rank()

        elapsed = time.time() - start_time

        print(
            f"Recommendation completed in "
            f"{elapsed:.2f} sec."
        )

        return ranked[:top_n]

    # ---------------------------------------------------------

    def statistics(self) -> Dict:
        """
        Return repository statistics.
        """

        return {
            "recommendations": self.repository.count(),
            "average_score": self.repository.average_score(),
            "highest_score": self.repository.highest_score(),
            "lowest_score": self.repository.lowest_score(),
        }

    # ---------------------------------------------------------
    # Internal Evaluation
    # ---------------------------------------------------------

    def _evaluate_dataset(
        self,
        dataset: Dict,
        filters: Dict,
    ) -> Optional[Recommendation]:
        """
        Evaluate one dataset.
        """

        metadata = self._metadata_score(
            dataset,
            filters,
        )

        quality = self._quality_score(dataset)

        coverage = self._coverage_score(dataset)

        similarity = self._similarity_score(
            dataset,
            filters,
        )

        usage = self._usage_score(dataset)

        synthetic = self._synthetic_score(dataset)

        total_score = (
            metadata * self.METADATA_WEIGHT
            + quality * self.QUALITY_WEIGHT
            + coverage * self.COVERAGE_WEIGHT
            + similarity * self.SIMILARITY_WEIGHT
            + usage * self.USAGE_WEIGHT
            + synthetic * self.SYNTHETIC_WEIGHT
        )

        confidence = min(
            100.0,
            total_score + 5.0,
        )

        return Recommendation(
            dataset_name=dataset.get(
                "dataset_name",
                "Unknown",
            ),
            score=round(total_score, 2),
            confidence=round(confidence, 2),
            rank=0,
            reason=self._reason(total_score),
            matched_columns=dataset.get(
                "matched_columns",
                [],
            ),
            tags=dataset.get(
                "tags",
                [],
            ),
            quality_score=quality,
            profile_score=coverage,
            metadata_score=metadata,
            similarity_score=similarity,
            coverage_score=coverage,
            usage_score=usage,
            synthetic_score=synthetic,
            synthetic_available=dataset.get(
                "synthetic_available",
                False,
            ),
            recommended_rows=dataset.get(
                "rows",
                None,
            ),
            metadata=dataset,
        )

    # ---------------------------------------------------------
    # Individual Score Components
    # ---------------------------------------------------------

    def _metadata_score(
        self,
        dataset: Dict,
        filters: Dict,
    ) -> float:
        return float(
            dataset.get(
                "metadata_score",
                80.0,
            )
        )

    def _quality_score(
        self,
        dataset: Dict,
    ) -> float:
        return float(
            dataset.get(
                "quality_score",
                80.0,
            )
        )

    def _coverage_score(
        self,
        dataset: Dict,
    ) -> float:
        return float(
            dataset.get(
                "coverage_score",
                80.0,
            )
        )

    def _similarity_score(
        self,
        dataset: Dict,
        filters: Dict,
    ) -> float:
        return float(
            dataset.get(
                "similarity_score",
                80.0,
            )
        )

    def _usage_score(
        self,
        dataset: Dict,
    ) -> float:
        return float(
            dataset.get(
                "usage_score",
                70.0,
            )
        )

    def _synthetic_score(
        self,
        dataset: Dict,
    ) -> float:
        return (
            100.0
            if dataset.get(
                "synthetic_available",
                False,
            )
            else 60.0
        )

    # ---------------------------------------------------------

    def _reason(
        self,
        score: float,
    ) -> str:
        """
        Generate recommendation explanation.
        """

        if score >= 90:
            return "Excellent metadata and quality match."

        if score >= 80:
            return "Highly recommended."

        if score >= 70:
            return "Good candidate."

        if score >= 60:
            return "Moderate match."

        return "Low recommendation score."
