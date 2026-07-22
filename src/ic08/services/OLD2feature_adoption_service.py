"""
feature_adoption_service.py

Refactored Feature Adoption Analytics Service for IC-08.
"""

from __future__ import annotations

from statistics import mean
from typing import Dict, List

from src.ic08.models.feature_adoption import FeatureAdoption
from src.ic08.models.feature_usage import FeatureUsage
from src.ic08.repositories.feature_adoption_repository import FeatureAdoptionRepository
from src.ic08.repositories.feature_repository import FeatureRepository
from src.ic08.services.feature_tracking_service import FeatureTrackingService


class FeatureAdoptionService:

    def __init__(
        self,
        feature_tracking_service: FeatureTrackingService,
        feature_repository: FeatureRepository,
        feature_adoption_repository: FeatureAdoptionRepository,
    ) -> None:
        self.feature_tracking_service = feature_tracking_service
        self.feature_repository = feature_repository
        self.feature_adoption_repository = feature_adoption_repository

    def calculate_adoption_rate(self, adopted_users: int, total_users: int) -> float:
        if total_users == 0:
            return 0.0
        return round((adopted_users / total_users) * 100, 2)

    def calculate_feature_score(
        self,
        adoption_rate: float,
        repeat_usage_rate: float,
        average_usage: float,
        trend: str,
    ) -> float:
        trend_bonus = {"Increasing": 10, "Stable": 5, "Decreasing": 0}.get(trend, 5)
        avg_component = min(average_usage * 10, 100)
        return round(
            adoption_rate * 0.40 +
            repeat_usage_rate * 0.30 +
            avg_component * 0.20 +
            trend_bonus * 0.10,
            2,
        )

    def _build_feature_adoption(self, feature: FeatureUsage) -> FeatureAdoption:
        adopted_users = feature.unique_users
        total_users = max(feature.unique_users, 1)

        adoption_rate = self.calculate_adoption_rate(adopted_users, total_users)

        repeat_usage_rate = 0.0
        if feature.total_usage > 0 and feature.unique_users > 0:
            repeat_usage_rate = round(
                max(feature.total_usage - feature.unique_users, 0)
                / feature.total_usage * 100,
                2,
            )

        average_usage = (
            feature.total_usage / feature.unique_users
            if feature.unique_users > 0 else feature.total_usage
        )

        trend = "Increasing" if feature.success_rate >= 95 else (
            "Stable" if feature.success_rate >= 80 else "Decreasing"
        )

        score = self.calculate_feature_score(
            adoption_rate,
            repeat_usage_rate,
            average_usage,
            trend,
        )

        return FeatureAdoption(
            feature_name=feature.feature_name,
            total_users=total_users,
            adopted_users=adopted_users,
            adoption_rate=adoption_rate,
            repeat_usage_rate=repeat_usage_rate,
            total_usage_count=feature.total_usage,
            average_usage=round(average_usage, 2),
            first_use=feature.created_at,
            last_use=feature.last_used,
            power_users=0,
            casual_users=adopted_users,
            inactive_users=max(total_users - adopted_users, 0),
            trend=trend,
            score=score,
        )

    def calculate_feature_adoption(self) -> List[FeatureAdoption]:
        self.feature_adoption_repository.clear()
        analytics: List[FeatureAdoption] = []
        for feature in self.feature_repository.get_all_features():
            adoption = self._build_feature_adoption(feature)
            self.feature_adoption_repository.save(adoption)
            analytics.append(adoption)
        return analytics

    def rank_features(self) -> List[FeatureAdoption]:
        return self.feature_adoption_repository.sort_by_score()

    def identify_low_adoption_features(
        self,
        threshold: float = 20.0,
    ) -> List[FeatureAdoption]:
        return self.feature_adoption_repository.get_low_adoption_features(threshold)

    def generate_feature_statistics(self) -> Dict:
        features = self.feature_adoption_repository.get_all()
        if not features:
            return {
                "total_features": 0,
                "average_adoption": 0.0,
                "highest_adoption": None,
                "lowest_adoption": None,
                "overall_score": 0.0,
            }
        return {
            "total_features": len(features),
            "average_adoption": round(mean(f.adoption_rate for f in features), 2),
            "highest_adoption": max(features, key=lambda x: x.adoption_rate).feature_name,
            "lowest_adoption": min(features, key=lambda x: x.adoption_rate).feature_name,
            "overall_score": round(mean(f.score for f in features), 2),
        }

    def generate_dashboard(self) -> Dict:
        """
        Generates dashboard data for reports/UI.
        """
        statistics = self.generate_feature_statistics()
        ranked = self.rank_features()
        return {
            "statistics": statistics,
            "total_features":
            statistics["total_features"],
		"average_adoption":
            statistics["average_adoption"],
	    "overall_score":
		    statistics["overall_score"],
		"highest_adoption":
		    statistics["highest_adoption"],
		"lowest_adoption":
		    statistics["lowest_adoption"],
		"top_features":
		    ranked[:10],
		"low_adoption_features":
		    self.identify_low_adoption_features(),
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


    def generate_dashboard(self) -> Dict:
        return {
            "statistics": self.generate_feature_statistics(),
            "top_features": self.rank_features()[:10],
            "low_adoption_features": self.identify_low_adoption_features(),
            "power_features": self.feature_adoption_repository.find_power_features(),
            "inactive_features": self.feature_adoption_repository.find_inactive_features(),
        }

    def repository_summary(self) -> Dict:
        return self.feature_adoption_repository.summary()

    def export_feature_statistics(self) -> Dict:
        return {
            "dashboard": self.generate_dashboard(),
            "statistics": self.generate_feature_statistics(),
            "features": [
                feature.to_dict()
                for feature in self.feature_adoption_repository.get_all()
            ],
        }
