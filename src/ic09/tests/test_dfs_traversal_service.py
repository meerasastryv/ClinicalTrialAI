import pytest

from ct_platform.graph.dependency_edge import DependencyEdge
from ct_platform.graph.dependency_graph import DependencyGraph
from ct_platform.graph.dependency_node import DependencyNode
from src.ic09.services.dfs_traversal_service import DFSTraversalService


def build_test_graph() -> DependencyGraph:
    """
    Build a deterministic dependency graph for DFS tests.

            A
           / \
          B   C
         / \   \
        D   E   F
             \
              G
    """

    graph = DependencyGraph()

    for node_id in ["A", "B", "C", "D", "E", "F", "G"]:
        graph.add_node(
            DependencyNode(
                id=node_id,
                name=node_id,
            )
        )

    edges = [
        ("A", "B"),
        ("A", "C"),
        ("B", "D"),
        ("B", "E"),
        ("C", "F"),
        ("E", "G"),
    ]

    for source, target in edges:
        graph.add_edge(
            DependencyEdge(
                source=source,
                target=target,
            )
        )

    return graph


def test_dfs_downstream_traversal():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    result = service.traverse(
        "A",
        direction="downstream",
    )

    assert result == ["A", "B", "D", "E", "G", "C", "F"]


def test_dfs_upstream_traversal():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    result = service.traverse(
        "G",
        direction="upstream",
    )

    assert result == ["G", "E", "B", "A"]


def test_dfs_max_depth_zero():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    result = service.traverse(
        "A",
        direction="downstream",
        max_depth=0,
    )

    assert result == ["A"]


def test_dfs_max_depth_one():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    result = service.traverse(
        "A",
        direction="downstream",
        max_depth=1,
    )

    assert result == ["A", "B", "C"]


def test_dfs_max_depth_two():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    result = service.traverse(
        "A",
        direction="downstream",
        max_depth=2,
    )

    assert result == ["A", "B", "D", "E", "C", "F"]


def test_dfs_reachable():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    assert service.is_reachable("A", "G")
    assert service.is_reachable("A", "F")
    assert service.is_reachable("B", "G")


def test_dfs_not_reachable():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    assert not service.is_reachable("D", "A")
    assert not service.is_reachable("F", "G")


def test_dfs_upstream_reachable():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    assert service.is_reachable(
        "G",
        "A",
        direction="upstream",
    )


def test_dfs_reachable_nodes():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    result = service.reachable_nodes(
        "A",
        direction="downstream",
    )

    assert result == {"A", "B", "C", "D", "E", "F", "G"}


def test_dfs_depth_limited_traversal():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    result = service.traverse(
        "A",
        direction="downstream",
        max_depth=2,
    )

    assert "D" in result
    assert "F" in result
    assert "G" not in result

def test_dfs_unknown_start_node():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    assert service.traverse("UNKNOWN") == []


def test_dfs_unknown_target_node():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    assert not service.is_reachable(
        "A",
        "UNKNOWN",
    )


def test_dfs_invalid_depth():
    graph = build_test_graph()
    service = DFSTraversalService(graph)

    with pytest.raises(ValueError):
        service.traverse(
            "A",
            max_depth=-1,
        )
