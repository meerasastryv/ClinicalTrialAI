"""
IC-07 Metadata Analysis Report

Generates reports from metadata analysis.
"""

from __future__ import annotations

from typing import List

from src.ic07.models.data_field import DataField


class MetadataReport:
    """
    Generates metadata analysis reports.
    """

    def generate_summary(self, fields: List[DataField]) -> str:
        """
        Generate a textual summary report.
        """

        total_fields = len(fields)

        primary_keys = sum(field.primary_key for field in fields)

        nullable_fields = sum(field.nullable for field in fields)

        sensitive_fields = sum(field.sensitive for field in fields)

        lines = [
            "=" * 70,
            "IC-07 Metadata Analysis Report",
            "=" * 70,
            f"Total Fields      : {total_fields}",
            f"Primary Keys      : {primary_keys}",
            f"Nullable Fields   : {nullable_fields}",
            f"Sensitive Fields  : {sensitive_fields}",
            "",
            "Field Details",
            "-" * 70,
        ]

        for field in fields:
            lines.append(
                f"{field.field_name:<25}"
                f"{field.data_type:<12}"
                f"Length={field.length:<5}"
                f"Nullable={field.nullable:<5}"
                f"Unique={field.unique:<5}"
                f"Sensitive={field.sensitive}"
            )

        return "\n".join(lines)
