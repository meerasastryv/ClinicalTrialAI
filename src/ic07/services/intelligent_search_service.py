"""
intelligent_search_service.py

IC-07 - Test Data Intelligence Engine
Milestone 8 - Intelligent Test Data Search

Provides intelligent dataset search using keyword, metadata,
schema, quality, and semantic-style matching.
"""

from __future__ import annotations

import time
from typing import Dict, List, Optional

from src.ic07.models.search_result import SearchResult
from src.ic07.repositories.search_repository import SearchRepository


class IntelligentSearchService:
    """
    Intelligent search engine for test datasets.
    """

    KEYWORD_WEIGHT = 0.25
    METADATA_WEIGHT = 0.20
    SCHEMA_WEIGHT = 0.20
    SIMILARITY_WEIGHT = 0.15
    QUALITY_WEIGHT = 0.10
    POPULARITY_WEIGHT = 0.10

    def __init__(self) -> None:
        self.repository = SearchRepository()

    # ---------------------------------------------------------
    # Public API
    # ---------------------------------------------------------

    def search(
        self,
        datasets: List[Dict],
        query: str,
        filters: Optional[Dict] = None,
        top_n: int = 10,
    ) -> List[SearchResult]:
        """
        Search datasets using multiple strategies.
        """

        self.repository.clear()

        filters = filters or {}

        start_time = time.time()

        keywords = self._extract_keywords(query)

        for dataset in datasets:

            result = self._evaluate_dataset(
                dataset,
                keywords,
                filters,
            )

            if result.score > 0:
                self.repository.add(result)

        ranked = self.repository.rank()

        elapsed = time.time() - start_time

        print(
            f"Search completed in "
            f"{elapsed:.2f} sec."
        )

        return ranked[:top_n]

    # ---------------------------------------------------------

    def statistics(self) -> Dict:
        """
        Return repository statistics.
        """

        return {
            "matches": self.repository.count(),
            "average_score": self.repository.average_score(),
            "highest_score": self.repository.highest_score(),
            "lowest_score": self.repository.lowest_score(),
        }

    # ---------------------------------------------------------
    # Internal evaluation
    # ---------------------------------------------------------

    def _evaluate_dataset(
        self,
        dataset: Dict,
        keywords: List[str],
        filters: Dict,
    ) -> SearchResult:
        """
        Evaluate one dataset.
        """

        keyword_score, matched_keywords = (
            self._keyword_score(dataset, keywords)
        )

        metadata_score = self._metadata_score(
            dataset,
            filters,
        )

        schema_score = self._schema_score(
            dataset,
            filters,
        )

        similarity_score = self._similarity_score(
            dataset,
        )

        quality_score = self._quality_score(
            dataset,
        )

        popularity_score = self._popularity_score(
            dataset,
        )

        total_score = (
            keyword_score * self.KEYWORD_WEIGHT
            + metadata_score * self.METADATA_WEIGHT
            + schema_score * self.SCHEMA_WEIGHT
            + similarity_score * self.SIMILARITY_WEIGHT
            + quality_score * self.QUALITY_WEIGHT
            + popularity_score * self.POPULARITY_WEIGHT
        )

        confidence = min(
            100.0,
            total_score + 5.0,
        )

        return SearchResult(
            dataset_name=dataset.get(
                "dataset_name",
                "Unknown",
            ),
            score=round(total_score, 2),
            confidence=round(confidence, 2),
            rank=0,
            search_type="Intelligent Search",
            reason=self._reason(total_score),
            matched_fields=dataset.get(
                "matched_fields",
                [],
            ),
            matched_keywords=matched_keywords,
            recommendation_score=dataset.get(
                "recommendation_score",
                0.0,
            ),
            quality_score=quality_score,
            metadata_score=metadata_score,
            similarity_score=similarity_score,
            synthetic_available=dataset.get(
                "synthetic_available",
                False,
            ),
            tags=dataset.get(
                "tags",
                [],
            ),
            metadata=dataset,
        )

    # ---------------------------------------------------------
    # Individual scoring
    # ---------------------------------------------------------

    def _keyword_score(
        self,
        dataset: Dict,
        keywords: List[str],
    ) -> tuple[float, List[str]]:
        """
        Calculate keyword score.
        """

        searchable = " ".join(
            [
                dataset.get("dataset_name", ""),
                " ".join(dataset.get("columns", [])),
                " ".join(dataset.get("tags", [])),
                dataset.get("description", ""),
            ]
        ).lower()

        matched = [
            keyword
            for keyword in keywords
            if keyword in searchable
        ]

        if not keywords:
            return 0.0, matched

        score = (len(matched) / len(keywords)) * 100.0

        return score, matched

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

    def _schema_score(
        self,
        dataset: Dict,
        filters: Dict,
    ) -> float:
        return float(
            dataset.get(
                "schema_score",
                80.0,
            )
        )

    def _similarity_score(
        self,
        dataset: Dict,
    ) -> float:
        return float(
            dataset.get(
                "similarity_score",
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

    def _popularity_score(
        self,
        dataset: Dict,
    ) -> float:
        return float(
            dataset.get(
                "usage_score",
                70.0,
            )
        )

    # ---------------------------------------------------------

    def _extract_keywords(
        self,
        query: str,
    ) -> List[str]:
        """
        Convert a search query into keywords.
        """

        return [
            keyword.lower()
            for keyword in query.split()
            if keyword.strip()
        ]

    def _reason(
        self,
        score: float,
    ) -> str:
        """
        Generate a human-readable explanation.
        """

        if score >= 90:
            return "Excellent search match."

        if score >= 80:
            return "Highly relevant dataset."

        if score >= 70:
            return "Good search match."

        if score >= 60:
            return "Moderately relevant."

        return "Low search relevance."
