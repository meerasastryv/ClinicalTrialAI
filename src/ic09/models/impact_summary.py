"""
Impact Summary Model

Provides a high-level summary of an impact analysis.

Author: ClinicalTrialAI
"""

from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class ImpactSummary:
    """
    Executive summary of an impact analysis.
    """

    total_nodes: int = 0

    total_relationships: int = 0

    impacted_requirements: int = 0

    impacted_files: int = 0

    impacted_classes: int = 0

    impacted_methods: int = 0

    impacted_apis: int = 0

    impacted_database_objects: int = 0

    impacted_runtime_flows: int = 0

    impacted_test_cases: int = 0

    overall_risk: str = "LOW"

    confidence: float = 0.0

    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert summary to dictionary.
        """
        return {
            "total_nodes": self.total_nodes,
            "total_relationships": self.total_relationships,
            "impacted_requirements": self.impacted_requirements,
            "impacted_files": self.impacted_files,
            "impacted_classes": self.impacted_classes,
            "impacted_methods": self.impacted_methods,
            "impacted_apis": self.impacted_apis,
            "impacted_database_objects": self.impacted_database_objects,
            "impacted_runtime_flows": self.impacted_runtime_flows,
            "impacted_test_cases": self.impacted_test_cases,
            "overall_risk": self.overall_risk,
            "confidence": self.confidence,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ImpactSummary":
        """
        Create summary from dictionary.
        """
        return cls(
            total_nodes=data.get("total_nodes", 0),
            total_relationships=data.get("total_relationships", 0),
            impacted_requirements=data.get("impacted_requirements", 0),
            impacted_files=data.get("impacted_files", 0),
            impacted_classes=data.get("impacted_classes", 0),
            impacted_methods=data.get("impacted_methods", 0),
            impacted_apis=data.get("impacted_apis", 0),
            impacted_database_objects=data.get("impacted_database_objects", 0),
            impacted_runtime_flows=data.get("impacted_runtime_flows", 0),
            impacted_test_cases=data.get("impacted_test_cases", 0),
            overall_risk=data.get("overall_risk", "LOW"),
            confidence=data.get("confidence", 0.0),
            metadata=data.get("metadata", {}),
        )
