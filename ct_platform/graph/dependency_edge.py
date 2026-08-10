"""
Dependency Graph Edge

Represents a dependency relationship between two nodes.
"""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class DependencyEdge:
    """
    Represents a directed edge in the dependency graph.
    """

    source: str
    target: str

    dependency_type: str = "import"
    weight: int = 1

    metadata: Dict = field(default_factory=dict)

    bidirectional: bool = False

    def __hash__(self):
        return hash(
            (
                self.source,
                self.target,
                self.dependency_type,
            )
        )

    def __str__(self):
        return (
            f"{self.source}"
            f" -> "
            f"{self.target}"
        )
