"""
Privacy Report

Generates a summary of privacy detection,
data masking, and validation results.
"""

from collections import Counter

from src.ic07.models.masking_result import MaskingResult
from src.ic07.models.sensitive_field import SensitiveField


class PrivacyReport:
    """
    Generates a privacy compliance report.
    """

    def generate(
        self,
        sensitive_fields: list[SensitiveField],
        masking_result: MaskingResult | None,
        validation_result: dict,
    ) -> str:
        """
        Generate a formatted privacy report.
        """

        lines = []

        lines.append("=" * 60)
        lines.append("DATA PRIVACY REPORT")
        lines.append("=" * 60)

        lines.append("")
        lines.append(f"Sensitive Columns : {len(sensitive_fields)}")

        # --------------------------------------------------
        # Privacy Categories
        # --------------------------------------------------

        category_counts = Counter(
            field.privacy_category
            for field in sensitive_fields
        )

        lines.append("")
        lines.append("Privacy Categories")

        for category, count in sorted(category_counts.items()):
            lines.append(f"  {category:<15}: {count}")

        # --------------------------------------------------
        # Masking Methods
        # --------------------------------------------------

        lines.append("")
        lines.append("Masking Methods")

        for field in sensitive_fields:
            lines.append(
                f"  {field.column_name:<25}"
                f" -> {field.recommended_mask}"
            )

        # --------------------------------------------------
        # Masking Statistics
        # --------------------------------------------------

        if masking_result:

            lines.append("")
            lines.append("Execution Summary")

            lines.append(
                f"Rows Processed     : {masking_result.rows_processed}"
            )

            lines.append(
                f"Columns Masked     : {masking_result.columns_masked}"
            )

            lines.append(
                f"Records Masked     : {masking_result.records_masked}"
            )

            lines.append(
                f"Execution Time     : "
                f"{masking_result.execution_time:.3f} sec"
            )

            lines.append(
                f"Status             : "
                f"{'SUCCESS' if masking_result.success else 'FAILED'}"
            )

        # --------------------------------------------------
        # Validation
        # --------------------------------------------------

        lines.append("")
        lines.append("Validation")

        lines.append(
            f"Rows Match         : "
            f"{validation_result['rows_match']}"
        )

        lines.append(
            f"Columns Match      : "
            f"{validation_result['columns_match']}"
        )

        lines.append(
            f"Null Counts Match  : "
            f"{validation_result['null_counts_match']}"
        )

        lines.append(
            f"Masked Columns     : "
            f"{validation_result['masked_columns']}"
        )

        lines.append(
            f"Masking Percentage : "
            f"{validation_result['masking_percentage']:.1f}%"
        )

        lines.append(
            f"Validation Passed  : "
            f"{validation_result['validation_passed']}"
        )

        if validation_result["warnings"]:

            lines.append("")
            lines.append("Warnings")

            for warning in validation_result["warnings"]:
                lines.append(f"  - {warning}")

        # --------------------------------------------------
        # Compliance Score
        # --------------------------------------------------

        compliance = (
            validation_result["masking_percentage"]
            if validation_result["validation_passed"]
            else 0.0
        )

        lines.append("")
        lines.append(f"Overall Compliance : {compliance:.1f}%")

        lines.append("=" * 60)

        return "\n".join(lines)
