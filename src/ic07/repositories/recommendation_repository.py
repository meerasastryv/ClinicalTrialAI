"""
recommendation_repository.py

IC-07 - Test Data Intelligence Engine
Milestone 7 - Test Data Recommendation Engine

Repository for storing and managing dataset recommendations.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional

from src.ic07.models.recommendation import Recommendation


class RecommendationRepository:
    """
    Repository for Recommendation objects.
    """

    def __init__(self) -> None:
        self._recommendations: Dict[str, Recommendation] = {}

    # ------------------------------------------------------------------
    # CRUD Operations
    # ------------------------------------------------------------------

    def add(self, recommendation: Recommendation) -> None:
        """
        Add or replace a recommendation.
        """
        self._recommendations[
            recommendation.dataset_name
        ] = recommendation

    def get(self, dataset_name: str) -> Optional[Recommendation]:
        """
        Retrieve recommendation by dataset name.
        """
        return self._recommendations.get(dataset_name)

    def remove(self, dataset_name: str) -> bool:
        """
        Remove recommendation by dataset name.
        """
        return (
            self._recommendations.pop(dataset_name, None)
            is not None
        )

    def clear(self) -> None:
        """
        Remove all recommendations.
        """
        self._recommendations.clear()

    # ------------------------------------------------------------------
    # Query Operations
    # ------------------------------------------------------------------

    def exists(self, dataset_name: str) -> bool:
        """
        Check whether a recommendation exists.
        """
        return dataset_name in self._recommendations

    def count(self) -> int:
        """
        Number of stored recommendations.
        """
        return len(self._recommendations)

    def list_all(self) -> List[Recommendation]:
        """
        Return all recommendations.
        """
        return list(self._recommendations.values())

    def top(self, limit: int = 10) -> List[Recommendation]:
        """
        Return highest scored recommendations.
        """
        return sorted(
            self._recommendations.values(),
            key=lambda r: r.score,
            reverse=True,
        )[:limit]

    def search(
        self,
        keyword: str,
    ) -> List[Recommendation]:
        """
        Search recommendations by dataset name.
        """
        keyword = keyword.lower()

        return [
            recommendation
            for recommendation in self._recommendations.values()
            if keyword in recommendation.dataset_name.lower()
        ]

    # ------------------------------------------------------------------
    # Ranking
    # ------------------------------------------------------------------

    def rank(self) -> List[Recommendation]:
        """
        Assign ranking based on score.
        """
        ranked = sorted(
            self._recommendations.values(),
            key=lambda r: r.score,
            reverse=True,
        )

        for index, recommendation in enumerate(
            ranked,
            start=1,
        ):
            recommendation.rank = index

        return ranked

    # ------------------------------------------------------------------
    # Persistence
    # ------------------------------------------------------------------

    def save(
        self,
        file_path: str,
    ) -> None:
        """
        Save recommendations as JSON.
        """
        data = [
            recommendation.to_dict()
            for recommendation in self.rank()
        ]

        Path(file_path).write_text(
            json.dumps(data, indent=4),
            encoding="utf-8",
        )

    def load(
        self,
        file_path: str,
    ) -> None:
        """
        Load recommendations from JSON.
        """
        path = Path(file_path)

        if not path.exists():
            return

        records = json.loads(
            path.read_text(encoding="utf-8")
        )

        self.clear()

        for record in records:
            recommendation = Recommendation.from_dict(record)
            self.add(recommendation)

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def average_score(self) -> float:
        """
        Calculate average recommendation score.
        """
        if not self._recommendations:
            return 0.0

        return (
            sum(
                recommendation.score
                for recommendation
                in self._recommendations.values()
            )
            / len(self._recommendations)
        )

    def highest_score(self) -> float:
        """
        Return highest recommendation score.
        """
        if not self._recommendations:
            return 0.0

        return max(
            recommendation.score
            for recommendation
            in self._recommendations.values()
        )

    def lowest_score(self) -> float:
        """
        Return lowest recommendation score.
        """
        if not self._recommendations:
            return 0.0

        return min(
            recommendation.score
            for recommendation
            in self._recommendations.values()
        )

    # ------------------------------------------------------------------

    def __len__(self) -> int:
        return self.count()

    def __iter__(self):
        return iter(self.rank())

    def __contains__(self, dataset_name: str) -> bool:
        return self.exists(dataset_name)
