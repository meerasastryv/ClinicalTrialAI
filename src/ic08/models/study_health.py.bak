"""
IC-08 - Platform Usage Intelligence
Milestone 16 - Study Health Index Model
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class StudyHealth:
    """
    Represents the overall health of a clinical study based on
    platform usage, productivity, workflow completion, metadata
    reuse and deliverable readiness.
    """

    study_id: str
    health_score: float
    status: str
    risk_level: str
    confidence: float
    indicators: List[str] = field(default_factory=list)

    def add_indicator(self, indicator: str):
        """
        Add a health indicator.
        """
        if indicator and indicator not in self.indicators:
            self.indicators.append(indicator)

    def is_healthy(self) -> bool:
        """
        Returns True if study health is good.
        """
        return self.health_score >= 80.0

    def needs_attention(self) -> bool:
        """
        Returns True if study requires attention.
        """
        return self.health_score < 60.0

    def __str__(self) -> str:

        lines = [
            f"Study ID      : {self.study_id}",
            f"Health Score  : {self.health_score:.2f}",
            f"Status        : {self.status}",
            f"Risk Level    : {self.risk_level}",
            f"Confidence    : {self.confidence:.2f}",
            "Indicators:"
        ]

        if self.indicators:

            for indicator in self.indicators:
                lines.append(f"  - {indicator}")

        else:
            lines.append("  None")

        return "\n".join(lines)
