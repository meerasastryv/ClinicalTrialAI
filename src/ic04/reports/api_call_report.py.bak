"""
api_call_report.py

Generates reports for runtime API calls.
"""

from datetime import datetime


class ApiCallReport:
    """
    Generates API call reports.
    """

    def __init__(self, api_call_repository):
        self.api_call_repository = api_call_repository

    def generate_report(self):
        """
        Generate API call report.
        """

        lines = []

        lines.append("=" * 80)
        lines.append("API CALL REPORT")
        lines.append("=" * 80)
        lines.append(f"Generated : {datetime.now()}")
        lines.append("")

        total_calls = self.api_call_repository.get_total_calls()

        lines.append(f"Total API Calls : {total_calls}")
        lines.append(
            f"Average Response Time : "
            f"{self.api_call_repository.get_average_duration():.3f} ms"
        )

        lines.append("")

        api_calls = self.api_call_repository.get_all_api_calls()

        if not api_calls:
            lines.append("No API calls recorded.")
            return "\n".join(lines)

        lines.append("-" * 80)

        lines.append(
            f"{'Method':10}"
            f"{'Endpoint':30}"
            f"{'Caller':20}"
            f"{'Duration(ms)':15}"
            f"{'Status':8}"
        )

        lines.append("-" * 80)

        for api_call in api_calls:

            lines.append(
                f"{api_call.http_method:10}"
                f"{api_call.endpoint:30}"
                f"{api_call.caller_method:20}"
                f"{api_call.duration_ms:15.3f}"
                f"{api_call.status_code:8}"
            )

        return "\n".join(lines)

    def print_report(self):
        """
        Print API call report.
        """
        print(self.generate_report())

    def save_report(self, output_file):
        """
        Save API call report.
        """

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(self.generate_report())

        return output_file
