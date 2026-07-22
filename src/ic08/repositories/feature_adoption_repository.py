from __future__ import annotations

from typing import Dict, List, Optional

from src.ic08.models.feature_adoption import FeatureAdoption


class FeatureAdoptionRepository:
    """
    Repository for storing Feature Adoption Analytics.
    """

    def __init__(self):
        self._adoptions: Dict[str, FeatureAdoption] = {}

    # ---------------------------------------------------------
    # CRUD Operations
    # ---------------------------------------------------------

    def save(self, adoption: FeatureAdoption) -> None:
        """Save a feature adoption record."""
        adoption.update_timestamp()
        self._adoptions[adoption.feature_name] = adoption

    def update(self, adoption: FeatureAdoption) -> None:
        """Update an existing feature adoption record."""
        adoption.update_timestamp()
        self._adoptions[adoption.feature_name] = adoption

    def get(self, feature_name: str) -> Optional[FeatureAdoption]:
        """Retrieve a feature by name."""
        return self._adoptions.get(feature_name)

    def exists(self, feature_name: str) -> bool:
        """Check whether a feature exists."""
        return feature_name in self._adoptions

    def get_all(self) -> List[FeatureAdoption]:
        """Return all feature adoption records."""
        return list(self._adoptions.values())

    def delete(self, feature_name: str) -> bool:
        """Delete a feature."""
        if feature_name in self._adoptions:
            del self._adoptions[feature_name]
            return True
        return False

    def clear(self) -> None:
        """Remove all analytics."""
        self._adoptions.clear()

    def count(self) -> int:
        """Number of stored features."""
        return len(self._adoptions)

    # ---------------------------------------------------------
    # Sorting
    # ---------------------------------------------------------

    def sort_by_adoption_rate(
        self,
        descending: bool = True
    ) -> List[FeatureAdoption]:

        return sorted(
            self.get_all(),
            key=lambda x: x.adoption_rate,
            reverse=descending,
        )

    def sort_by_score(
        self,
        descending: bool = True
    ) -> List[FeatureAdoption]:

        return sorted(
            self.get_all(),
            key=lambda x: x.score,
            reverse=descending,
        )

    def sort_by_average_usage(
        self,
        descending: bool = True
    ) -> List[FeatureAdoption]:

        return sorted(
            self.get_all(),
            key=lambda x: x.average_usage,
            reverse=descending,
        )

    # ---------------------------------------------------------
    # Ranking
    # ---------------------------------------------------------

    def get_highest_adoption(self) -> Optional[FeatureAdoption]:

        if not self._adoptions:
            return None

        return max(
            self.get_all(),
            key=lambda x: x.adoption_rate,
        )

    def get_lowest_adoption(self) -> Optional[FeatureAdoption]:

        if not self._adoptions:
            return None

        return min(
            self.get_all(),
            key=lambda x: x.adoption_rate,
        )

    def get_top_features(
        self,
        limit: int = 10
    ) -> List[FeatureAdoption]:

        return self.sort_by_score()[:limit]

    def get_low_adoption_features(
        self,
        threshold: float = 20.0
    ) -> List[FeatureAdoption]:

        return [
            feature
            for feature in self.get_all()
            if feature.adoption_rate < threshold
        ]

    # ---------------------------------------------------------
    # Search
    # ---------------------------------------------------------

    def find_by_trend(
        self,
        trend: str
    ) -> List[FeatureAdoption]:

        return [
            feature
            for feature in self.get_all()
            if feature.trend.lower() == trend.lower()
        ]

    def find_power_features(
        self,
        minimum_power_users: int = 10
    ) -> List[FeatureAdoption]:

        return [
            feature
            for feature in self.get_all()
            if feature.power_users >= minimum_power_users
        ]

    def find_inactive_features(self) -> List[FeatureAdoption]:

        return [
            feature
            for feature in self.get_all()
            if feature.adopted_users == 0
        ]

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def get_feature_names(self) -> List[str]:
        """Return all feature names."""
        return list(self._adoptions.keys())

    def summary(self) -> dict:
        """Repository summary."""

        highest = self.get_highest_adoption()
        lowest = self.get_lowest_adoption()

        return {
            "total_features": self.count(),
            "highest_adoption": (
                highest.feature_name if highest else None
            ),
            "lowest_adoption": (
                lowest.feature_name if lowest else None
            ),
        }

    def __len__(self):
        return len(self._adoptions)

    def __iter__(self):
        return iter(self._adoptions.values())

    def __str__(self):
        return (
            f"FeatureAdoptionRepository("
            f"features={self.count()})"
        )
