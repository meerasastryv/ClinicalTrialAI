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


def test_downstream_n_hop_neighborhood():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C", "D", "E", "F"]:
        repository.add_node(create_node(node_id))

    repository.add_edge(create_edge("A", "B"))
    repository.add_edge(create_edge("A", "C"))
    repository.add_edge(create_edge("B", "D"))
    repository.add_edge(create_edge("B", "E"))
    repository.add_edge(create_edge("C", "F"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "A",
        direction="downstream",
        max_hops=2,
    )

    assert result.source_node == "A"
    assert result.direction == "downstream"

    assert result.get_nodes_at_hop(0) == ["A"]

    assert set(
        result.get_nodes_at_hop(1)
    ) == {"B", "C"}

    assert set(
        result.get_nodes_at_hop(2)
    ) == {"D", "E", "F"}

    assert result.total_nodes == 6
    assert result.max_reached_hop == 2


def test_downstream_neighborhood_respects_max_hops():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C", "D"]:
        repository.add_node(create_node(node_id))

    repository.add_edge(create_edge("A", "B"))
    repository.add_edge(create_edge("B", "C"))
    repository.add_edge(create_edge("C", "D"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "A",
        direction="downstream",
        max_hops=2,
    )

    assert set(
        result.get_nodes_within_hops(2)
    ) == {"A", "B", "C"}

    assert result.get_nodes_at_hop(3) == []


def test_upstream_n_hop_neighborhood():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C", "D"]:
        repository.add_node(create_node(node_id))

    repository.add_edge(create_edge("A", "B"))
    repository.add_edge(create_edge("B", "C"))
    repository.add_edge(create_edge("C", "D"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "D",
        direction="upstream",
        max_hops=2,
    )

    assert result.get_nodes_at_hop(0) == ["D"]

    assert result.get_nodes_at_hop(1) == ["C"]

    assert result.get_nodes_at_hop(2) == ["B"]

    assert result.total_nodes == 3


def test_n_hop_handles_cycles():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C"]:
        repository.add_node(create_node(node_id))

    repository.add_edge(create_edge("A", "B"))
    repository.add_edge(create_edge("B", "C"))
    repository.add_edge(create_edge("C", "A"))

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "A",
        direction="downstream",
        max_hops=10,
    )

    assert set(
        result.get_nodes_within_hops(10)
    ) == {"A", "B", "C"}

    assert result.total_nodes == 3


def test_unknown_source_returns_empty_neighborhood():
    repository = ImpactRepository()

    service = NeighborhoodAnalysisService(repository)

    result = service.analyze(
        "UNKNOWN",
        max_hops=3,
    )

    assert result.nodes_by_hop == {}
    assert result.total_nodes == 0


def test_negative_max_hops_is_rejected():
    repository = ImpactRepository()

    service = NeighborhoodAnalysisService(repository)

    try:
        service.analyze(
            "A",
            max_hops=-1,
        )
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert str(exc) == "max_hops must be non-negative"


def test_invalid_direction_is_rejected():
    repository = ImpactRepository()

    service = NeighborhoodAnalysisService(repository)

    try:
        service.analyze(
            "A",
            direction="sideways",
            max_hops=2,
        )
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert str(exc) == (
            "Unsupported neighborhood direction: sideways"
        )
