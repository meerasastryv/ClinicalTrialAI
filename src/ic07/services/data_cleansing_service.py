"""
Intelligent data cleansing service.
"""

from __future__ import annotations

from typing import Dict

import pandas as pd

from src.ic07.models.cleansing_action import CleansingAction
from src.ic07.repositories.cleansing_repository import (
    CleansingRepository,
)


class DataCleansingService:
    """
    Applies intelligent data cleansing operations based on
    validation results.
    """

    def __init__(self) -> None:
        self.repository = CleansingRepository()

    # ---------------------------------------------------------

    def clean(
        self,
        dataframe: pd.DataFrame,
        validation_result: Dict,
    ) -> Dict:
        """
        Clean the dataset using validation results.
        """

        cleaned_df = dataframe.copy()

        self.repository.clear()

        issues = validation_result.get(
            "issues",
            [],
        )

        processed = set()

        for issue in issues:

            key = (
                issue.column,
                issue.rule,
            )

            if key in processed:
                continue

            processed.add(key)

            if issue.rule == "Required":

                self._clean_required(
                    cleaned_df,
                    issue.column,
                )

            elif issue.rule == "Range":

                self._clean_range(
                    cleaned_df,
                    issue.column,
                )

            elif issue.rule == "Allowed Values":

                self._clean_allowed_values(
                    cleaned_df,
                    issue.column,
                )

            elif issue.rule == "Pattern":

                self._record_manual_review(
                    issue.column,
                    "Pattern Validation",
                )

            elif issue.rule == "Duplicate":

                self._record_manual_review(
                    issue.column,
                    "Duplicate Records",
                )

        return {
            "cleaned_dataframe": cleaned_df,
            "actions": self.repository.list_all(),
        }

    # ---------------------------------------------------------

    def _clean_required(
        self,
        dataframe: pd.DataFrame,
        column: str,
    ) -> None:
        """
        Fill missing values.
        """

        if dataframe[column].dtype == object:

            replacement = "Unknown"

        else:

            replacement = dataframe[column].median()

        affected = dataframe[column].isna().sum()

        dataframe[column] = dataframe[column].fillna(
            replacement
        )

        self.repository.add(
            CleansingAction(
                column=column,
                action="Missing Value Replacement",
                description=(
                    f"Filled missing values "
                    f"using {replacement}."
                ),
                rows_affected=int(affected),
                status="SUCCESS",
            )
        )

    # ---------------------------------------------------------

    def _clean_range(
        self,
        dataframe: pd.DataFrame,
        column: str,
    ) -> None:
        """
        Replace invalid numeric values.
        """

        invalid = dataframe[column] == -999999

        affected = invalid.sum()

        valid_values = dataframe.loc[
            ~invalid,
            column,
        ]

        if len(valid_values):

            replacement = valid_values.median()

            dataframe.loc[
                invalid,
                column,
            ] = replacement

        self.repository.add(
            CleansingAction(
                column=column,
                action="Range Correction",
                description=(
                    "Replaced invalid values "
                    "with median."
                ),
                rows_affected=int(affected),
                status="SUCCESS",
            )
        )

    # ---------------------------------------------------------

    def _clean_allowed_values(
        self,
        dataframe: pd.DataFrame,
        column: str,
    ) -> None:
        """
        Replace invalid categorical values.
        """

        invalid = dataframe[column] == -999999

        affected = invalid.sum()

        dataframe.loc[
            invalid,
            column,
        ] = "Unknown"

        self.repository.add(
            CleansingAction(
                column=column,
                action="Category Correction",
                description=(
                    "Replaced invalid values "
                    "with 'Unknown'."
                ),
                rows_affected=int(affected),
                status="SUCCESS",
            )
        )

    # ---------------------------------------------------------

    def _record_manual_review(
        self,
        column: str,
        action: str,
    ) -> None:
        """
        Record manual review action.
        """

        self.repository.add(
            CleansingAction(
                column=column,
                action=action,
                description=(
                    "Manual review required."
                ),
                rows_affected=0,
                status="PENDING",
            )
        )
