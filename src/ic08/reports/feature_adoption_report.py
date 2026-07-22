from __future__ import annotations

from typing import List

from src.ic08.models.feature_adoption import FeatureAdoption
from src.ic08.services.feature_adoption_service import (
    FeatureAdoptionService,
)


class FeatureAdoptionReport:
    """
    Generates Feature Adoption Analytics reports.
    """

    def __init__(
        self,
        feature_adoption_service: FeatureAdoptionService,
    ):
        self.service = feature_adoption_service

    # ---------------------------------------------------------
    # Main Report
    # ---------------------------------------------------------

    def print_report(self) -> None:

        dashboard = self.service.generate_dashboard()

        print("\n" + "=" * 70)
        print("FEATURE ADOPTION ANALYTICS")
        print("=" * 70)

        print()

        header = (
            f"{'Feature':25}"
            f"{'Users':>10}"
            f"{'Adoption%':>12}"
            f"{'Avg Usage':>12}"
            f"{'Power':>10}"
            f"{'Trend':>15}"
            f"{'Score':>10}"
        )

        print(header)
        print("-" * len(header))

        for feature in self.service.rank_features():

            print(
                f"{feature.feature_name:25}"
                f"{feature.adopted_users:>10}"
                f"{feature.adoption_rate:>12.2f}"
                f"{feature.average_usage:>12.2f}"
                f"{feature.power_users:>10}"
                f"{feature.trend:>15}"
                f"{feature.score:>10.2f}"
            )

        print()

        self.print_top_features()

        self.print_low_adoption_features()

        self.print_power_features()

        self.print_trend_summary()

        self.print_statistics()

        print("=" * 70)

    # ---------------------------------------------------------
    # Top Features
    # ---------------------------------------------------------

    def print_top_features(self):

        print("\nTop Features")
        print("-" * 70)

        for feature in self.service.rank_features()[:10]:

            print(
                f"{feature.feature_name:30}"
                f"{feature.score:>8.2f}"
            )

    # ---------------------------------------------------------
    # Low Adoption
    # ---------------------------------------------------------

    def print_low_adoption_features(self):

        print("\nLow Adoption Features")
        print("-" * 70)

        for feature in self.service.identify_low_adoption_features():

            print(
                f"{feature.feature_name:30}"
                f"{feature.adoption_rate:>8.2f}%"
            )

    # ---------------------------------------------------------
    # Power Features
    # ---------------------------------------------------------

    def print_power_features(self):

        print("\nPower User Features")
        print("-" * 70)

        features = (
            self.service
            .feature_adoption_repository
            .find_power_features()
        )

        if not features:
            print("None")
            return

        for feature in features:

            print(
                f"{feature.feature_name:30}"
                f"{feature.power_users:>8}"
            )

    # ---------------------------------------------------------
    # Trend Summary
    # ---------------------------------------------------------

    def print_trend_summary(self):

        print("\nTrend Summary")
        print("-" * 70)

        dashboard = self.service.generate_dashboard()

        print(
            f"Increasing : "
            f"{len(dashboard['increasing_features'])}"
        )

        print(
            f"Stable     : "
            f"{len(dashboard['stable_features'])}"
        )

        print(
            f"Decreasing : "
            f"{len(dashboard['decreasing_features'])}"
        )

    # ---------------------------------------------------------
    # Statistics
    # ---------------------------------------------------------

    def print_statistics(self):

        stats = self.service.generate_feature_statistics()

        print("\nOverall Statistics")
        print("-" * 70)

        print(
            f"Total Features      : "
            f"{stats['total_features']}"
        )

        print(
            f"Average Adoption    : "
            f"{stats['average_adoption']:.2f}%"
        )

        print(
            f"Highest Adoption    : "
            f"{stats['highest_adoption']}"
        )

        print(
            f"Lowest Adoption     : "
            f"{stats['lowest_adoption']}"
        )

        print(
            f"Overall Score       : "
            f"{stats['overall_score']:.2f}"
        )

    # ---------------------------------------------------------
    # Dictionary Export
    # ---------------------------------------------------------

    def to_dict(self):

        return self.service.export_feature_statistics()

    # ---------------------------------------------------------
    # String Representation
    # ---------------------------------------------------------

    def __str__(self):

        stats = self.service.generate_feature_statistics()

        return (
            f"FeatureAdoptionReport("
            f"features={stats['total_features']}, "
            f"average_adoption="
            f"{stats['average_adoption']:.2f}%)"
        )
