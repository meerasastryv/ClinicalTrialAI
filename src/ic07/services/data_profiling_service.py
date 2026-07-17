"""
IC-07 Data Profiling Service

Profiles datasets and calculates quality metrics.
"""

from __future__ import annotations

import logging
from typing import Dict, List

from src.ic07.models.data_profile import DataProfile
from src.ic07.models.data_set import DataSet

logger = logging.getLogger(__name__)


class DataProfilingService:
    """
    Profiles datasets and computes data quality metrics.
    """

    def __init__(self):
        self.logger = logger

    # -------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------

    def profile_dataset(
        self,
        dataset: DataSet
    ) -> DataProfile:
        """
        Generate a profile for a dataset.
        """

        self.logger.info(
            "Profiling dataset '%s'...",
            dataset.name
        )

        total_records = dataset.record_count
        total_fields = dataset.field_count

        null_values = self._count_null_values(dataset)

        duplicate_records = self._count_duplicates(dataset)

        unique_records = max(
            total_records - duplicate_records,
            0
        )

        completeness = self._calculate_completeness(
            total_records,
            total_fields,
            null_values
        )

        uniqueness = self._calculate_uniqueness(
            total_records,
            duplicate_records
        )

        profile = DataProfile(
            profile_id=f"profile_{dataset.dataset_id}",
            dataset_id=dataset.dataset_id,
            total_records=total_records,
            total_fields=total_fields,
            null_values=null_values,
            duplicate_records=duplicate_records,
            unique_records=unique_records,
            completeness=completeness,
            uniqueness=uniqueness,
            consistency=100.0,
            validity=100.0,
            accuracy=100.0,
        )

        profile.calculate_overall_score()

        profile.add_metric(
            "null_percentage",
            self._null_percentage(
                total_records,
                total_fields,
                null_values
            )
        )

        profile.add_metric(
            "duplicate_percentage",
            self._duplicate_percentage(
                total_records,
                duplicate_records
            )
        )

        profile.add_metric(
            "record_density",
            self._record_density(
                total_records,
                total_fields
            )
        )

        self.logger.info(
            "Profiling completed."
        )

        return profile

    # -------------------------------------------------------------
    # Statistics
    # -------------------------------------------------------------

    def _count_null_values(
        self,
        dataset: DataSet
    ) -> int:

        count = 0

        for record in dataset.records:

            for value in record.values.values():

                if value is None or value == "":
                    count += 1

        return count

    def _count_duplicates(
        self,
        dataset: DataSet
    ) -> int:

        seen = set()

        duplicates = 0

        for record in dataset.records:

            key = tuple(
                sorted(record.values.items())
            )

            if key in seen:
                duplicates += 1
            else:
                seen.add(key)

        return duplicates

    # -------------------------------------------------------------
    # Quality Metrics
    # -------------------------------------------------------------

    def _calculate_completeness(
        self,
        total_records: int,
        total_fields: int,
        null_values: int
    ) -> float:

        if total_records == 0 or total_fields == 0:
            return 100.0

        total_values = total_records * total_fields

        return (
            (total_values - null_values)
            / total_values
        ) * 100

    def _calculate_uniqueness(
        self,
        total_records: int,
        duplicate_records: int
    ) -> float:

        if total_records == 0:
            return 100.0

        return (
            (total_records - duplicate_records)
            / total_records
        ) * 100

    # -------------------------------------------------------------
    # Derived Metrics
    # -------------------------------------------------------------

    def _null_percentage(
        self,
        total_records: int,
        total_fields: int,
        null_values: int
    ) -> float:

        if total_records == 0 or total_fields == 0:
            return 0.0

        return (
            null_values /
            (total_records * total_fields)
        ) * 100

    def _duplicate_percentage(
        self,
        total_records: int,
        duplicate_records: int
    ) -> float:

        if total_records == 0:
            return 0.0

        return (
            duplicate_records /
            total_records
        ) * 100

    def _record_density(
        self,
        total_records: int,
        total_fields: int
    ) -> float:

        return float(total_records * total_fields)
