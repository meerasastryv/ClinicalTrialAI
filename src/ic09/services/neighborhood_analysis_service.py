"""
Neighborhood Analysis Service

Provides N-Hop neighborhood analysis over the IC-09 impact graph.

Author: ClinicalTrialAI
"""
from src.ic09.models.bidirectional_neighborhood_result import (
    BidirectionalNeighborhoodResult,
)
from collections import deque
from typing import Dict, List, Set

from src.ic09.models.neighborhood_result import NeighborhoodResult
from src.ic09.repositories.impact_repository import ImpactRepository


class NeighborhoodAnalysisService:
    """
    Performs breadth-first N-Hop neighborhood analysis
    over the IC-09 impact repository.
    """

    def __init__(self, repository: ImpactRepository) -> None:
        """
        Initialize the neighborhood analysis service.
        """
        self._repository = repository

    def analyze(
        self,
        source_id: str,
        direction: str = "downstream",
        max_hops: int = 1,
    ) -> NeighborhoodResult:
        """
        Analyze the neighborhood surrounding a source node.

        Parameters
        ----------
        source_id:
            Identifier of the starting node.

        direction:
            Traversal direction.

            Supported values:
            - downstream
            - upstream

        max_hops:
            Maximum number of hops to traverse.

            Hop 0 represents the source node itself.

        Returns
        -------
        NeighborhoodResult
            Nodes grouped by their shortest hop distance
            from the source node.

        Raises
        ------
        ValueError
            If max_hops is negative or direction is unsupported.
        """

        if max_hops < 0:
            raise ValueError(
                "max_hops must be non-negative"
            )

        direction = direction.lower()

        if direction not in {"downstream", "upstream"}:
            raise ValueError(
                f"Unsupported neighborhood direction: {direction}"
            )

        # Unknown source node
        if self._repository.get_node(source_id) is None:
            return NeighborhoodResult(
                source_node=source_id,
                direction=direction,
                max_hops=max_hops,
                nodes_by_hop={},
            )

        visited: Set[str] = {source_id}

        queue = deque(
            [(source_id, 0)]
        )

        nodes_by_hop: Dict[int, List[str]] = {
            0: [source_id]
        }

        while queue:
            current_id, current_hop = queue.popleft()

            if current_hop >= max_hops:
                continue

            next_hop = current_hop + 1

            if direction == "downstream":
                edges = self._repository.get_outgoing_edges(
                    current_id
                )
                neighbor_ids = [
                    edge.target_id
                    for edge in edges
                ]
            else:
                edges = self._repository.get_incoming_edges(
                    current_id
                )
                neighbor_ids = [
                    edge.source_id
                    for edge in edges
                ]

            for neighbor_id in neighbor_ids:

                if neighbor_id in visited:
                    continue

                # Ignore relationships pointing to nodes that
                # are not registered in the repository.
                if self._repository.get_node(
                    neighbor_id
                ) is None:
                    continue

                visited.add(neighbor_id)

                nodes_by_hop.setdefault(
                    next_hop,
                    []
                ).append(neighbor_id)

                queue.append(
                    (
                        neighbor_id,
                        next_hop,
                    )
                )

        return NeighborhoodResult(
            source_node=source_id,
            direction=direction,
            max_hops=max_hops,
            nodes_by_hop=nodes_by_hop,
        )


    def analyze_bidirectional(
        self,
        source_id: str,
        max_hops: int = 1,
    ) -> BidirectionalNeighborhoodResult:
        """
        Analyze both upstream and downstream neighborhoods
        surrounding a source node.

        Parameters
        ----------
        source_id:
            Identifier of the starting node.

        max_hops:
            Maximum number of hops in each direction.

        Returns
        -------
        BidirectionalNeighborhoodResult
            Separate upstream and downstream neighborhood
            results.
        """

        if max_hops < 0:
            raise ValueError(
                "max_hops must be non-negative"
            )

        upstream_result = self.analyze(
            source_id=source_id,
            direction="upstream",
            max_hops=max_hops,
        )

        downstream_result = self.analyze(
            source_id=source_id,
            direction="downstream",
            max_hops=max_hops,
        )

        return BidirectionalNeighborhoodResult(
            source_node=source_id,
            upstream=upstream_result,
            downstream=downstream_result,
        )
