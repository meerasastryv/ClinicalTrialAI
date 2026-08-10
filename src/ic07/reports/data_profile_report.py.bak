"""
IC-07 Data Profile Report

Generates reports from dataset profiling results.
"""

from __future__ import annotations

from typing import List

from src.ic07.models.data_profile import DataProfile


class DataProfileReport:
    """
    Generates reports for dataset profiling.
    """

    def generate_summary(
        self,
        profile: DataProfile
    ) -> str:
        """
        Generate a profiling summary report.
        """

        lines: List[str] = [
            "=" * 70,
            "IC-07 Data Profiling Report",
            "=" * 70,
            "",
            "Dataset Statistics",
            "-" * 70,
            f"Dataset ID           : {profile.dataset_id}",
            f"Profile ID           : {profile.profile_id}",
            f"Total Records        : {profile.total_records}",
            f"Total Fields         : {profile.total_fields}",
            f"Null Values          : {profile.null_values}",
            f"Duplicate Records    : {profile.duplicate_records}",
            f"Unique Records       : {profile.unique_records}",
            "",
            "Quality Metrics",
            "-" * 70,
            f"Completeness         : {profile.completeness:.2f}%",
            f"Uniqueness           : {profile.uniqueness:.2f}%",
            f"Consistency          : {profile.consistency:.2f}%",
            f"Validity             : {profile.validity:.2f}%",
            f"Accuracy             : {profile.accuracy:.2f}%",
            f"Overall Score        : {profile.overall_score:.2f}%",
            "",
            "Additional Metrics",
            "-" * 70,
        ]

        if profile.metrics:
            for name, value in sorted(profile.metrics.items()):
                lines.append(f"{name:<25}: {value}")
        else:
            lines.append("No additional metrics available.")

        lines.extend([
            "",
            "-" * 70,
            f"Profiled By : {profile.profiled_by}",
            f"Profiled At : {profile.profiled_at}",
            "=" * 70,
        ])

        return "\n".join(lines)
