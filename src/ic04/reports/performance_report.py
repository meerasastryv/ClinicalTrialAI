"""
performance_report.py

Generates a formatted runtime performance analysis report.
"""

from datetime import datetime


class PerformanceReport:
    """
    Generates performance analysis reports from a PerformanceRepository.
    """

    def __init__(self, performance_repository):
        self.performance_repository = performance_repository

    def generate_report(self, top_n=10):
        """
        Generate a formatted performance report.

        Returns:
            str
        """

        lines = []

        lines.append("=" * 80)
        lines.append("PERFORMANCE ANALYSIS REPORT")
        lines.append("=" * 80)
        lines.append(f"Generated : {datetime.now()}")
        lines.append("")

        total_methods = self.performance_repository.get_total_methods()
        total_calls = self.performance_repository.get_total_calls()

        lines.append(f"Total Methods : {total_methods}")
        lines.append(f"Total Calls   : {total_calls}")
        lines.append("")

        metrics = self.performance_repository.get_sorted_by_average_time()

        if not metrics:
            lines.append("No runtime performance data available.")
            return "\n".join(lines)

        lines.append("-" * 80)
        lines.append("METHOD PERFORMANCE")
        lines.append("-" * 80)

        for metric in metrics:

            lines.append(f"Method        : {metric.method_name}")
            lines.append(f"Calls         : {metric.call_count}")
            lines.append(f"Average Time  : {metric.average_time:.6f} sec")
            lines.append(f"Minimum Time  : {metric.min_time:.6f} sec")
            lines.append(f"Maximum Time  : {metric.maximum_time:.6f} sec")
            lines.append(f"Total Time    : {metric.total_time:.6f} sec")
            lines.append("-" * 80)

        lines.append("")
        lines.append("=" * 80)
        lines.append(f"TOP {top_n} SLOWEST METHODS")
        lines.append("=" * 80)

        for index, metric in enumerate(metrics[:top_n], start=1):

            lines.append(
                f"{index:>2}. "
                f"{metric.method_name}"
            )

            lines.append(
                f"    Avg={metric.average_time:.6f} sec | "
                f"Max={metric.maximum_time:.6f} sec | "
                f"Calls={metric.call_count}"
            )

        return "\n".join(lines)

    def print_report(self, top_n=10):
        """
        Print the report.
        """

        print(self.generate_report(top_n))

    def save_report(self, output_file, top_n=10):
        """
        Save report to disk.
        """

        report = self.generate_report(top_n)

        with open(output_file, "w", encoding="utf-8") as file:
            file.write(report)

        return output_file
