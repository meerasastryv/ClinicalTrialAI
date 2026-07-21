"""
Data Masking Service

Applies masking algorithms to sensitive columns.
"""

from __future__ import annotations

import random
import time

import pandas as pd

from src.ic07.models.masking_result import MaskingResult
from src.ic07.models.sensitive_field import SensitiveField
from src.ic07.repositories.privacy_repository import PrivacyRepository


class DataMaskingService:
    """
    Performs masking of sensitive data.
    """

    def __init__(self, repository: PrivacyRepository):
        self.repository = repository

    def mask_dataframe(
        self,
        df: pd.DataFrame,
        sensitive_fields: list[SensitiveField],
    ) -> pd.DataFrame:
        """
        Return a masked copy of the dataframe.
        """

        start = time.time()

        masked_df = df.copy()

        records_masked = 0

        for field in sensitive_fields:

            column = field.column_name

            if column not in masked_df.columns:
                continue

            method = field.recommended_mask

            masked_df[column] = masked_df[column].apply(
                lambda value: self._mask_value(value, method)
            )

            records_masked += len(masked_df)

        result = MaskingResult(
            rows_processed=len(masked_df),
            columns_masked=len(sensitive_fields),
            records_masked=records_masked,
            execution_time=time.time() - start,
            success=True,
            message="Masking completed successfully."
        )

        self.repository.save_result(result)

        return masked_df

    # ----------------------------------------------------
    # Individual masking algorithms
    # ----------------------------------------------------

    def _mask_value(
        self,
        value,
        method: str
    ):

        if pd.isna(value):
            return value

        text = str(value)

        if method == "Name Replacement":
            return f"Person_{random.randint(1000,9999)}"

        if method == "Email Masking":
            return f"user{random.randint(100,999)}@masked.com"

        if method == "Phone Masking":
            if len(text) >= 6:
                return text[:2] + "XXXX" + text[-4:]
            return "XXXX"

        if method == "Date Generalization":
            if len(text) >= 4:
                return text[:4] + "-XX-XX"
            return "XXXX"

        if method == "Age Generalization":
            try:
                age = int(text)
                lower = (age // 5) * 5
                upper = lower + 5
                return f"{lower}-{upper}"
            except ValueError:
                return "Unknown"

        if method == "Address Masking":
            return f"City_{random.randint(1,999)}"

        if method == "PAN Masking":
            if len(text) >= 10:
                return text[:5] + "****" + text[-1]
            return "********"

        return f"TOKEN_{random.randint(1000,9999)}"
