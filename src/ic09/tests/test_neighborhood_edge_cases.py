from src.ic09.models.impact_edge import ImpactEdge
from src.ic09.models.impact_node import ImpactNode
from src.ic09.repositories.impact_repository import ImpactRepository
from src.ic09.services.neighborhood_analysis_service import (
    NeighborhoodAnalysisService,
)


def create_node(node_id: str) -> ImpactNode:
    return ImpactNode(
        node_id=node_id,
        node_type="Service",
        name=f"Service {node_id}",
    )


def create_edge(source: str, target: str) -> ImpactEdge:
    return ImpactEdge(
        source_id=source,
        target_id=target,
        relationship="DEPENDS_ON",
    )


def test_zero_hop_returns_source_only():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C"]:
        repository.add_node(create_node(node_id))

    repository.add_edge(create_edge("A", "B"))
    repository.add_edge(create_edge("B", "C"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "A",
        direction="downstream",
        max_hops=0,
    )

    assert result.nodes_by_hop == {
        0: ["A"],
    }

    assert result.total_nodes == 1
    assert result.blast_radius == 0


def test_source_only_graph():
    repository = ImpactRepository()

    repository.add_node(create_node("A"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "A",
        max_hops=10,
    )

    assert result.nodes_by_hop == {
        0: ["A"],
    }

    assert result.total_nodes == 1
    assert result.blast_radius == 0
    assert result.max_reached_hop == 0


def test_multiple_paths_do_not_duplicate_nodes():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C", "D"]:
        repository.add_node(create_node(node_id))

    repository.add_edge(create_edge("A", "B"))
    repository.add_edge(create_edge("A", "C"))
    repository.add_edge(create_edge("B", "D"))
    repository.add_edge(create_edge("C", "D"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "A",
        direction="downstream",
        max_hops=3,
    )

    assert set(
        result.get_nodes_at_hop(1)
    ) == {"B", "C"}

    assert result.get_nodes_at_hop(2) == ["D"]

    assert result.total_nodes == 4
    assert result.blast_radius == 3


def test_cycle_with_branching():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C", "D"]:
        repository.add_node(create_node(node_id))

    repository.add_edge(create_edge("A", "B"))
    repository.add_edge(create_edge("B", "C"))
    repository.add_edge(create_edge("C", "A"))
    repository.add_edge(create_edge("B", "D"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "A",
        direction="downstream",
        max_hops=10,
    )

    assert set(
        result.get_nodes_within_hops(10)
    ) == {"A", "B", "C", "D"}

    assert result.blast_radius == 3


def test_disconnected_component_is_not_reached():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C", "X", "Y"]:
        repository.add_node(create_node(node_id))

    repository.add_edge(create_edge("A", "B"))
    repository.add_edge(create_edge("B", "C"))

    repository.add_edge(create_edge("X", "Y"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "A",
        direction="downstream",
        max_hops=10,
    )

    assert set(
        result.get_nodes_within_hops(10)
    ) == {"A", "B", "C"}

    assert "X" not in result.get_nodes_within_hops(10)
    assert "Y" not in result.get_nodes_within_hops(10)


def test_large_hop_count_stops_at_graph_boundary():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C"]:
        repository.add_node(create_node(node_id))

    repository.add_edge(create_edge("A", "B"))
    repository.add_edge(create_edge("B", "C"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "A",
        direction="downstream",
        max_hops=100,
    )

    assert result.max_reached_hop == 2
    assert result.total_nodes == 3
    assert result.blast_radius == 2


def test_direction_is_case_insensitive():
    repository = ImpactRepository()

    for node_id in ["A", "B"]:
        repository.add_node(create_node(node_id))

    repository.add_edge(create_edge("A", "B"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "A",
        direction="DOWNSTREAM",
        max_hops=1,
    )

    assert result.get_nodes_at_hop(1) == ["B"]


def test_upstream_cycle_is_safe():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C"]:
        repository.add_node(create_node(node_id))

    repository.add_edge(create_edge("A", "B"))
    repository.add_edge(create_edge("B", "C"))
    repository.add_edge(create_edge("C", "A"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "C",
        direction="upstream",
        max_hops=10,
    )

    assert set(
        result.get_nodes_within_hops(10)
    ) == {"A", "B", "C"}

    assert result.blast_radius == 2


def test_bidirectional_overlapping_neighborhood_counts_unique_nodes():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C"]:
        repository.add_node(create_node(node_id))

    repository.add_edge(create_edge("A", "B"))
    repository.add_edge(create_edge("B", "C"))
    repository.add_edge(create_edge("C", "A"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze_bidirectional(
        "A",
        max_hops=10,
    )

    assert result.total_unique_nodes == 3
    assert result.combined_blast_radius == 2
