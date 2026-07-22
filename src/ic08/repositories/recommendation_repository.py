"""
recommendation_repository.py

Repository for managing Recommendation objects.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from src.ic08.models.recommendation import Recommendation


class RecommendationRepository:
    """
    Repository for storing and analyzing AI-generated recommendations.
    """

    def __init__(self) -> None:
        """
        Initialize the repository.
        """
        self._recommendations: Dict[str, Recommendation] = {}

    def add_recommendation(
        self,
        recommendation: Recommendation,
    ) -> None:
        """
        Adds or replaces a recommendation.
        """
        self._recommendations[
            recommendation.recommendation_id
        ] = recommendation

    def get_recommendation(
        self,
        recommendation_id: str,
    ) -> Optional[Recommendation]:
        """
        Returns a recommendation by ID.
        """
        return self._recommendations.get(recommendation_id)

    def update_recommendation(
        self,
        recommendation: Recommendation,
    ) -> None:
        """
        Updates an existing recommendation.
        """
        self._recommendations[
            recommendation.recommendation_id
        ] = recommendation

    def remove_recommendation(
        self,
        recommendation_id: str,
    ) -> bool:
        """
        Removes a recommendation.
        """
        return (
            self._recommendations.pop(recommendation_id, None)
            is not None
        )

    def get_all_recommendations(self) -> List[Recommendation]:
        """
        Returns all recommendations.
        """
        return list(self._recommendations.values())

    def get_high_priority_recommendations(
        self,
    ) -> List[Recommendation]:
        """
        Returns all high-priority recommendations.
        """
        return [
            recommendation
            for recommendation in self._recommendations.values()
            if recommendation.is_high_priority
        ]

    def get_pending_recommendations(
        self,
    ) -> List[Recommendation]:
        """
        Returns recommendations that have not yet been implemented.
        """
        return [
            recommendation
            for recommendation in self._recommendations.values()
            if not recommendation.implemented
        ]

    def get_implemented_recommendations(
        self,
    ) -> List[Recommendation]:
        """
        Returns implemented recommendations.
        """
        return [
            recommendation
            for recommendation in self._recommendations.values()
            if recommendation.implemented
        ]

    def get_recommendations_by_feature(
        self,
        feature_name: str,
    ) -> List[Recommendation]:
        """
        Returns recommendations affecting a feature.
        """
        return [
            recommendation
            for recommendation in self._recommendations.values()
            if recommendation.affected_feature.lower()
            == feature_name.lower()
        ]

    def get_recommendations_by_category(
        self,
        category: str,
    ) -> List[Recommendation]:
        """
        Returns recommendations for a category.
        """
        return [
            recommendation
            for recommendation in self._recommendations.values()
            if recommendation.category.lower()
            == category.lower()
        ]

    def average_confidence_score(self) -> float:
        """
        Returns the average confidence score.
        """
        if not self._recommendations:
            return 0.0

        return (
            sum(
                recommendation.confidence_score
                for recommendation in self._recommendations.values()
            )
            / len(self._recommendations)
        )

    def recommendation_exists(
        self,
        recommendation_id: str,
    ) -> bool:
        """
        Checks whether a recommendation exists.
        """
        return recommendation_id in self._recommendations

    def total_recommendations(self) -> int:
        """
        Returns the total number of recommendations.
        """
        return len(self._recommendations)

    def clear(self) -> None:
        """
        Removes all recommendations.
        """
        self._recommendations.clear()
