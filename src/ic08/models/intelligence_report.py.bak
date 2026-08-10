from dataclasses import dataclass, field
from datetime import datetime
from typing import Dict, List


@dataclass
class IntelligenceReport:
    report_id: str
    customer_id: str
    organization_name: str

    generated_at: datetime = field(default_factory=datetime.utcnow)

    overall_score: float = 0.0
    risk_level: str = "UNKNOWN"

    metrics: Dict[str, float] = field(default_factory=dict)

    recommendations: List[str] = field(default_factory=list)

    executive_summary: str = ""

    report_format: str = "TEXT"

    def to_dict(self) -> Dict:
        return {
            "report_id": self.report_id,
            "customer_id": self.customer_id,
            "organization_name": self.organization_name,
            "generated_at": self.generated_at.isoformat(),
            "overall_score": self.overall_score,
            "risk_level": self.risk_level,
            "metrics": self.metrics,
            "recommendations": self.recommendations,
            "executive_summary": self.executive_summary,
            "report_format": self.report_format,
        }
