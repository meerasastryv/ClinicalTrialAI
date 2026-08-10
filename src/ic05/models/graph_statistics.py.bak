"""
Graph Statistics Model
IC-05 – Knowledge Graph Engine
Milestone 10
"""

from dataclasses import dataclass, field
from typing import Dict


@dataclass
class GraphStatistics:
    """
    Stores summary statistics for the Knowledge Graph.
    """

    total_nodes: int = 0
    total_edges: int = 0

    node_types: Dict[str, int] = field(default_factory=dict)
    relationship_types: Dict[str, int] = field(default_factory=dict)

    average_degree: float = 0.0
    isolated_nodes: int = 0

    def to_dict(self) -> dict:
        """
        Convert statistics to dictionary.
        """

        return {
            "total_nodes": self.total_nodes,
            "total_edges": self.total_edges,
            "node_types": self.node_types,
            "relationship_types": self.relationship_types,
            "average_degree": self.average_degree,
            "isolated_nodes": self.isolated_nodes,
        }

    def __str__(self) -> str:
        lines = [
            "Graph Statistics",
            "----------------",
            f"Total Nodes        : {self.total_nodes}",
            f"Total Edges        : {self.total_edges}",
            f"Average Degree     : {self.average_degree:.2f}",
            f"Isolated Nodes     : {self.isolated_nodes}",
            "",
            "Node Types",
            "----------",
        ]

        if self.node_types:
            for node_type, count in sorted(self.node_types.items()):
                lines.append(f"{node_type:<25} {count}")
        else:
            lines.append("None")

        lines.extend([
            "",
            "Relationship Types",
            "------------------",
        ])

        if self.relationship_types:
            for rel_type, count in sorted(self.relationship_types.items()):
                lines.append(f"{rel_type:<25} {count}")
        else:
            lines.append("None")

        return "\n".join(lines)
