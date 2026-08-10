"""
Intelligent data cleansing report.
"""

from __future__ import annotations

from datetime import datetime
from typing import List

from src.ic07.models.cleansing_action import (
    CleansingAction,
)


class DataCleansingReport:
    """
    Generates intelligent data cleansing reports.
    """

    def __init__(self) -> None:
        self.generated_at = datetime.now()

    # ------------------------------------------------------------------

    def generate(
        self,
        actions: List[CleansingAction],
    ) -> None:
        """
        Generate cleansing report.
        """

        print("\n" + "=" * 80)
        print(
            "INTELLIGENT DATA CLEANSING REPORT"
        )
        print("=" * 80)

        print(
            f"Generated : "
            f"{self.generated_at.strftime('%Y-%m-%d %H:%M:%S')}"
        )

        print(
            f"Total Actions : "
            f"{len(actions)}"
        )

        self._print_actions(actions)

        print("=" * 80)

    # ------------------------------------------------------------------

    def _print_actions(
        self,
        actions: List[CleansingAction],
    ) -> None:

        print("\nCLEANSING ACTIONS")
        print("-" * 80)

        if not actions:

            print(
                "No cleansing actions performed."
            )

            return

        for action in actions:

            print(
                f"Column         : "
                f"{action.column}"
            )

            print(
                f"Action         : "
                f"{action.action}"
            )

            print(
                f"Description    : "
                f"{action.description}"
            )

            print(
                f"Rows Affected  : "
                f"{action.rows_affected}"
            )

            print(
                f"Status         : "
                f"{action.status}"
            )

            print("-" * 80)
