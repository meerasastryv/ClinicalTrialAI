"""
feature_tracking_service.py

Service responsible for tracking feature usage metrics.
"""

from __future__ import annotations

from datetime import datetime
from typing import Optional

from src.ic08.models.feature_usage import FeatureUsage
from src.ic08.repositories.feature_repository import FeatureRepository


class FeatureTrackingService:
    """
    Service for tracking and managing feature usage.
    """

    def __init__(
        self,
        feature_repository: FeatureRepository,
    ) -> None:
        self._repository = feature_repository

    # ---------------------------------------------------------
    # Record Feature Usage
    # ---------------------------------------------------------

    def record_feature_usage(
        self,
        feature_name: str,
        duration_ms: int,
        success: bool = True,
    ) -> None:
        """
        Records a feature usage event.
        """

        feature = self._repository.get_feature(feature_name)

        if feature is None:
            feature = FeatureUsage(
                feature_name=feature_name,
            )

        #
        # Update usage statistics
        #
        feature.total_usage += 1

        feature.total_duration_ms += duration_ms

        if success:
            feature.successful_events += 1
        else:
            feature.failed_events += 1

        feature.touch()

        feature.refresh_statistics()

        self._repository.add_feature(feature)

    # ---------------------------------------------------------
    # Retrieval
    # ---------------------------------------------------------

    def get_feature(
        self,
        feature_name: str,
    ) -> Optional[FeatureUsage]:

        return self._repository.get_feature(feature_name)

    def get_all_features(self):

        return self._repository.get_all_features()

    def get_most_used_feature(self):

        return self._repository.get_most_used_feature()

    def get_least_used_feature(self):

        return self._repository.get_least_used_feature()

    def get_high_success_features(
        self,
        threshold: float = 95.0,
    ):

        return self._repository.get_high_success_features(
            threshold
        )

    def total_features(self):

        return self._repository.total_features()

    # ---------------------------------------------------------
    # Summary
    # ---------------------------------------------------------

    def generate_summary(self):

        most_used = self.get_most_used_feature()

        least_used = self.get_least_used_feature()

        return {
            "total_features": self.total_features(),
            "most_used": (
                most_used.feature_name
                if most_used
                else None
            ),
            "least_used": (
                least_used.feature_name
                if least_used
                else None
            ),
        }

    def clear(self):

        self._repository.clear()
