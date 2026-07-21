"""
Validation report.
"""

from typing import Any


class ValidationReport:
    """
    Generates validation reports.
    """

    @staticmethod
    def print_report(result: dict[str, Any]) -> None:

        print("\n" + "=" * 60)
        print("INTELLIGENT DATA VALIDATION REPORT")
        print("=" * 60)

        print(f"Rows              : {result['rows']}")
        print(f"Columns           : {result['columns']}")
        print(f"Rules Executed    : {result['rules']}")

        summary = result["summary"]

        print(f"Total Issues      : {summary['total_issues']}")

        print("\nIssue Summary")
        print("-" * 60)
        """
        for key, value in summary.items():
            if key != "total_issues":
                print(f"{key:20}: {value}")
        """
        labels = {"required": "Required",
            "range": "Range","pattern": "Pattern","duplicates": "Duplicates",
            "allowed_values": "Allowed Values","length": "Length","custom": "Custom",}
        for key, value in summary.items():
            if key != "total_issues":
                print(f"{labels[key]:20}: {value}")
        print("\nDetailed Issues")
        print("-" * 60)

        for issue in result["issues"]:

            print(
                f"Row={issue.row:<4}"
                f" Column={issue.column:<15}"
                f" Rule={issue.rule:<15}"
                f" Value={issue.value}"
            )
