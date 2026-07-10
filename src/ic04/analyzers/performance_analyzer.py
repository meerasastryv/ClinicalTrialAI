"""
performance_analyzer.py

Analyzes runtime execution traces and computes
aggregated performance metrics.
"""

from src.ic04.repositories.performance_repository import PerformanceRepository


class PerformanceAnalyzer:
    """
    Builds performance metrics from RuntimeRepository.
    """

    def __init__(self):
        self.performance_repository = PerformanceRepository()

    def analyze(self, runtime_repository):
        """
        Analyze runtime events captured by RuntimeRepository.
        """

        self.performance_repository.clear()

        events = runtime_repository.get_all_events()

        for event in events:


            if event.event_type != "METHOD_END":
                continue
            # Ignore events that do not contain execution duration
            if event.duration_ms is None:
                continue

            self.performance_repository.add_execution(
                event.method_name,
                event.duration_ms
            )

        return self.performance_repository

    def get_repository(self):
        """
        Return generated repository.
        """
        return self.performance_repository

    def get_total_methods(self):
        return self.performance_repository.get_total_methods()

    def get_total_calls(self):
        return self.performance_repository.get_total_calls()

    def get_slowest_methods(self, top_n=10):
        return self.performance_repository.get_sorted_by_average_time()[:top_n]

    def get_highest_total_time_methods(self, top_n=10):
        return self.performance_repository.get_sorted_by_total_time()[:top_n]

    def get_peak_execution_methods(self, top_n=10):
        return self.performance_repository.get_sorted_by_maximum_time()[:top_n]

    def get_summary(self):

        metrics = self.performance_repository.get_all_metrics()

        total_execution_time = sum(
            metric.total_time
            for metric in metrics
        )

        average_execution_time = (
            total_execution_time / len(metrics)
            if metrics else 0.0
        )

        return {
            "total_methods": self.get_total_methods(),
            "total_calls": self.get_total_calls(),
            "total_execution_time": total_execution_time,
            "average_execution_time": average_execution_time,
        }

    def clear(self):
        self.performance_repository.clear()
