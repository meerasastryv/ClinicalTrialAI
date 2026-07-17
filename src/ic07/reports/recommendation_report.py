"""
recommendation_report.py

IC-07 - Test Data Intelligence Engine
Milestone 7 - Test Data Recommendation Engine

Generates a formatted report for dataset recommendations.
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List

from src.ic07.models.recommendation import Recommendation


class RecommendationReport:
    """
    Generates recommendation reports.
    """

    def __init__(self) -> None:
        self.generated_at = datetime.now()

    # ------------------------------------------------------------------

    def generate(
        self,
        recommendations: List[Recommendation],
        filters: Dict,
        execution_time: float = 0.0,
    ) -> None:
        """
        Generate recommendation report.
        """

        print("\n" + "=" * 80)
        print("TEST DATA RECOMMENDATION REPORT")
        print("=" * 80)

        print(
            f"Generated : "
            f"{self.generated_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        print(f"Execution Time : {execution_time:.2f} sec")

        self._print_filters(filters)

        self._print_recommendations(recommendations)

        self._print_statistics(recommendations)

        print("=" * 80)

    # ------------------------------------------------------------------

    def _print_filters(
        self,
        filters: Dict,
    ) -> None:

        print("\nSEARCH FILTERS")
        print("-" * 80)

        if not filters:
            print("No filters specified.")
            return

        for key, value in filters.items():
            print(f"{key:30}: {value}")

    # ------------------------------------------------------------------

    def _print_recommendations(
        self,
        recommendations: List[Recommendation],
    ) -> None:

        print("\nTOP RECOMMENDATIONS")
        print("-" * 80)

        if not recommendations:
            print("No matching datasets found.")
            return

        for recommendation in recommendations:

            print(f"Rank                : {recommendation.rank}")
            print(f"Dataset             : {recommendation.dataset_name}")
            print(f"Score               : {recommendation.score:.2f}")
            print(
                f"Confidence          : "
                f"{recommendation.confidence:.2f}%"
            )

            print(f"Reason              : {recommendation.reason}")

            if recommendation.matched_columns:
                print(
                    "Matched Columns    : "
                    + ", ".join(recommendation.matched_columns)
                )

            if recommendation.tags:
                print(
                    "Tags               : "
                    + ", ".join(recommendation.tags)
                )

            print(
                f"Quality Score       : "
                f"{recommendation.quality_score:.2f}"
            )

            print(
                f"Coverage Score      : "
                f"{recommendation.coverage_score:.2f}"
            )

            print(
                f"Similarity Score    : "
                f"{recommendation.similarity_score:.2f}"
            )

            print(
                f"Metadata Score      : "
                f"{recommendation.metadata_score:.2f}"
            )

            print(
                f"Usage Score         : "
                f"{recommendation.usage_score:.2f}"
            )

            print(
                f"Synthetic Score     : "
                f"{recommendation.synthetic_score:.2f}"
            )

            print(
                f"Synthetic Available : "
                f"{recommendation.synthetic_available}"
            )

            if recommendation.recommended_rows is not None:
                print(
                    f"Recommended Rows    : "
                    f"{recommendation.recommended_rows}"
                )

            print("-" * 80)

    # ------------------------------------------------------------------

    def _print_statistics(
        self,
        recommendations: List[Recommendation],
    ) -> None:

        print("\nSTATISTICS")
        print("-" * 80)

        if not recommendations:
            print("No statistics available.")
            return

        scores = [r.score for r in recommendations]

        print(f"Datasets Evaluated : {len(recommendations)}")
        print(f"Highest Score      : {max(scores):.2f}")
        print(f"Lowest Score       : {min(scores):.2f}")
        print(
            f"Average Score      : "
            f"{sum(scores) / len(scores):.2f}"
        )

        excellent = len([s for s in scores if s >= 90])
        good = len([s for s in scores if 80 <= s < 90])
        fair = len([s for s in scores if 70 <= s < 80])

        print(f"Excellent Matches  : {excellent}")
        print(f"Good Matches       : {good}")
        print(f"Fair Matches       : {fair}")
