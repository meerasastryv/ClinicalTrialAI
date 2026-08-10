from typing import Dict, List

from src.ic07.models.data_quality_metric import DataQualityMetric
from src.ic07.models.data_quality_issue import DataQualityIssue


class DataQualityRepository:
    """
    Repository for storing data quality metrics and issues.
    """

    def __init__(self):
        self._metrics: Dict[str, DataQualityMetric] = {}
        self._issues: List[DataQualityIssue] = []

    def save_metric(self, metric: DataQualityMetric) -> None:
        """Save or update a quality metric."""
        self._metrics[metric.dataset_name] = metric

    def save_issue(self, issue: DataQualityIssue) -> None:
        """Save a quality issue."""
        self._issues.append(issue)

    def get_metric(self, dataset_name: str) -> DataQualityMetric | None:
        """Retrieve the quality metric for a dataset."""
        return self._metrics.get(dataset_name)

    def get_metrics(self) -> List[DataQualityMetric]:
        """Return all quality metrics."""
        return list(self._metrics.values())

    def get_issues(self, dataset_name: str | None = None) -> List[DataQualityIssue]:
        """
        Return quality issues.
        If dataset_name is provided, return only issues for that dataset.
        """
        if dataset_name is None:
            return list(self._issues)

        return [
            issue
            for issue in self._issues
            if issue.dataset_name == dataset_name
        ]

    def clear(self) -> None:
        """Clear all stored metrics and issues."""
        self._metrics.clear()
        self._issues.clear()
