"""
feature_adoption_service.py

Feature Adoption Analytics Service.

Calculates customer adoption metrics for product features based on
usage events.
"""

from __future__ import annotations

import logging
from collections import Counter, defaultdict
from datetime import datetime
from typing import Dict, List, Optional

from src.ic08.models.feature_adoption import FeatureAdoption
from src.ic08.models.usage_event import UsageEvent
from src.ic08.repositories.feature_adoption_repository import (
    FeatureAdoptionRepository,
)

logger = logging.getLogger(__name__)


class FeatureAdoptionService:
    """
    Service responsible for computing feature adoption analytics.
    """

    def __init__(
        self,
        repository: Optional[FeatureAdoptionRepository] = None,
    ):
        self.repository = repository or FeatureAdoptionRepository()

    # ---------------------------------------------------------
    # Main Analysis
    # ---------------------------------------------------------

    def analyze_feature(
        self,
        feature_name: str,
        usage_events: List[UsageEvent],
    ) -> FeatureAdoption:
        """
        Analyze a single feature using usage events.
        """

        feature_events = [
            event
            for event in usage_events
            if event.feature_name == feature_name
        ]

        adoption = FeatureAdoption(
            feature_name=feature_name,
        )

        if not feature_events:
            self.repository.save(adoption)
            return adoption

        self._calculate_basic_metrics(
            adoption,
            feature_events,
            usage_events,
        )

        self._calculate_usage_metrics(
            adoption,
            feature_events,
        )

        self._calculate_user_segments(
            adoption,
            feature_events,
        )

        adoption.trend = self._calculate_trend(adoption)
        adoption.score = self._calculate_score(adoption)

        self.repository.save(adoption)

        logger.info(
            "Feature '%s' analyzed successfully.",
            feature_name,
        )

        return adoption

    # ---------------------------------------------------------
    # Basic Metrics
    # ---------------------------------------------------------

    def _calculate_basic_metrics(
        self,
        adoption: FeatureAdoption,
        feature_events: List[UsageEvent],
        all_events: List[UsageEvent],
    ) -> None:
        """
        Calculate adoption statistics.
        """

        all_users = {
            event.customer_id
            for event in all_events
        }

        adopted_users = {
            event.customer_id
            for event in feature_events
        }

        adoption.total_users = len(all_users)
        adoption.adopted_users = len(adopted_users)

        if adoption.total_users > 0:
            adoption.adoption_rate = (
                adoption.adopted_users
                / adoption.total_users
            ) * 100.0

        timestamps = sorted(
            event.timestamp
            for event in feature_events
        )

        if timestamps:
            adoption.first_use = timestamps[0]
            adoption.last_use = timestamps[-1]

            adoption.time_to_adoption = (
                timestamps[-1] - timestamps[0]
            ).total_seconds() / 3600.0

    # ---------------------------------------------------------
    # Usage Metrics
    # ---------------------------------------------------------

    def _calculate_usage_metrics(
        self,
        adoption: FeatureAdoption,
        feature_events: List[UsageEvent],
    ) -> None:
        """
        Calculate usage statistics.
        """

        adoption.total_usage_count = len(feature_events)

        if adoption.adopted_users > 0:
            adoption.average_usage = (
                adoption.total_usage_count
                / adoption.adopted_users
            )

        usage_counter = Counter(
            event.customer_id
            for event in feature_events
        )

        repeat_users = sum(
            1
            for count in usage_counter.values()
            if count > 1
        )

        if adoption.adopted_users > 0:
            adoption.repeat_usage_rate = (
                repeat_users
                / adoption.adopted_users
            ) * 100.0

    # ---------------------------------------------------------
    # User Segmentation
    # ---------------------------------------------------------

    def _calculate_user_segments(
        self,
        adoption: FeatureAdoption,
        feature_events: List[UsageEvent],
    ) -> None:
        """
        Categorize customers based on usage.
        """

        usage_counter = defaultdict(int)

        for event in feature_events:
            usage_counter[event.customer_id] += 1

        for count in usage_counter.values():

            if count >= 10:
                adoption.power_users += 1

            elif count >= 2:
                adoption.casual_users += 1

            else:
                adoption.inactive_users += 1


         # ---------------------------------------------------------
    # Trend Analysis
    # ---------------------------------------------------------

    def _calculate_trend(
        self,
        adoption: FeatureAdoption,
    ) -> str:
        """
        Determine feature adoption trend.
        """

        if adoption.adoption_rate >= 80:
            return "Excellent"

        if adoption.adoption_rate >= 60:
            return "Growing"

        if adoption.adoption_rate >= 40:
            return "Stable"

        if adoption.adoption_rate >= 20:
            return "Declining"

        return "Poor"

    # ---------------------------------------------------------
    # Adoption Score
    # ---------------------------------------------------------

    def _calculate_score(
        self,
        adoption: FeatureAdoption,
    ) -> float:
        """
        Calculate an overall adoption score.
        """

        score = (
            (adoption.adoption_rate * 0.50)
            + (adoption.repeat_usage_rate * 0.30)
            + (min(adoption.average_usage, 10.0) * 2.0)
        )

        return round(score, 2)

    # ---------------------------------------------------------
    # CRUD Operations
    # ---------------------------------------------------------

    def save(
        self,
        adoption: FeatureAdoption,
    ) -> None:
        self.repository.save(adoption)

    def update(
        self,
        adoption: FeatureAdoption,
    ) -> None:
        self.repository.update(adoption)

    def get(
        self,
        feature_name: str,
    ) -> Optional[FeatureAdoption]:
        return self.repository.get(feature_name)

    def exists(
        self,
        feature_name: str,
    ) -> bool:
        return self.repository.exists(feature_name)

    def delete(
        self,
        feature_name: str,
    ) -> bool:
        return self.repository.delete(feature_name)

    def clear(self) -> None:
        self.repository.clear()

    # ---------------------------------------------------------
    # Repository Queries
    # ---------------------------------------------------------

    def get_all(
        self,
    ) -> List[FeatureAdoption]:
        return self.repository.get_all()

    def count(
        self,
    ) -> int:
        return self.repository.count()

    def get_top_features(
        self,
        limit: int = 10,
    ) -> List[FeatureAdoption]:
        return self.repository.get_top_features(limit)

    def get_low_adoption_features(
        self,
        threshold: float = 20.0,
    ) -> List[FeatureAdoption]:
        return self.repository.get_low_adoption_features(
            threshold
        )

    def sort_by_adoption_rate(
        self,
        descending: bool = True,
    ) -> List[FeatureAdoption]:
        return self.repository.sort_by_adoption_rate(
            descending
        )

    def sort_by_score(
        self,
        descending: bool = True,
    ) -> List[FeatureAdoption]:
        return self.repository.sort_by_score(
            descending
        )

    def sort_by_average_usage(
        self,
        descending: bool = True,
    ) -> List[FeatureAdoption]:
        return self.repository.sort_by_average_usage(
            descending
        )

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def find_by_trend(
        self,
        trend: str,
    ) -> List[FeatureAdoption]:
        return self.repository.find_by_trend(trend)

    def find_power_features(
        self,
        minimum_power_users: int = 10,
    ) -> List[FeatureAdoption]:
        return self.repository.find_power_features(
            minimum_power_users
        )

    def find_inactive_features(
        self,
    ) -> List[FeatureAdoption]:
        return self.repository.find_inactive_features()

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def summary(self) -> Dict:
        """
        Returns repository summary.
        """

        return self.repository.summary()

    def generate_summary(self) -> Dict:
        """
        Generate detailed analytics summary.
        """

        features = self.repository.get_all()

        if not features:
            return {
                "total_features": 0,
                "average_adoption_rate": 0.0,
                "average_score": 0.0,
            }

        average_rate = (
            sum(
                feature.adoption_rate
                for feature in features
            )
            / len(features)
        )

        average_score = (
            sum(
                feature.score
                for feature in features
            )
            / len(features)
        )

        return {
            "total_features": len(features),
            "average_adoption_rate": round(
                average_rate,
                2,
            ),
            "average_score": round(
                average_score,
                2,
            ),
            "highest_adoption": (
                self.repository.get_highest_adoption()
            ),
            "lowest_adoption": (
                self.repository.get_lowest_adoption()
            ),
        }

    # ---------------------------------------------------------
    # Batch Analysis
    # ---------------------------------------------------------

    def analyze_all_features(
        self,
        usage_events: List[UsageEvent],
    ) -> List[FeatureAdoption]:
        """
        Analyze every feature found in usage events.
        """

        feature_names = sorted(
            {
                event.feature_name
                for event in usage_events
            }
        )

        results = []

        for feature_name in feature_names:
            results.append(
                self.analyze_feature(
                    feature_name,
                    usage_events,
                )
            )

        return results

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def get_feature_names(
        self,
    ) -> List[str]:
        return self.repository.get_feature_names()

    def __len__(self) -> int:
        return self.repository.count()

    def __iter__(self):
        return iter(self.repository.get_all())

    def __str__(self) -> str:
        return (
            f"FeatureAdoptionService("
            f"features={self.repository.count()})"
        )
