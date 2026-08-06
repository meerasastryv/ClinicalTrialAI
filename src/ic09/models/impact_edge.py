"""
Impact Edge Model

Represents a relationship between two impact nodes.

Author: ClinicalTrialAI
"""

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class ImpactEdge:
    """
    Represents a directed relationship between two nodes.
    """

    source_id: str
    target_id: str
    relationship: str

    confidence: float = 1.0

    weight: float = 1.0

    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert object to dictionary.
        """
        return {
            "source_id": self.source_id,
            "target_id": self.target_id,
            "relationship": self.relationship,
            "confidence": self.confidence,
            "weight": self.weight,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ImpactEdge":
        """
        Create an edge from dictionary.
        """
        return cls(
            source_id=data.get("source_id", ""),
            target_id=data.get("target_id", ""),
            relationship=data.get("relationship", ""),
            confidence=data.get("confidence", 1.0),
            weight=data.get("weight", 1.0),
            metadata=data.get("metadata", {}),
        )
