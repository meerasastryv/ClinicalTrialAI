"""
AI-assisted quality recommendation report.
"""

from __future__ import annotations

from datetime import datetime
from typing import List

from src.ic07.models.quality_recommendation import (
    QualityRecommendation,
)


class QualityRecommendationReport:
    """
    Generates quality recommendation reports.
    """

    def __init__(self) -> None:
        self.generated_at = datetime.now()

    # ------------------------------------------------------------------

    def generate(
        self,
        recommendations: List[
            QualityRecommendation
        ],
    ) -> None:
        """
        Generate recommendation report.
        """

        print("\n" + "=" * 80)
        print(
            "AI-ASSISTED DATA QUALITY "
            "RECOMMENDATION REPORT"
        )
        print("=" * 80)

        print(
            f"Generated : "
            f"{self.generated_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        print(
            f"Total Recommendations : "
            f"{len(recommendations)}"
        )

        self._print_recommendations(
            recommendations
        )

        print("=" * 80)

    # ------------------------------------------------------------------

    def _print_recommendations(
        self,
        recommendations: List[
            QualityRecommendation
        ],
    ) -> None:

        print("\nRECOMMENDATIONS")
        print("-" * 80)

        if not recommendations:
            print(
                "No recommendations generated."
            )
            return

        for recommendation in recommendations:

            print(
                f"Priority       : "
                f"{recommendation.priority}"
            )

            print(
                f"Category       : "
                f"{recommendation.category}"
            )

            print(
                f"Column         : "
                f"{recommendation.column}"
            )

            print(
                f"Issue          : "
                f"{recommendation.issue}"
            )

            print(
                f"Recommendation : "
                f"{recommendation.recommendation}"
            )

            print("-" * 80)
