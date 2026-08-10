"""
Synthetic Data Service
----------------------

Generates realistic synthetic datasets based on the source dataset.

Author : Meera Sastry
Project: ClinicalTrialAI
"""

from __future__ import annotations

import logging
import random
import string
import time
import uuid
from datetime import datetime, timedelta
from typing import Any

import numpy as np
import pandas as pd

from src.ic07.models.synthetic_data_request import SyntheticDataRequest
from src.ic07.models.synthetic_data_result import SyntheticDataResult

logger = logging.getLogger(__name__)


class SyntheticDataService:
    """Service responsible for generating synthetic datasets."""

    def __init__(self) -> None:
        logger.info("SyntheticDataService initialized.")

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------

    def generate(
        self,
        source_df: pd.DataFrame,
        request: SyntheticDataRequest,
    ) -> SyntheticDataResult:
        """
        Generate synthetic data.

        Parameters
        ----------
        source_df : pd.DataFrame
            Source dataset.

        request : SyntheticDataRequest
            Generation options.

        Returns
        -------
        SyntheticDataResult
        """

        start = time.time()

        if request.random_seed is not None:
            random.seed(request.random_seed)
            np.random.seed(request.random_seed)

        synthetic = pd.DataFrame()

        for column in source_df.columns:
            synthetic[column] = self._generate_column(
                source_df[column],
                request.rows,
                request.preserve_distribution,
            )

        if request.include_nulls:
            synthetic = self._apply_nulls(synthetic)

        if request.include_duplicates:
            synthetic = self._apply_duplicates(synthetic)

        if request.include_invalid_values:
            synthetic = self._apply_invalid_values(synthetic)

        if request.include_boundary_values:
            synthetic = self._apply_boundary_values(synthetic)

        generation_time = round(time.time() - start, 3)

        return SyntheticDataResult(
            generated_dataframe=synthetic,
            row_count=len(synthetic),
            column_count=len(synthetic.columns),
            duplicate_count=int(synthetic.duplicated().sum()),
            null_count=int(synthetic.isna().sum().sum()),
            invalid_count=0,
            generation_time=generation_time,
            warnings=[],
        )

    # ------------------------------------------------------------------
    # Column Generator
    # ------------------------------------------------------------------

    def _generate_column(
        self,
        series: pd.Series,
        rows: int,
        preserve_distribution: bool,
    ) -> pd.Series:

        dtype = series.dtype

        if pd.api.types.is_integer_dtype(dtype):
            return self._generate_numeric(series, rows, integer=True)

        if pd.api.types.is_float_dtype(dtype):
            return self._generate_numeric(series, rows, integer=False)

        if pd.api.types.is_bool_dtype(dtype):
            return self._generate_boolean(rows)

        if pd.api.types.is_datetime64_any_dtype(dtype):
            return self._generate_datetime(series, rows)

        return self._generate_string(series, rows)

    # ------------------------------------------------------------------
    # Numeric
    # ------------------------------------------------------------------

    def _generate_numeric(
        self,
        series: pd.Series,
        rows: int,
        integer: bool,
    ) -> pd.Series:

        minimum = series.min()
        maximum = series.max()

        if pd.isna(minimum) or pd.isna(maximum):
            minimum = 0
            maximum = 100

        values = np.random.uniform(minimum, maximum, rows)

        if integer:
            values = values.astype(int)

        return pd.Series(values)

    # ------------------------------------------------------------------
    # String
    # ------------------------------------------------------------------

    def _generate_string(
        self,
        series: pd.Series,
        rows: int,
    ) -> pd.Series:

        samples = (
            series.dropna()
            .astype(str)
            .unique()
            .tolist()
        )

        if samples:
            return pd.Series(
                random.choices(samples, k=rows)
            )

        return pd.Series(
            [
                "".join(
                    random.choices(
                        string.ascii_uppercase + string.digits,
                        k=8,
                    )
                )
                for _ in range(rows)
            ]
        )

    # ------------------------------------------------------------------
    # Boolean
    # ------------------------------------------------------------------

    def _generate_boolean(
        self,
        rows: int,
    ) -> pd.Series:

        return pd.Series(
            np.random.choice(
                [True, False],
                rows,
            )
        )

    # ------------------------------------------------------------------
    # DateTime
    # ------------------------------------------------------------------

    def _generate_datetime(
        self,
        series: pd.Series,
        rows: int,
    ) -> pd.Series:

        minimum = series.min()
        maximum = series.max()

        if pd.isna(minimum) or pd.isna(maximum):
            minimum = datetime.now() - timedelta(days=365)
            maximum = datetime.now()

        delta = (maximum - minimum).days

        values = [
            minimum + timedelta(days=random.randint(0, max(delta, 1)))
            for _ in range(rows)
        ]

        return pd.Series(values)

    # ------------------------------------------------------------------
    # Null Injection
    # ------------------------------------------------------------------

    def _apply_nulls(
        self,
        df: pd.DataFrame,
        percentage: float = 0.05,
    ) -> pd.DataFrame:

        total = int(df.size * percentage)

        for _ in range(total):
            r = random.randrange(df.shape[0])
            c = random.randrange(df.shape[1])
            df.iat[r, c] = np.nan

        return df

    def _apply_nulls(self,df: pd.DataFrame,percentage: float = 0.05,) -> pd.DataFrame:
        """
        Randomly inject null values into columns that support NaN.
        Boolean columns are skipped.
        """
        total = int(df.size * percentage)
        valid_columns = [i for i, column in enumerate(df.columns) if not pd.api.types.is_bool_dtype(df[column])]
        if not valid_columns:
            return df
        for _ in range(total):
             row = random.randrange(len(df))
             column = random.choice(valid_columns)
             df.iat[row, column] = np.nan
        return df 
    # ------------------------------------------------------------------
    # Duplicate Injection
    # ------------------------------------------------------------------
    def _apply_duplicates(
        self,
        df: pd.DataFrame,
        percentage: float = 0.05,
    ) -> pd.DataFrame:
        duplicates = int(len(df) * percentage)
        if duplicates == 0:
            return df

        sample = df.sample(
            duplicates,
            replace=True,
            random_state=42,
        )

        return pd.concat(
            [df, sample],
            ignore_index=True,
        )

    # ------------------------------------------------------------------
    # Invalid Values
    # ------------------------------------------------------------------

    def _apply_invalid_values(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        for column in df.columns:

            if pd.api.types.is_numeric_dtype(df[column]):

                idx = random.randrange(len(df))
                df.at[idx, column] = -999999

        return df

    # ------------------------------------------------------------------
    # Boundary Values
    # ------------------------------------------------------------------

    def _apply_boundary_values(
        self,
        df: pd.DataFrame,
    ) -> pd.DataFrame:

        for column in df.columns:

            if pd.api.types.is_numeric_dtype(df[column]):

                df.at[0, column] = df[column].min()

                if len(df) > 1:
                    df.at[1, column] = df[column].max()

        return df

    # ------------------------------------------------------------------
    # Output
    # ------------------------------------------------------------------

    def save_output(
        self,
        df: pd.DataFrame,
        filename: str,
        output_format: str = "csv",
    ) -> None:

        output_format = output_format.lower()

        if output_format == "csv":
            df.to_csv(filename, index=False)

        elif output_format == "json":
            df.to_json(filename, orient="records", indent=4)

        elif output_format == "excel":
            df.to_excel(filename, index=False)

        else:
            raise ValueError(f"Unsupported output format: {output_format}")

        logger.info("Synthetic dataset saved to %s", filename)
