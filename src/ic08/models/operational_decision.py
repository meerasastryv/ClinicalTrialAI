from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class OperationalDecision:
    decision_id: str
    customer_id: str
    organization_name: str

    generated_at: datetime = field(default_factory=datetime.utcnow)

    overall_score: float = 0.0

    risk_level: str = "UNKNOWN"

    decision_status: str = "REVIEW"

    executive_summary: str = ""

    recommended_actions: List[str] = field(default_factory=list)

    expected_outcome: str = ""

    owner: str = "Operations Team"

    def __str__(self):

        lines = [
            f"Decision ID      : {self.decision_id}",
            f"Customer         : {self.organization_name}",
            f"Overall Score    : {self.overall_score:.2f}",
            f"Risk Level       : {self.risk_level}",
            f"Decision Status  : {self.decision_status}",
            "",
            "Recommended Actions:"
        ]

        for action in self.recommended_actions:
            lines.append(f" - {action}")

        lines.append("")
        lines.append("Executive Summary:")
        lines.append(self.executive_summary)

        lines.append("")
        lines.append(f"Expected Outcome : {self.expected_outcome}")

        return "\n".join(lines)
