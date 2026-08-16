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


def test_bidirectional_neighborhood():
    repository = ImpactRepository()

    for node_id in [
        "UP2",
        "UP1",
        "A",
        "DOWN1",
        "DOWN2",
    ]:
        repository.add_node(
            create_node(node_id)
        )

    repository.add_edge(
        create_edge("UP2", "UP1")
    )

    repository.add_edge(
        create_edge("UP1", "A")
    )

    repository.add_edge(
        create_edge("A", "DOWN1")
    )

    repository.add_edge(
        create_edge("DOWN1", "DOWN2")
    )

    service = NeighborhoodAnalysisService(
        repository
    )

    result = service.analyze_bidirectional(
        "A",
        max_hops=2,
    )

    assert result.source_node == "A"

    assert result.upstream.get_nodes_at_hop(0) == ["A"]
    assert result.upstream.get_nodes_at_hop(1) == ["UP1"]
    assert result.upstream.get_nodes_at_hop(2) == ["UP2"]

    assert result.downstream.get_nodes_at_hop(0) == ["A"]
    assert result.downstream.get_nodes_at_hop(1) == ["DOWN1"]
    assert result.downstream.get_nodes_at_hop(2) == ["DOWN2"]


def test_bidirectional_node_counts():
    repository = ImpactRepository()

    for node_id in [
        "UP1",
        "A",
        "DOWN1",
        "DOWN2",
    ]:
        repository.add_node(
            create_node(node_id)
        )

    repository.add_edge(
        create_edge("UP1", "A")
    )

    repository.add_edge(
        create_edge("A", "DOWN1")
    )

    repository.add_edge(
        create_edge("DOWN1", "DOWN2")
    )

    service = NeighborhoodAnalysisService(
        repository
    )

    result = service.analyze_bidirectional(
        "A",
        max_hops=2,
    )

    assert result.upstream_node_count == 2
    assert result.downstream_node_count == 3


def test_bidirectional_unique_node_count():
    repository = ImpactRepository()

    for node_id in [
        "UP1",
        "A",
        "DOWN1",
    ]:
        repository.add_node(
            create_node(node_id)
        )

    repository.add_edge(
        create_edge("UP1", "A")
    )

    repository.add_edge(
        create_edge("A", "DOWN1")
    )

    service = NeighborhoodAnalysisService(
        repository
    )

    result = service.analyze_bidirectional(
        "A",
        max_hops=2,
    )

    # A appears in both directions but is counted once.
    assert result.total_unique_nodes == 3


def test_bidirectional_unknown_source():
    repository = ImpactRepository()

    service = NeighborhoodAnalysisService(
        repository
    )

    result = service.analyze_bidirectional(
        "UNKNOWN",
        max_hops=2,
    )

    assert result.source_node == "UNKNOWN"
    assert result.upstream.nodes_by_hop == {}
    assert result.downstream.nodes_by_hop == {}
    assert result.total_unique_nodes == 0


def test_bidirectional_negative_hops_rejected():
    repository = ImpactRepository()

    service = NeighborhoodAnalysisService(
        repository
    )

    try:
        service.analyze_bidirectional(
            "A",
            max_hops=-1,
        )
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert str(exc) == (
            "max_hops must be non-negative"
        )


def test_bidirectional_blast_radius():
    repository = ImpactRepository()

    for node_id in [
        "UP2",
        "UP1",
        "A",
        "DOWN1",
        "DOWN2",
    ]:
        repository.add_node(
            create_node(node_id)
        )

    repository.add_edge(
        create_edge("UP2", "UP1")
    )

    repository.add_edge(
        create_edge("UP1", "A")
    )

    repository.add_edge(
        create_edge("A", "DOWN1")
    )

    repository.add_edge(
        create_edge("DOWN1", "DOWN2")
    )

    service = NeighborhoodAnalysisService(
        repository
    )

    result = service.analyze_bidirectional(
        "A",
        max_hops=2,
    )

    assert result.upstream_blast_radius == 2
    assert result.downstream_blast_radius == 2
    assert result.combined_blast_radius == 4
