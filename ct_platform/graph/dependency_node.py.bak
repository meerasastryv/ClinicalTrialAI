"""
Dependency Graph Node

Represents a node (module/file/class) in the dependency graph.
"""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class DependencyNode:
    """
    Represents a node in the dependency graph.
    """

    id: str
    name: str
    node_type: str = "module"
    path: str = ""

    metadata: Dict = field(default_factory=dict)

    incoming_edges: int = 0
    outgoing_edges: int = 0

    visited: bool = False

    def degree(self) -> int:
        """
        Total degree of the node.
        """
        return self.incoming_edges + self.outgoing_edges

    def reset(self):
        """
        Reset traversal state.
        """
        self.visited = False

    def increment_incoming(self):
        self.incoming_edges += 1

    def increment_outgoing(self):
        self.outgoing_edges += 1

    def __hash__(self):
        return hash(self.id)

    def __str__(self):
        return self.name
