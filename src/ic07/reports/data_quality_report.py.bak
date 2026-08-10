from src.ic07.models.data_quality_metric import DataQualityMetric
from src.ic07.repositories.data_quality_repository import DataQualityRepository


class DataQualityReport:

    def __init__(self, repository: DataQualityRepository):
        self.repository = repository

    def generate(self, dataset_name: str) -> None:
        """
        Generate a data quality report for a dataset.
        """

        metric = self.repository.get_metric(dataset_name)

        if metric is None:
            print(f"No quality metrics found for dataset: {dataset_name}")
            return

        issues = self.repository.get_issues(dataset_name)

        print("\n" + "=" * 60)
        print("DATA QUALITY REPORT")
        print("=" * 60)

        print(f"Dataset           : {metric.dataset_name}")
        print(f"Status            : {metric.status}")
        print(f"Overall Score     : {metric.overall_score:.2f}%")
        print(f"Total Records     : {metric.total_records}")
        print(f"Failed Records    : {metric.failed_records}")

        print("\nQuality Dimensions")
        print("-" * 60)
        print(f"Completeness      : {metric.completeness_score:.2f}%")
        print(f"Validity          : {metric.validity_score:.2f}%")
        print(f"Consistency       : {metric.consistency_score:.2f}%")
        print(f"Uniqueness        : {metric.uniqueness_score:.2f}%")
        print(f"Accuracy          : {metric.accuracy_score:.2f}%")
        print(f"Timeliness        : {metric.timeliness_score:.2f}%")

        print("\nIssues")
        print("-" * 60)

        if not issues:
            print("No data quality issues found.")
        else:
            for issue in issues:
                print(
                    f"[{issue.severity}] "
                    f"Row {issue.row_number}, "
                    f"{issue.column_name} -> "
                    f"{issue.issue_type}"
                )

        print("\nEvaluation Time")
        print("-" * 60)
        print(metric.evaluated_at.strftime("%Y-%m-%d %H:%M:%S"))

        print("=" * 60)
