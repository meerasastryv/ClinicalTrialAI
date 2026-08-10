"""
Synthetic Data Report

Author : Meera Sastry
Project : ClinicalTrialAI
"""

from __future__ import annotations

from src.ic07.models.synthetic_data_result import SyntheticDataResult


class SyntheticDataReport:
    """
    Generates a console report for synthetic data generation.
    """

    def print_report(
        self,
        result: SyntheticDataResult,
    ) -> None:

        print("\n" + "=" * 70)
        print("Synthetic Data Report")
        print("=" * 70)

        print(f"Rows Generated     : {result.row_count}")
        print(f"Columns            : {result.column_count}")
        print(f"Duplicate Rows     : {result.duplicate_count}")
        print(f"Null Values        : {result.null_count}")
        print(f"Invalid Values     : {result.invalid_count}")
        print(f"Generation Time    : {result.generation_time:.3f} sec")

        if result.warnings:
            print("\nWarnings")
            print("-" * 70)

            for warning in result.warnings:
                print(f"- {warning}")

        print("=" * 70)
