"""
Bidirectional Neighborhood Analysis Result Model

Represents upstream and downstream neighborhoods
around a source node.

Author: ClinicalTrialAI
"""

from dataclasses import dataclass

from src.ic09.models.neighborhood_result import NeighborhoodResult


@dataclass
class BidirectionalNeighborhoodResult:
    """
    Represents both upstream and downstream neighborhoods
    surrounding a source node.
    """

    source_node: str
    upstream: NeighborhoodResult
    downstream: NeighborhoodResult





    @property
    def upstream_blast_radius(self) -> int:
        """
        Return the upstream blast radius excluding
        the source node.
        """
        return self.upstream.blast_radius

    @property
    def downstream_blast_radius(self) -> int:
        """
        Return the downstream blast radius excluding
        the source node.
        """
        return self.downstream.blast_radius

    @property
    def combined_blast_radius(self) -> int:
        """
        Return the number of unique impacted nodes across
        upstream and downstream neighborhoods, excluding
        the source node.
        """
        return max(
            self.total_unique_nodes - 1,
            0,
        )



    @property
    def upstream_node_count(self) -> int:
        """
        Return the number of nodes in the upstream neighborhood.
        """
        return self.upstream.total_nodes

    @property
    def downstream_node_count(self) -> int:
        """
        Return the number of nodes in the downstream neighborhood.
        """
        return self.downstream.total_nodes

    @property
    def total_unique_nodes(self) -> int:
        """
        Return the total number of unique nodes across both
        neighborhoods.

        The source node is counted only once.
        """
        upstream_nodes = set(
            self.upstream.get_nodes_within_hops(
                self.upstream.max_hops
            )
        )

        downstream_nodes = set(
            self.downstream.get_nodes_within_hops(
                self.downstream.max_hops
            )
        )

        return len(
            upstream_nodes | downstream_nodes
        )

    @property
    def upstream_only_nodes(self) -> set[str]:
        """
        Return nodes found only in the upstream neighborhood.
        """
        upstream_nodes = set(
            self.upstream.get_nodes_within_hops(
                self.upstream.max_hops
            )
        )

        downstream_nodes = set(
            self.downstream.get_nodes_within_hops(
                self.downstream.max_hops
            )
        )

        return upstream_nodes - downstream_nodes

    @property
    def downstream_only_nodes(self) -> set[str]:
        """
        Return nodes found only in the downstream neighborhood.
        """
        upstream_nodes = set(
            self.upstream.get_nodes_within_hops(
                self.upstream.max_hops
            )
        )

        downstream_nodes = set(
            self.downstream.get_nodes_within_hops(
                self.downstream.max_hops
            )
        )

        return downstream_nodes - upstream_nodes

    @property
    def common_nodes(self) -> set[str]:
        """
        Return nodes present in both neighborhoods.
        """
        upstream_nodes = set(
            self.upstream.get_nodes_within_hops(
                self.upstream.max_hops
            )
        )

        downstream_nodes = set(
            self.downstream.get_nodes_within_hops(
                self.downstream.max_hops
            )
        )

        return upstream_nodes & downstream_nodes

    def to_dict(self) -> dict:
        """
        Convert the result into a serializable dictionary.
        """
        return {
            "source_node": self.source_node,
            "upstream": self.upstream.to_dict(),
            "downstream": self.downstream.to_dict(),
            "upstream_node_count": self.upstream_node_count,
            "downstream_node_count": self.downstream_node_count,
            "total_unique_nodes": self.total_unique_nodes,
            "upstream_only_nodes": sorted(
                self.upstream_only_nodes
            ),
            "downstream_only_nodes": sorted(
                self.downstream_only_nodes
            ),
            "common_nodes": sorted(
                self.common_nodes
            ),


            "upstream_blast_radius": (
                self.upstream_blast_radius
            ),
            "downstream_blast_radius": (
                self.downstream_blast_radius
            ),
            "combined_blast_radius": (
                self.combined_blast_radius
            ),

        }
