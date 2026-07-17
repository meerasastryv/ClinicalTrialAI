"""
search_report.py

IC-07 - Test Data Intelligence Engine
Milestone 8 - Intelligent Test Data Search

Generates a formatted report for Intelligent Search results.
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List

from src.ic07.models.search_result import SearchResult


class SearchReport:
    """
    Generates Intelligent Search reports.
    """

    def __init__(self) -> None:
        self.generated_at = datetime.now()

    # ------------------------------------------------------------------

    def generate(
        self,
        query: str,
        results: List[SearchResult],
        filters: Dict,
        execution_time: float = 0.0,
    ) -> None:
        """
        Generate the search report.
        """

        print("\n" + "=" * 80)
        print("INTELLIGENT TEST DATA SEARCH REPORT")
        print("=" * 80)

        print(
            f"Generated : "
            f"{self.generated_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        print(f"Execution Time : {execution_time:.2f} sec")

        print("\nSEARCH QUERY")
        print("-" * 80)
        print(query)

        self._print_filters(filters)

        self._print_results(results)

        self._print_statistics(results)

        print("=" * 80)

    # ------------------------------------------------------------------

    def _print_filters(
        self,
        filters: Dict,
    ) -> None:

        print("\nSEARCH FILTERS")
        print("-" * 80)

        if not filters:
            print("No filters specified.")
            return

        for key, value in filters.items():
            print(f"{key:30}: {value}")

    # ------------------------------------------------------------------

    def _print_results(
        self,
        results: List[SearchResult],
    ) -> None:

        print("\nSEARCH RESULTS")
        print("-" * 80)

        if not results:
            print("No matching datasets found.")
            return

        for result in results:

            print(f"Rank                 : {result.rank}")
            print(f"Dataset              : {result.dataset_name}")
            print(f"Search Type          : {result.search_type}")

            print(
                f"Search Score         : "
                f"{result.score:.2f}"
            )

            print(
                f"Confidence           : "
                f"{result.confidence:.2f}%"
            )

            print(f"Reason               : {result.reason}")

            if result.matched_fields:
                print(
                    "Matched Fields       :
