from __future__ import annotations

from statistics import mean
from typing import Dict, List

from src.ic08.models.feature_adoption import FeatureAdoption
from src.ic08.repositories.feature_adoption_repository import (
    FeatureAdoptionRepository,
)


class FeatureAdoptionService:
    """
    Service responsible for computing feature adoption analytics.
    """
    def __init__(self,
        feature_tracking_service: FeatureTrackingService,
        feature_repository: FeatureRepository,
        feature_adoption_repository: FeatureAdoptionRepository,):
        self.feature_tracking_service = feature_tracking_service
        self.feature_repository = feature_repository
        self.feature_adoption_repository = feature_adoption_repository
        

    # ---------------------------------------------------------
    # Adoption Rate
    # ---------------------------------------------------------

    def calculate_adoption_rate(
        self,
        adopted_users: int,
        total_users: int,
    ) -> float:

        if total_users == 0:
            return 0.0

        return round((adopted_users / total_users) * 100, 2)

    # ---------------------------------------------------------
    # Repeat Usage
    # ---------------------------------------------------------

    def calculate_repeat_usage(
        self,
        user_usage: Dict[str, int],
    ) -> float:

        if not user_usage:
            return 0.0

        repeat_users = sum(
            1
            for usage in user_usage.values()
            if usage >= 2
        )

        return round(
            (repeat_users / len(user_usage)) * 100,
            2,
        )

    # ---------------------------------------------------------
    # User Segmentation
    # ---------------------------------------------------------

    def identify_power_users(
        self,
        user_usage: Dict[str, int],
    ) -> tuple[int, int, int]:

        power_users = 0
        casual_users = 0
        inactive_users = 0

        for usage in user_usage.values():

            if usage >= 10:
                power_users += 1

            elif usage >= 1:
                casual_users += 1

            else:
                inactive_users += 1

        return (
            power_users,
            casual_users,
            inactive_users,
        )

    # ---------------------------------------------------------
    # Feature Score
    # ---------------------------------------------------------

    def calculate_feature_score(
        self,
        adoption_rate: float,
        repeat_usage_rate: float,
        average_usage: float,
        trend: str,
    ) -> float:

        trend_bonus = {
            "Increasing": 10,
            "Stable": 5,
            "Decreasing": 0,
        }.get(trend, 5)

        average_component = min(
            average_usage * 10,
            100,
        )

        score = (
            adoption_rate * 0.40
            + repeat_usage_rate * 0.30
            + average_component * 0.20
            + trend_bonus * 0.10
        )

        return round(score, 2)

    # ---------------------------------------------------------
    # Ranking
    # ---------------------------------------------------------

    def rank_features(self) -> List[FeatureAdoption]:

        features = self.feature_adoption_repository.get_all()

        return sorted(
            features,
            key=lambda x: x.score,
            reverse=True,
        )

    # ---------------------------------------------------------
    # Low Adoption Features
    # ---------------------------------------------------------

    def identify_low_adoption_features(
        self,
        threshold: float = 20.0,
    ) -> List[FeatureAdoption]:

        return [
            feature
            for feature in self.feature_adoption_repository.get_all()
            if feature.adoption_rate < threshold
        ]

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def generate_feature_statistics(self) -> dict:

        features = self.feature_adoption_repository.get_all()

        if not features:

            return {
                "total_features": 0,
                "average_adoption": 0,
                "highest_adoption": None,
                "lowest_adoption": None,
                "overall_score": 0,
            }

        average_adoption = mean(
            f.adoption_rate for f in features
        )

        overall_score = mean(
            f.score for f in features
        )

        highest = max(
            features,
            key=lambda x: x.adoption_rate,
        )

        lowest = min(
            features,
            key=lambda x: x.adoption_rate,
        )

        return {
            "total_features": len(features),
            "average_adoption": round(
                average_adoption,
                2,
            ),
            "highest_adoption": highest.feature_name,
            "lowest_adoption": lowest.feature_name,
            "overall_score": round(
                overall_score,
                2,
            ),
        }

    # ---------------------------------------------------------
    # Feature Analytics
    # ---------------------------------------------------------

    def generate_feature_analytics(
        self,
        feature_name: str,
        total_users: int,
        user_usage: Dict[str, int],
        trend: str = "Stable",
    ) -> FeatureAdoption:
        """
        Creates a FeatureAdoption object and stores it.
        """

        adopted_users = sum(
            1
            for count in user_usage.values()
            if count > 0
        )

        total_usage = sum(user_usage.values())

        average_usage = (
            total_usage / adopted_users
            if adopted_users
            else 0
        )

        adoption_rate = self.calculate_adoption_rate(
            adopted_users,
            total_users,
        )

        repeat_usage = self.calculate_repeat_usage(
            user_usage,
        )

        (
            power_users,
            casual_users,
            inactive_users,
        ) = self.identify_power_users(
            user_usage,
        )

        score = self.calculate_feature_score(
            adoption_rate,
            repeat_usage,
            average_usage,
            trend,
        )

        adoption = FeatureAdoption(
            feature_name=feature_name,
            total_users=total_users,
            adopted_users=adopted_users,
            adoption_rate=adoption_rate,
            repeat_usage_rate=repeat_usage,
            total_usage_count=total_usage,
            average_usage=round(
                average_usage,
                2,
            ),
            power_users=power_users,
            casual_users=casual_users,
            inactive_users=inactive_users,
            trend=trend,
            score=score,
        )

        self.feature_adoption_repository.save(
            adoption
        )

        return adoption

