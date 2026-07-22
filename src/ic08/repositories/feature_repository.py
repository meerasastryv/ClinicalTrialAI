"""
feature_repository.py

Repository for managing FeatureUsage objects.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from src.ic08.models.feature_usage import FeatureUsage


class FeatureRepository:
    """
    Repository for storing and analyzing feature usage statistics.
    """

    def __init__(self) -> None:
        """
        Initialize the repository.
        """
        self._features: Dict[str, FeatureUsage] = {}

    def add_feature(
        self,
        feature: FeatureUsage,
    ) -> None:
        """
        Adds or replaces a feature usage record.
        """
        self._features[feature.feature_name] = feature

    def get_feature(
        self,
        feature_name: str,
    ) -> Optional[FeatureUsage]:
        """
        Returns a feature by name.
        """
        return self._features.get(feature_name)

    def update_feature(
        self,
        feature: FeatureUsage,
    ) -> None:
        """
        Updates a feature.
        """
        self._features[feature.feature_name] = feature

    def remove_feature(
        self,
        feature_name: str,
    ) -> bool:
        """
        Removes a feature.
        """
        return self._features.pop(feature_name, None) is not None

    def get_all_features(self) -> List[FeatureUsage]:
        """
        Returns all features.
        """
        return list(self._features.values())

    def get_most_used_feature(self) -> Optional[FeatureUsage]:
        """
        Returns the feature with the highest usage.
        """
        if not self._features:
            return None

        return max(
            self._features.values(),
            key=lambda feature: feature.total_usage,
        )

    def get_least_used_feature(self) -> Optional[FeatureUsage]:
        """
        Returns the least-used feature.
        """
        if not self._features:
            return None

        return min(
            self._features.values(),
            key=lambda feature: feature.total_usage,
        )

    def get_features_with_failures(self) -> List[FeatureUsage]:
        """
        Returns features that have recorded failures.
        """
        return [
            feature
            for feature in self._features.values()
            if feature.failed_events > 0
        ]

    def get_high_success_features(
        self,
        threshold: float = 95.0,
    ) -> List[FeatureUsage]:
        """
        Returns features with a success rate above the threshold.
        """
        return [
            feature
            for feature in self._features.values()
            if feature.success_rate >= threshold
        ]

    def total_features(self) -> int:
        """
        Returns the total number of tracked features.
        """
        return len(self._features)

    def clear(self) -> None:
        """
        Removes all feature usage records.
        """
        self._features.clear()
