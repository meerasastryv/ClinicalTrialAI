"""
Risk Score Model

Represents the calculated risk associated with an impact analysis.

Author: ClinicalTrialAI
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List


@dataclass
class RiskScore:
    """
    Represents the calculated risk for an impact analysis.
    """

    score: float = 0.0

    level: str = "LOW"

    confidence: float = 0.0

    impacted_components: int = 0

    impacted_tests: int = 0

    impacted_dependencies: int = 0

    impacted_runtime_paths: int = 0

    factors: List[str] = field(default_factory=list)

    recommendation: str = ""

    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert object to dictionary.
        """
        return {
            "score": self.score,
            "level": self.level,
            "confidence": self.confidence,
            "impacted_components": self.impacted_components,
            "impacted_tests": self.impacted_tests,
            "impacted_dependencies": self.impacted_dependencies,
            "impacted_runtime_paths": self.impacted_runtime_paths,
            "factors": self.factors,
            "recommendation": self.recommendation,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "RiskScore":
        """
        Build object from dictionary.
        """
        return cls(
            score=data.get("score", 0.0),
            level=data.get("level", "LOW"),
            confidence=data.get("confidence", 0.0),
            impacted_components=data.get("impacted_components", 0),
            impacted_tests=data.get("impacted_tests", 0),
            impacted_dependencies=data.get("impacted_dependencies", 0),
            impacted_runtime_paths=data.get("impacted_runtime_paths", 0),
            factors=data.get("factors", []),
            recommendation=data.get("recommendation", ""),
            metadata=data.get("metadata", {}),
        )
