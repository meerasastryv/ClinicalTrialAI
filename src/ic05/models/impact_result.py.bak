"""
Impact Result Model
IC-05 – Knowledge Graph Engine
Milestone 11
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class ImpactResult:
    """
    Represents the result of an impact analysis.
    """

    source_node: str

    impacted_nodes: List[str] = field(default_factory=list)

    direct_dependencies: List[str] = field(default_factory=list)

    indirect_dependencies: List[str] = field(default_factory=list)

    impacted_requirements: List[str] = field(default_factory=list)

    impacted_classes: List[str] = field(default_factory=list)

    impacted_methods: List[str] = field(default_factory=list)

    impacted_apis: List[str] = field(default_factory=list)

    impacted_databases: List[str] = field(default_factory=list)

    dependency_depth: int = 0

    impact_score: float = 0.0

    blast_radius: str = "LOW"

    metadata: Dict[str, str] = field(default_factory=dict)

    # ---------------------------------------------------------

    @property
    def total_impacted_nodes(self) -> int:
        """
        Returns the total number of impacted nodes.
        """
        return len(self.impacted_nodes)

    # ---------------------------------------------------------

    def to_dict(self) -> dict:
        """
        Convert to dictionary.
        """
        return {
            "source_node": self.source_node,
            "impacted_nodes": self.impacted_nodes,
            "direct_dependencies": self.direct_dependencies,
            "indirect_dependencies": self.indirect_dependencies,
            "impacted_requirements": self.impacted_requirements,
            "impacted_classes": self.impacted_classes,
            "impacted_methods": self.impacted_methods,
            "impacted_apis": self.impacted_apis,
            "impacted_databases": self.impacted_databases,
            "dependency_depth": self.dependency_depth,
            "impact_score": self.impact_score,
            "blast_radius": self.blast_radius,
            "metadata": self.metadata,
        }

    # ---------------------------------------------------------

    def __str__(self) -> str:
        lines = [
            "Impact Analysis Result",
            "----------------------",
            f"Source Node           : {self.source_node}",
            f"Total Impacted Nodes  : {self.total_impacted_nodes}",
            f"Dependency Depth      : {self.dependency_depth}",
            f"Impact Score          : {self.impact_score:.2f}",
            f"Blast Radius          : {self.blast_radius}",
            "",
            f"Requirements          : {len(self.impacted_requirements)}",
            f"Classes               : {len(self.impacted_classes)}",
            f"Methods               : {len(self.impacted_methods)}",
            f"APIs                  : {len(self.impacted_apis)}",
            f"Databases             : {len(self.impacted_databases)}",
        ]

        return "\n".join(lines)
