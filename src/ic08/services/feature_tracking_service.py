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
    Service for managing feature usage statistics.
    """

    def __init__(
        self,
        feature_repository: FeatureRepository,
    ) -> None:
        self._repository = feature_repository

    def record_feature_usage(
        self,
        feature_name: str,
        duration_ms: int,
        success: bool,
    ) -> None:
        """
        Records usage for a feature.
        """
        feature = self._repository.get_feature(feature_name)

        if feature is None:
            feature = FeatureUsage(
                feature_name=feature_name,
            )
            self._repository.add_feature(feature)

        feature.total_usage += 1
        feature.total_duration_ms += duration_ms
        feature.average_duration_ms = (
            feature.total_duration_ms / feature.total_usage
        )
        feature.last_used = datetime.utcnow()
        feature.updated_at = datetime.utcnow()

        if success:
            feature.record_success()
        else:
            feature.record_failure()

        self._repository.update_feature(feature)

    def get_feature(
        self,
        feature_name: str,
    ) -> Optional[FeatureUsage]:
        """
        Returns statistics for a feature.
        """
        return self._repository.get_feature(feature_name)

    def get_most_used_feature(
        self,
    ) -> Optional[FeatureUsage]:
        """
        Returns the most frequently used feature.
        """
        return self._repository.get_most_used_feature()

    def get_least_used_feature(
        self,
    ) -> Optional[FeatureUsage]:
        """
        Returns the least-used feature.
        """
        return self._repository.get_least_used_feature()

    def get_high_success_features(
        self,
        threshold: float = 95.0,
    ):
        """
        Returns features with a success rate above the threshold.
        """
        return self._repository.get_high_success_features(
            threshold
        )

    def total_features(self) -> int:
        """
        Returns the total number of tracked features.
        """
        return self._repository.total_features()
