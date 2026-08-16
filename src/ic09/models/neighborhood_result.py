"""
Neighborhood Analysis Result Model

Represents the result of N-Hop / Neighborhood Analysis
within the Impact Analysis Engine.

Author: ClinicalTrialAI
"""

from dataclasses import dataclass, field
from typing import Dict, List


@dataclass
class NeighborhoodResult:
    """
    Represents nodes surrounding a source node, grouped
    by their shortest-hop distance from the source.
    """

    source_node: str
    direction: str
    max_hops: int

    nodes_by_hop: Dict[int, List[str]] = field(
        default_factory=dict
    )

    @property
    def total_nodes(self) -> int:
        """
        Return the total number of unique nodes in the
        neighborhood, including the source node.
        """
        return sum(
            len(nodes)
            for nodes in self.nodes_by_hop.values()
        )

    @property
    def max_reached_hop(self) -> int:
        """
        Return the greatest hop level actually reached.
        """
        if not self.nodes_by_hop:
            return 0

        return max(self.nodes_by_hop.keys())

    @property
    def nodes_per_hop(self) -> Dict[int, int]:
        """
        Return the number of nodes at each hop level.
        """
        return {
            hop: len(nodes)
            for hop, nodes in self.nodes_by_hop.items()
        }

    @property
    def blast_radius(self) -> int:
        """
        Return the number of impacted nodes excluding
        the source node.
        """
        return max(
            self.total_nodes - 1,
            0,
        )

    @property
    def average_nodes_per_hop(self) -> float:
        """
        Return the average number of nodes per non-source
        hop level.
        """
        non_source_counts = [
            len(nodes)
            for hop, nodes in self.nodes_by_hop.items()
            if hop > 0
        ]

        if not non_source_counts:
            return 0.0

        return sum(
            non_source_counts
        ) / len(non_source_counts)



    def get_nodes_at_hop(self, hop: int) -> List[str]:
        """
        Return nodes located at an exact hop distance.
        """
        return self.nodes_by_hop.get(hop, [])

    def get_nodes_within_hops(self, hops: int) -> List[str]:
        """
        Return all nodes within the specified number of hops.

        The result is ordered by hop level.
        """
        if hops < 0:
            raise ValueError(
                "hops must be non-negative"
            )

        nodes: List[str] = []

        for level in sorted(self.nodes_by_hop.keys()):
            if level > hops:
                break

            nodes.extend(self.nodes_by_hop[level])

        return nodes



    def to_dict(self) -> dict:
        """
        Convert the result into a serializable dictionary.
        """
        return {
            "source_node": self.source_node,
            "direction": self.direction,
            "max_hops": self.max_hops,
            "nodes_by_hop": self.nodes_by_hop,
            "nodes_per_hop": self.nodes_per_hop,
            "total_nodes": self.total_nodes,
            "blast_radius": self.blast_radius,
            "max_reached_hop": self.max_reached_hop,
            "average_nodes_per_hop": (
                self.average_nodes_per_hop
            ),
        }