from collections import defaultdict
from datetime import datetime
from typing import Dict, List


    # ---------------------------------------------------------
    # Complete Feature Adoption Analysis
    # ---------------------------------------------------------

    def calculate_feature_adoption(
        self,
        feature_usage_data: Dict[str, Dict],
    ) -> List[FeatureAdoption]:
        """
        Build FeatureAdoption analytics for all features.

        Expected Input Format

        {
            "Search": {
                "total_users": 150,
                "user_usage": {
                    "U001": 12,
                    "U002": 4,
                    "U003": 1
                },
                "trend": "Increasing"
            }
        }
        """

        analytics = []

        # Optional: clear previous analytics
        self.feature_adoption_repository.clear()

        for feature_name, data in feature_usage_data.items():

            adoption = self.generate_feature_analytics(
                feature_name=feature_name,
                total_users=data.get("total_users", 0),
                user_usage=data.get("user_usage", {}),
                trend=data.get("trend", "Stable"),
            )

            analytics.append(adoption)

        return analytics

    # ---------------------------------------------------------
    # Time To Adoption
    # ---------------------------------------------------------

    def calculate_time_to_adoption(
        self,
        feature_release_date: datetime,
        first_usage_date: datetime,
    ) -> int:
        """
        Calculates number of days required
        for a feature to be adopted.
        """

        if (
            feature_release_date is None
            or first_usage_date is None
        ):
            return 0

        days = (
            first_usage_date -
            feature_release_date
        ).days

        return max(days, 0)

    # ---------------------------------------------------------
    # Dashboard
    # ---------------------------------------------------------

    def generate_dashboard(self) -> Dict:
        """
        Generates dashboard data for reports/UI.
        """

        statistics = self.generate_feature_statistics()

        ranked = self.rank_features()

        top_features = ranked[:10]

        low_features = self.identify_low_adoption_features()

        highest = (
            ranked[0].feature_name
            if ranked
            else None
        )

        lowest = (
            ranked[-1].feature_name
            if ranked
            else None
        )

        dashboard = {

            "statistics": statistics,

            "total_features":
                statistics["total_features"],

            "average_adoption":
                statistics["average_adoption"],

            "overall_score":
                statistics["overall_score"],

            "highest_adoption":
                highest,

            "lowest_adoption":
                lowest,

            "top_features":
                top_features,

            "low_adoption_features":
                low_features,

            "power_features":
                self.feature_adoption_repository.find_power_features(),

            "inactive_features":
                self.feature_adoption_repository.find_inactive_features(),

            "increasing_features":
                self.feature_adoption_repository.find_by_trend(
                    "Increasing"
                ),

            "stable_features":
                self.feature_adoption_repository.find_by_trend(
                    "Stable"
                ),

            "decreasing_features":
                self.feature_adoption_repository.find_by_trend(
                    "Decreasing"
                ),
        }

        return dashboard

    # ---------------------------------------------------------
    # Repository Summary
    # ---------------------------------------------------------

    def repository_summary(self) -> Dict:
        """
        Returns repository level summary.
        """

        return self.feature_adoption_repository.summary()

    # ---------------------------------------------------------
    # Export
    # ---------------------------------------------------------

    def export_feature_statistics(self) -> Dict:
        """
        Export all analytics in dictionary format.
        """

        return {
            "dashboard": self.generate_dashboard(),
            "statistics": self.generate_feature_statistics(),
            "features": [
                feature.to_dict()
                for feature in
                self.feature_adoption_repository.get_all()
            ],
        }
