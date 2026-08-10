"""
Impact Node Model

Represents a single impacted artifact within the platform.

Author: ClinicalTrialAI
"""

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class ImpactNode:
    """
    Represents one node in the impact graph.
    """

    node_id: str
    node_type: str
    name: str

    description: str = ""

    severity: str = "LOW"

    confidence: float = 0.0

    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert object to dictionary.
        """
        return {
            "node_id": self.node_id,
            "node_type": self.node_type,
            "name": self.name,
            "description": self.description,
            "severity": self.severity,
            "confidence": self.confidence,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ImpactNode":
        """
        Build object from dictionary.
        """
        return cls(
            node_id=data.get("node_id", ""),
            node_type=data.get("node_type", ""),
            name=data.get("name", ""),
            description=data.get("description", ""),
            severity=data.get("severity", "LOW"),
            confidence=data.get("confidence", 0.0),
            metadata=data.get("metadata", {}),
        )
