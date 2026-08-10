"""
IC-08 - Customer Usage Intelligence
Milestone 14 - Satisfaction Prediction Model
"""

from dataclasses import dataclass, field
from typing import List


@dataclass
class SatisfactionPrediction:
    """
    Represents the predicted satisfaction of a customer.
    """

    customer_id: str
    score: float
    confidence: float
    category: str
    contributing_factors: List[str] = field(default_factory=list)

    def add_factor(self, factor: str):
        """Add a contributing factor if not already present."""
        if factor and factor not in self.contributing_factors:
            self.contributing_factors.append(factor)

    def is_highly_satisfied(self) -> bool:
        """Returns True if customer is highly satisfied."""
        return self.score >= 80.0

    def is_at_risk(self) -> bool:
        """Returns True if customer satisfaction is low."""
        return self.score < 60.0

    def __str__(self) -> str:
        lines = [
            f"Customer ID : {self.customer_id}",
            f"Score       : {self.score:.2f}",
            f"Category    : {self.category}",
            f"Confidence  : {self.confidence:.2f}",
            "Contributing Factors:"
        ]

        if self.contributing_factors:
            lines.extend(
                [f"  - {factor}" for factor in self.contributing_factors]
            )
        else:
            lines.append("  None")

        return "\n".join(lines)
