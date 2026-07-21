"""
AI-assisted data quality recommendation engine.
"""

from __future__ import annotations

from typing import Dict, Set, Tuple

from src.ic07.models.quality_recommendation import (
    QualityRecommendation,
)
from src.ic07.repositories.quality_recommendation_repository import (
    QualityRecommendationRepository,
)


class QualityRecommendationEngine:
    """
    Generates recommendations from validation results.
    """

    def __init__(self) -> None:
        self.repository = QualityRecommendationRepository()

    # ------------------------------------------------------------------

    def generate(
        self,
        validation_result: Dict,
    ) -> list[QualityRecommendation]:
        """
        Generate recommendations from validation issues.
        """

        self.repository.clear()

        issues = validation_result.get(
            "issues",
            [],
        )

        seen: Set[Tuple[str, str]] = set()

        for issue in issues:

            key = (
                issue.column,
                issue.rule,
            )

            if key in seen:
                continue

            seen.add(key)

            recommendation = self._create_recommendation(
                issue
            )

            if recommendation:
                self.repository.add(
                    recommendation
                )

        return self.repository.list_all()

    # ------------------------------------------------------------------

    def _create_recommendation(
        self,
        issue,
    ) -> QualityRecommendation | None:
        """
        Create recommendation for a validation issue.
        """

        if issue.rule == "Required":

            return QualityRecommendation(
                category="Missing Values",
                column=issue.column,
                issue="Missing values detected",
                recommendation=(
                    "Populate missing values using "
                    "median, default values, or "
                    "business rules."
                ),
                priority="HIGH",
            )

        if issue.rule == "Range":

            return QualityRecommendation(
                category="Range Validation",
                column=issue.column,
                issue="Invalid numeric values",
                recommendation=(
                    "Replace values outside the "
                    "permitted range."
                ),
                priority="HIGH",
            )

        if issue.rule == "Pattern":

            return QualityRecommendation(
                category="Pattern Validation",
                column=issue.column,
                issue="Invalid format",
                recommendation=(
                    "Correct values to match the "
                    "expected pattern."
                ),
                priority="MEDIUM",
            )

        if issue.rule == "Allowed Values":

            return QualityRecommendation(
                category="Allowed Values",
                column=issue.column,
                issue="Unexpected category",
                recommendation=(
                    "Replace with one of the "
                    "approved values."
                ),
                priority="MEDIUM",
            )

        if issue.rule == "Duplicate":

            return QualityRecommendation(
                category="Duplicate Records",
                column=issue.column,
                issue="Duplicate values found",
                recommendation=(
                    "Remove or merge duplicate "
                    "records."
                ),
                priority="MEDIUM",
            )

        if issue.rule == "Custom":

            return QualityRecommendation(
                category="Business Rules",
                column=issue.column,
                issue="Business rule violation",
                recommendation=(
                    "Review and correct the "
                    "values according to "
                    "business rules."
                ),
                priority="HIGH",
            )

        return None
