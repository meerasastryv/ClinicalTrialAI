from dataclasses import dataclass


@dataclass
class DataQualityIssue:
    dataset_name: str
    row_number: int
    column_name: str

    issue_type: str
    severity: str

    expected_value: str
    actual_value: str

    suggestion: str
