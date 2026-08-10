"""
Privacy Validation Service

Validates masking quality and structural integrity.
"""

from typing import Any

import pandas as pd

from src.ic07.models.sensitive_field import SensitiveField


class PrivacyValidationService:
    """
    Validates data masking results.
    """

    def validate(
        self,
        original_df: pd.DataFrame,
        masked_df: pd.DataFrame,
        sensitive_fields: list[SensitiveField],
    ) -> dict[str, Any]:
        """
        Validate masking quality.
        """

        validation = {
            "rows_match": True,
            "columns_match": True,
            "null_counts_match": True,
            "masked_columns": 0,
            "validation_passed": True,
            "warnings": [],
        }

        # -------------------------------------------------
        # Row count
        # -------------------------------------------------

        if len(original_df) != len(masked_df):
            validation["rows_match"] = False
            validation["validation_passed"] = False
            validation["warnings"].append(
                "Row count changed after masking."
            )

        # -------------------------------------------------
        # Column count
        # -------------------------------------------------

        if len(original_df.columns) != len(masked_df.columns):
            validation["columns_match"] = False
            validation["validation_passed"] = False
            validation["warnings"].append(
                "Column count changed after masking."
            )

        # -------------------------------------------------
        # Null count validation
        # -------------------------------------------------

        for column in original_df.columns:

            if column not in masked_df.columns:
                continue

            original_nulls = original_df[column].isna().sum()
            masked_nulls = masked_df[column].isna().sum()

            if original_nulls != masked_nulls:
                validation["null_counts_match"] = False
                validation["validation_passed"] = False

                validation["warnings"].append(
                    f"Null count changed for '{column}'."
                )

        # -------------------------------------------------
        # Sensitive column validation
        # -------------------------------------------------

        for field in sensitive_fields:

            column = field.column_name

            if column not in masked_df.columns:
                continue

            different = (
                original_df[column].fillna("").astype(str)
                !=
                masked_df[column].fillna("").astype(str)
            )

            if different.any():
                validation["masked_columns"] += 1
            else:
                validation["validation_passed"] = False

                validation["warnings"].append(
                    f"Column '{column}' appears unmasked."
                )

        validation["masking_percentage"] = (
            validation["masked_columns"]
            / max(len(sensitive_fields), 1)
        ) * 100

        return validation
