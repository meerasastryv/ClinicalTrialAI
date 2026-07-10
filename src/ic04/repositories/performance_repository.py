"""
performance_repository.py

Repository for storing and managing performance metrics
generated from runtime execution traces.
"""

from typing import Dict, List, Optional

from src.ic04.models.performance_metric import PerformanceMetric


class PerformanceRepository:
    """
    Repository that stores aggregated performance metrics
    for all observed methods.
    """

    def __init__(self):
        self._metrics: Dict[str, PerformanceMetric] = {}

    def add_execution(self, method_name: str, execution_time: float):
        """
        Add an execution record for a method.
        """

        if method_name not in self._metrics:
            self._metrics[method_name] = PerformanceMetric(method_name)

        self._metrics[method_name].update(execution_time)

    def get_metric(self, method_name: str) -> Optional[PerformanceMetric]:
        """
        Retrieve metric for a specific method.
        """

        return self._metrics.get(method_name)

    def get_all_metrics(self) -> List[PerformanceMetric]:
        """
        Return all performance metrics.
        """

        return list(self._metrics.values())

    def get_sorted_by_average_time(
        self,
        descending: bool = True
    ) -> List[PerformanceMetric]:
        """
        Return metrics sorted by average execution time.
        """

        return sorted(
            self._metrics.values(),
            key=lambda metric: metric.average_time,
            reverse=descending,
        )

    def get_sorted_by_total_time(
        self,
        descending: bool = True
    ) -> List[PerformanceMetric]:
        """
        Return metrics sorted by total execution time.
        """

        return sorted(
            self._metrics.values(),
            key=lambda metric: metric.total_time,
            reverse=descending,
        )

    def get_sorted_by_maximum_time(
        self,
        descending: bool = True
    ) -> List[PerformanceMetric]:
        """
        Return metrics sorted by maximum execution time.
        """

        return sorted(
            self._metrics.values(),
            key=lambda metric: metric.maximum_time,
            reverse=descending,
        )

    def get_total_methods(self) -> int:
        """
        Return the number of methods tracked.
        """

        return len(self._metrics)

    def get_total_calls(self) -> int:
        """
        Return the total number of recorded executions.
        """

        return sum(metric.call_count for metric in self._metrics.values())

    def clear(self):
        """
        Clear all stored metrics.
        """

        self._metrics.clear()

    def to_dict(self):
        """
        Convert repository contents to a dictionary.
        """

        return {
            metric.method_name: metric.to_dict()
            for metric in self._metrics.values()
        }

    def __len__(self):
        return len(self._metrics)

    def __iter__(self):
        return iter(self._metrics.values())

    def __contains__(self, method_name: str):
        return method_name in self._metrics

    def __str__(self):
        return (
            f"PerformanceRepository("
            f"methods={self.get_total_methods()}, "
            f"calls={self.get_total_calls()})"
        )
