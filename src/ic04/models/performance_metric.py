"""
performance_metric.py

Performance metric model used by the Runtime Exploration Agent.
Stores aggregated execution statistics for a single method.
"""

from dataclasses import dataclass


@dataclass
class PerformanceMetric:
    """
    Stores performance statistics for a single method.
    """

    method_name: str

    call_count: int = 0

    total_time: float = 0.0

    average_time: float = 0.0

    minimum_time: float = float("inf")

    maximum_time: float = 0.0

    def update(self, execution_time: float):
        """
        Update performance statistics with a new execution time.
        """

        self.call_count += 1
        self.total_time += execution_time

        if execution_time < self.minimum_time:
            self.minimum_time = execution_time

        if execution_time > self.maximum_time:
            self.maximum_time = execution_time

        self.average_time = self.total_time / self.call_count

    @property
    def min_time(self):
        """
        Returns 0 if no executions have occurred.
        """
        if self.call_count == 0:
            return 0.0
        return self.minimum_time

    @property
    def max_time(self):
        return self.maximum_time

    @property
    def avg_time(self):
        return self.average_time

    def to_dict(self):
        """
        Convert metric to dictionary representation.
        """
        return {
            "method_name": self.method_name,
            "call_count": self.call_count,
            "total_time": round(self.total_time, 6),
            "average_time": round(self.average_time, 6),
            "minimum_time": round(self.min_time, 6),
            "maximum_time": round(self.maximum_time, 6),
        }

    def __str__(self):
        return (
            f"{self.method_name} | "
            f"Calls={self.call_count} | "
            f"Avg={self.average_time:.6f}s | "
            f"Min={self.min_time:.6f}s | "
            f"Max={self.maximum_time:.6f}s | "
            f"Total={self.total_time:.6f}s"
        )
