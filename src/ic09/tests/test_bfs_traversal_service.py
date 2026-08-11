#import pytest

#from src.ic09.models.dependency_graph import DependencyGraph
#from src.ic09.services.bfs_traversal_service import BFSTraversalService
import pytest

from ct_platform.graph.dependency_graph import DependencyGraph
from ct_platform.graph.dependency_node import DependencyNode
from ct_platform.graph.dependency_edge import DependencyEdge

from src.ic09.services.bfs_traversal_service import BFSTraversalService

@pytest.fixture
def sample_graph():
    """
    Graph Structure

            A
          / | \
         B  C  E
          \ |
           D
    """

    graph = DependencyGraph()

    # Create nodes
    for node_id in ["A", "B", "C", "D", "E"]:
        graph.add_node(
            DependencyNode(
                id=node_id,
                name=node_id,
            )
        )

    # Create edges
    graph.add_edge(
        DependencyEdge(
            source="A",
            target="B",
        )
    )

    graph.add_edge(
        DependencyEdge(
            source="A",
            target="C",
        )
    )

    graph.add_edge(
        DependencyEdge(
            source="A",
            target="E",
        )
    )

    graph.add_edge(
        DependencyEdge(
            source="B",
            target="D",
        )
    )

    graph.add_edge(
        DependencyEdge(
            source="C",
            target="D",
        )
    )

    return graph

@pytest.fixture
def bfs_service(sample_graph):
    return BFSTraversalService(sample_graph)


def test_downstream_traversal(bfs_service):

    traversal = bfs_service.traverse("A")

    assert traversal[0] == "A"

    assert set(traversal) == {
        "A",
        "B",
        "C",
        "D",
        "E",
    }

def test_upstream_traversal(bfs_service):

    traversal = bfs_service.traverse(
        "D",
        direction="upstream",
    )

    assert set(traversal) == {
        "A",
        "B",
        "C",
        "D",
    }


def test_max_depth(bfs_service):

    traversal = bfs_service.traverse(
        "A",
        max_depth=1,
    )

    assert "D" not in traversal

    assert set(traversal) == {
        "A",
        "B",
        "C",
        "E",
    }

def test_is_reachable(bfs_service):

    assert bfs_service.is_reachable("A", "D")

    assert not bfs_service.is_reachable("E", "D")

def test_distances(bfs_service):

    distances = bfs_service.get_distances("A")

    assert distances["A"] == 0
    assert distances["B"] == 1
    assert distances["C"] == 1
    assert distances["E"] == 1
    assert distances["D"] == 2

def test_levels(bfs_service):

    levels = bfs_service.get_levels("A")

    assert levels[0] == ["A"]

    assert set(levels[1]) == {
        "B",
        "C",
        "E",
    }

    assert levels[2] == ["D"]

def test_traversal_statistics(bfs_service):

    stats = bfs_service.traversal_statistics("A")

    assert stats["start_node"] == "A"
    assert stats["direction"] == "downstream"
    assert stats["visited_nodes"] == 5
    assert stats["levels"] == 3
    assert stats["max_level"] == 2

def test_invalid_node(bfs_service):

    assert bfs_service.traverse("UNKNOWN") == []

    assert bfs_service.get_levels("UNKNOWN") == {}

    assert bfs_service.get_distances("UNKNOWN") == {}

    assert bfs_service.reachable_nodes("UNKNOWN") == set()

def test_invalid_max_depth(bfs_service):

    with pytest.raises(ValueError):
        bfs_service.traverse(
            "A",
            max_depth=-1,
        )


def test_bfs_find_path(bfs_service):

    result = bfs_service.find_path("A", "D")

    assert result == ["A", "B", "D"]


def test_bfs_find_path_not_found(bfs_service):

    result = bfs_service.find_path("D", "A")

    assert result == []


def test_bfs_find_path_unknown_node(bfs_service):

    assert bfs_service.find_path("UNKNOWN", "D") == []




def test_bfs_find_path_upstream(bfs_service):

    result = bfs_service.find_path(
        "D",
        "A",
        direction="upstream",
    )

    assert result == ["D", "B", "A"]
