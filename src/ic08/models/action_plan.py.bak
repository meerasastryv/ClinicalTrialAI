from dataclasses import dataclass, field
from datetime import datetime
from typing import List


@dataclass
class ActionPlan:
    action_plan_id: str
    customer_id: str
    organization_name: str

    generated_at: datetime = field(default_factory=datetime.utcnow)

    overall_score: float = 0.0
    risk_level: str = "UNKNOWN"

    priority: str = "MEDIUM"

    actions: List[str] = field(default_factory=list)

    expected_outcome: str = ""

    owner: str = "Operations Team"

    status: str = "OPEN"

    def __str__(self):

        lines = [
            f"Action Plan ID : {self.action_plan_id}",
            f"Customer       : {self.organization_name}",
            f"Priority       : {self.priority}",
            f"Risk Level     : {self.risk_level}",
            f"Status         : {self.status}",
            "",
            "Actions:"
        ]

        for action in self.actions:
            lines.append(f" - {action}")

        lines.append("")
        lines.append(f"Expected Outcome : {self.expected_outcome}")

        return "\n".join(lines)
