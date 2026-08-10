"""
Impact Result Model

Represents the complete output of an impact analysis.

Author: ClinicalTrialAI
"""

from dataclasses import dataclass, field
from typing import Dict, Any, List

from src.ic09.models.impact_node import ImpactNode
from src.ic09.models.impact_edge import ImpactEdge


@dataclass
class ImpactResult:
    """
    Complete impact analysis result.
    """

    analysis_id: str

    source_artifact: str

    source_type: str

    impacted_nodes: List[ImpactNode] = field(default_factory=list)

    relationships: List[ImpactEdge] = field(default_factory=list)

    total_impacts: int = 0

    risk_score: float = 0.0

    execution_time: float = 0.0

    metadata: Dict[str, Any] = field(default_factory=dict)

    def add_node(self, node: ImpactNode) -> None:
        """
        Add an impacted node.
        """
        self.impacted_nodes.append(node)
        self.total_impacts = len(self.impacted_nodes)

    def add_relationship(self, edge: ImpactEdge) -> None:
        """
        Add an impact relationship.
        """
        self.relationships.append(edge)

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert the impact result to a dictionary.
        """
        return {
            "analysis_id": self.analysis_id,
            "source_artifact": self.source_artifact,
            "source_type": self.source_type,
            "impacted_nodes": [
                node.to_dict()
                for node in self.impacted_nodes
            ],
            "relationships": [
                edge.to_dict()
                for edge in self.relationships
            ],
            "total_impacts": self.total_impacts,
            "risk_score": self.risk_score,
            "execution_time": self.execution_time,
            "metadata": self.metadata,
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ImpactResult":
        """
        Build object from dictionary.
        """
        result = cls(
            analysis_id=data.get("analysis_id", ""),
            source_artifact=data.get("source_artifact", ""),
            source_type=data.get("source_type", ""),
            total_impacts=data.get("total_impacts", 0),
            risk_score=data.get("risk_score", 0.0),
            execution_time=data.get("execution_time", 0.0),
            metadata=data.get("metadata", {}),
        )

        for node in data.get("impacted_nodes", []):
            result.impacted_nodes.append(
                ImpactNode.from_dict(node)
            )

        for edge in data.get("relationships", []):
            result.relationships.append(
                ImpactEdge.from_dict(edge)
            )

        result.total_impacts = len(result.impacted_nodes)

        return result
