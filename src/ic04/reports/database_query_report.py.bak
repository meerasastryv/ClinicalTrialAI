"""
database_query_report.py

Generates reports for runtime database queries.
"""

from datetime import datetime


class DatabaseQueryReport:
    """
    Generates database query reports.
    """

    def __init__(self, database_query_repository):
        self.database_query_repository = database_query_repository

    def generate_report(self):
        """
        Generate database query report.
        """

        lines = []

        lines.append("=" * 80)
        lines.append("DATABASE QUERY REPORT")
        lines.append("=" * 80)
        lines.append(f"Generated : {datetime.now()}")
        lines.append("")

        total_queries = (
            self.database_query_repository.get_total_queries()
        )

        average_duration = (
            self.database_query_repository.get_average_duration()
        )

        total_rows = (
            self.database_query_repository.get_total_rows_affected()
        )

        lines.append(f"Total Queries        : {total_queries}")
        lines.append(
            f"Average Query Time   : {average_duration:.3f} ms"
        )
        lines.append(
            f"Total Rows Affected  : {total_rows}"
        )

        lines.append("")

        queries = (
            self.database_query_repository.get_all_queries()
        )

        if not queries:
            lines.append("No database queries recorded.")
            return "\n".join(lines)

        lines.append("-" * 90)

        lines.append(
            f"{'Operation':12}"
            f"{'Table':20}"
            f"{'Caller':20}"
            f"{'Duration(ms)':15}"
            f"{'Rows':8}"
        )

        lines.append("-" * 90)

        for query in queries:

            lines.append(
                f"{query.operation:12}"
                f"{query.table_name:20}"
                f"{query.caller_method:20}"
                f"{query.duration_ms:15.3f}"
                f"{query.rows_affected:8}"
            )

        return "\n".join(lines)

    def print_report(self):
        """
        Print database query report.
        """
        print(self.generate_report())

    def save_report(self, output_file):
        """
        Save report to a file.
        """

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(self.generate_report())

        return output_file
