"""
IC-07 Metadata Analyzer

Analyzes datasets and automatically discovers
metadata describing the dataset structure.
"""

from __future__ import annotations

import logging
from collections import Counter
from typing import Any, Dict, List

from src.ic07.models.data_field import DataField
from src.ic07.models.data_set import DataSet

logger = logging.getLogger(__name__)


class MetadataAnalyzer:
    """
    Performs metadata analysis for datasets.
    """

    def __init__(self):
        self.logger = logger

    # -------------------------------------------------------------
    # Public API
    # -------------------------------------------------------------

    def analyze(self, dataset: DataSet) -> List[DataField]:
        """
        Analyze an entire dataset.
        """

        self.logger.info(
            "Analyzing dataset '%s'...",
            dataset.name
        )

        discovered_fields: List[DataField] = []

        field_names = self._collect_field_names(dataset)

        for field_name in sorted(field_names):

            field = self._analyze_field(
                dataset,
                field_name
            )

            discovered_fields.append(field)

        self.logger.info(
            "Discovered %d fields.",
            len(discovered_fields)
        )

        return discovered_fields

    # -------------------------------------------------------------
    # Helpers
    # -------------------------------------------------------------

    def _collect_field_names(
        self,
        dataset: DataSet
    ) -> set[str]:

        fields = set()

        for record in dataset.records:
            fields.update(record.values.keys())

        return fields

    def _analyze_field(
        self,
        dataset: DataSet,
        field_name: str
    ) -> DataField:

        values = []

        null_count = 0

        for record in dataset.records:

            value = record.values.get(field_name)

            if value is None:
                null_count += 1
            else:
                values.append(value)

        data_type = self._infer_type(values)

        max_length = self._max_length(values)

        unique = len(values) == len(set(values))

        nullable = null_count > 0

        sensitive = self._is_sensitive(field_name)

        primary_key = unique and not nullable

        return DataField(
            field_name=field_name,
            data_type=data_type,
            length=max_length,
            nullable=nullable,
            unique=unique,
            primary_key=primary_key,
            sensitive=sensitive,
            description=f"Auto-discovered field: {field_name}"
        )

    # -------------------------------------------------------------
    # Type Detection
    # -------------------------------------------------------------

    def _infer_type(
        self,
        values: List[Any]
    ) -> str:

        if not values:
            return "unknown"

        types = Counter(type(v).__name__ for v in values)

        return types.most_common(1)[0][0]

    def _max_length(
        self,
        values: List[Any]
    ) -> int:

        if not values:
            return 0

        return max(len(str(v)) for v in values)

    # -------------------------------------------------------------
    # Sensitive Data Detection
    # -------------------------------------------------------------

    def _is_sensitive(
        self,
        field_name: str
    ) -> bool:

        keywords = {
            "password",
            "email",
            "phone",
            "mobile",
            "ssn",
            "aadhaar",
            "pan",
            "dob",
            "creditcard",
            "card",
            "cvv",
            "passport",
            "patient",
            "medical"
        }

        field = field_name.lower()

        return any(keyword in field for keyword in keywords)

    # -------------------------------------------------------------
    # Summary
    # -------------------------------------------------------------

    def summarize(
        self,
        fields: List[DataField]
    ) -> Dict[str, int]:

        return {
            "total_fields": len(fields),
            "primary_keys": sum(
                field.primary_key
                for field in fields
            ),
            "nullable_fields": sum(
                field.nullable
                for field in fields
            ),
            "sensitive_fields": sum(
                field.sensitive
                for field in fields
            )
        }
