from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class DataQualityMetric:
    dataset_name: str

    completeness_score: float = 0.0
    validity_score: float = 0.0
    consistency_score: float = 0.0
    uniqueness_score: float = 0.0
    accuracy_score: float = 0.0
    timeliness_score: float = 0.0

    overall_score: float = 0.0

    total_records: int = 0
    failed_records: int = 0

    status: str = "Unknown"

    evaluated_at: datetime = field(default_factory=datetime.now)
