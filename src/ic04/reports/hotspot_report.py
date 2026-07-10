"""
hotspot_report.py

Generates hotspot analysis reports.
"""

from datetime import datetime


class HotspotReport:
    """
    Generates hotspot analysis reports.
    """

    def __init__(self, hotspot_repository):
        self.hotspot_repository = hotspot_repository

    def generate_report(self):

        lines = []

        lines.append("=" * 80)
        lines.append("HOTSPOT ANALYSIS REPORT")
        lines.append("=" * 80)
        lines.append(f"Generated : {datetime.now()}")
        lines.append("")

        hotspots = self.hotspot_repository.get_sorted_hotspots()

        if not hotspots:
            lines.append("No hotspots detected.")
            return "\n".join(lines)

        lines.append(
            f"{'Method':30}"
            f"{'Calls':>10}"
            f"{'Avg(ms)':>15}"
            f"{'Total(ms)':>15}"
            f"{'Level':>10}"
        )

        lines.append("-" * 80)

        for hotspot in hotspots:

            lines.append(
                f"{hotspot.method_name:30}"
                f"{hotspot.call_count:>10}"
                f"{hotspot.average_time:>15.6f}"
                f"{hotspot.total_time:>15.6f}"
                f"{hotspot.hotspot_level:>10}"
            )

        return "\n".join(lines)

    def print_report(self):
        print(self.generate_report())

    def save_report(self, output_file):

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(self.generate_report())

        return output_file
