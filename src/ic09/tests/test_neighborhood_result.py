from src.ic09.models.neighborhood_result import NeighborhoodResult


def test_neighborhood_result_basic_properties():
    result = NeighborhoodResult(
        source_node="A",
        direction="downstream",
        max_hops=3,
        nodes_by_hop={
            0: ["A"],
            1: ["B", "C"],
            2: ["D", "E", "F"],
            3: ["G"],
        },
    )

    assert result.source_node == "A"
    assert result.direction == "downstream"
    assert result.max_hops == 3

    assert result.get_nodes_at_hop(0) == ["A"]
    assert result.get_nodes_at_hop(1) == ["B", "C"]
    assert result.get_nodes_at_hop(2) == ["D", "E", "F"]
    assert result.get_nodes_at_hop(3) == ["G"]

    assert result.total_nodes == 7
    assert result.max_reached_hop == 3


def test_get_nodes_within_hops():
    result = NeighborhoodResult(
        source_node="A",
        direction="downstream",
        max_hops=3,
        nodes_by_hop={
            0: ["A"],
            1: ["B", "C"],
            2: ["D", "E", "F"],
            3: ["G"],
        },
    )

    assert result.get_nodes_within_hops(0) == ["A"]

    assert result.get_nodes_within_hops(1) == [
        "A",
        "B",
        "C",
    ]

    assert result.get_nodes_within_hops(2) == [
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
    ]


def test_get_nodes_at_unknown_hop():
    result = NeighborhoodResult(
        source_node="A",
        direction="downstream",
        max_hops=2,
        nodes_by_hop={
            0: ["A"],
            1: ["B"],
            2: ["C"],
        },
    )

    assert result.get_nodes_at_hop(5) == []


def test_get_nodes_within_hops_rejects_negative_hops():
    result = NeighborhoodResult(
        source_node="A",
        direction="downstream",
        max_hops=2,
        nodes_by_hop={
            0: ["A"],
            1: ["B"],
        },
    )

    try:
        result.get_nodes_within_hops(-1)
        assert False, "Expected ValueError"
    except ValueError as exc:
        assert str(exc) == "hops must be non-negative"



def test_nodes_per_hop():
    result = NeighborhoodResult(
        source_node="A",
        direction="downstream",
        max_hops=3,
        nodes_by_hop={
            0: ["A"],
            1: ["B", "C"],
            2: ["D", "E", "F"],
            3: ["G"],
        },
    )

    assert result.nodes_per_hop == {
        0: 1,
        1: 2,
        2: 3,
        3: 1,
    }


def test_blast_radius_excludes_source():
    result = NeighborhoodResult(
        source_node="A",
        direction="downstream",
        max_hops=2,
        nodes_by_hop={
            0: ["A"],
            1: ["B", "C"],
            2: ["D", "E"],
        },
    )

    assert result.total_nodes == 5
    assert result.blast_radius == 4


def test_blast_radius_for_source_only():
    result = NeighborhoodResult(
        source_node="A",
        direction="downstream",
        max_hops=3,
        nodes_by_hop={
            0: ["A"],
        },
    )

    assert result.total_nodes == 1
    assert result.blast_radius == 0


def test_average_nodes_per_hop():
    result = NeighborhoodResult(
        source_node="A",
        direction="downstream",
        max_hops=3,
        nodes_by_hop={
            0: ["A"],
            1: ["B", "C"],
            2: ["D", "E", "F"],
            3: ["G"],
        },
    )

    # (2 + 3 + 1) / 3 = 2
    assert result.average_nodes_per_hop == 2.0

def test_neighborhood_result_to_dict():
    result = NeighborhoodResult(
        source_node="A",
        direction="upstream",
        max_hops=2,
        nodes_by_hop={
            0: ["A"],
            1: ["B"],
            2: ["C", "D"],
        },
    )

    data = result.to_dict()

    assert data["source_node"] == "A"
    assert data["direction"] == "upstream"
    assert data["max_hops"] == 2
    assert data["nodes_by_hop"] == {
        0: ["A"],
        1: ["B"],
        2: ["C", "D"],
    }
    assert data["total_nodes"] == 4
    assert data["max_reached_hop"] == 2
