from src.ic09.models.impact_edge import ImpactEdge
from src.ic09.models.impact_node import ImpactNode
from src.ic09.repositories.impact_repository import ImpactRepository
from src.ic09.services.relationship_service import RelationshipService


def test_get_direct_impacts():
    repository = ImpactRepository()

    source = ImpactNode(
        node_id="A",
        node_type="Service",
        name="Service A",
    )

    target = ImpactNode(
        node_id="B",
        node_type="Service",
        name="Service B",
    )

    repository.add_node(source)
    repository.add_node(target)

    repository.add_edge(
        ImpactEdge(
            source_id="A",
            target_id="B",
            relationship="DEPENDS_ON",
        )
    )

    service = RelationshipService(repository)

    impacts = service.get_direct_impacts("A")

    assert len(impacts) == 1
    assert impacts[0].node_id == "B"


def test_get_transitive_impacts():
    repository = ImpactRepository()

    nodes = [
        ImpactNode(
            node_id="A",
            node_type="Service",
            name="Service A",
        ),
        ImpactNode(
            node_id="B",
            node_type="Service",
            name="Service B",
        ),
        ImpactNode(
            node_id="C",
            node_type="Service",
            name="Service C",
        ),
    ]

    for node in nodes:
        repository.add_node(node)

    repository.add_edge(
        ImpactEdge(
            source_id="A",
            target_id="B",
            relationship="DEPENDS_ON",
        )
    )

    repository.add_edge(
        ImpactEdge(
            source_id="B",
            target_id="C",
            relationship="DEPENDS_ON",
        )
    )

    service = RelationshipService(repository)

    impacts = service.get_transitive_impacts("A")

    impacted_ids = {node.node_id for node in impacts}

    assert impacted_ids == {"B", "C"}


def test_get_transitive_impacts_with_cycle():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C"]:
        repository.add_node(
            ImpactNode(
                node_id=node_id,
                node_type="Service",
                name=f"Service {node_id}",
            )
        )

    repository.add_edge(
        ImpactEdge(
            source_id="A",
            target_id="B",
            relationship="DEPENDS_ON",
        )
    )

    repository.add_edge(
        ImpactEdge(
            source_id="B",
            target_id="C",
            relationship="DEPENDS_ON",
        )
    )

    repository.add_edge(
        ImpactEdge(
            source_id="C",
            target_id="A",
            relationship="DEPENDS_ON",
        )
    )

    service = RelationshipService(repository)

    impacts = service.get_transitive_impacts("A")

    impacted_ids = {node.node_id for node in impacts}

    assert impacted_ids == {"B", "C"}


def test_get_transitive_impacts_unknown_node():
    repository = ImpactRepository()

    service = RelationshipService(repository)

    impacts = service.get_transitive_impacts("UNKNOWN")

    assert impacts == []


def test_get_upstream_impacts():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C"]:
        repository.add_node(
            ImpactNode(
                node_id=node_id,
                node_type="Service",
                name=f"Service {node_id}",
            )
        )

    repository.add_edge(
        ImpactEdge(
            source_id="A",
            target_id="B",
            relationship="DEPENDS_ON",
        )
    )

    repository.add_edge(
        ImpactEdge(
            source_id="B",
            target_id="C",
            relationship="DEPENDS_ON",
        )
    )

    service = RelationshipService(repository)

    impacts = service.get_upstream_impacts("C")

    impacted_ids = {node.node_id for node in impacts}

    assert impacted_ids == {"A", "B"}


def test_get_upstream_impacts_with_cycle():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C"]:
        repository.add_node(
            ImpactNode(
                node_id=node_id,
                node_type="Service",
                name=f"Service {node_id}",
            )
        )

    repository.add_edge(
        ImpactEdge(
            source_id="A",
            target_id="B",
            relationship="DEPENDS_ON",
        )
    )

    repository.add_edge(
        ImpactEdge(
            source_id="B",
            target_id="C",
            relationship="DEPENDS_ON",
        )
    )

    repository.add_edge(
        ImpactEdge(
            source_id="C",
            target_id="A",
            relationship="DEPENDS_ON",
        )
    )

    service = RelationshipService(repository)

    impacts = service.get_upstream_impacts("C")

    impacted_ids = {node.node_id for node in impacts}

    assert impacted_ids == {"A", "B"}


def test_find_impact_path_returns_shortest_downstream_path():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C", "D", "E"]:
        repository.add_node(
            ImpactNode(
                node_id=node_id,
                node_type="Service",
                name=f"Service {node_id}",
            )
        )

    # Short path: A -> B -> D
    repository.add_edge(
        ImpactEdge(
            source_id="A",
            target_id="B",
            relationship="DEPENDS_ON",
        )
    )

    repository.add_edge(
        ImpactEdge(
            source_id="B",
            target_id="D",
            relationship="DEPENDS_ON",
        )
    )

    # Longer path: A -> C -> E -> D
    repository.add_edge(
        ImpactEdge(
            source_id="A",
            target_id="C",
            relationship="DEPENDS_ON",
        )
    )

    repository.add_edge(
        ImpactEdge(
            source_id="C",
            target_id="E",
            relationship="DEPENDS_ON",
        )
    )

    repository.add_edge(
        ImpactEdge(
            source_id="E",
            target_id="D",
            relationship="DEPENDS_ON",
        )
    )

    service = RelationshipService(repository)

    path = service.find_impact_path("A", "D")

    assert path == ["A", "B", "D"]


def test_find_impact_path_returns_shortest_upstream_path():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C", "D"]:
        repository.add_node(
            ImpactNode(
                node_id=node_id,
                node_type="Service",
                name=f"Service {node_id}",
            )
        )

    repository.add_edge(
        ImpactEdge(
            source_id="A",
            target_id="B",
            relationship="DEPENDS_ON",
        )
    )

    repository.add_edge(
        ImpactEdge(
            source_id="B",
            target_id="D",
            relationship="DEPENDS_ON",
        )
    )

    repository.add_edge(
        ImpactEdge(
            source_id="C",
            target_id="D",
            relationship="DEPENDS_ON",
        )
    )

    service = RelationshipService(repository)

    path = service.find_impact_path(
        "D",
        "A",
        direction="upstream",
    )

    assert path == ["D", "B", "A"]


def test_find_impact_path_unknown_source_returns_empty_path():
    repository = ImpactRepository()

    repository.add_node(
        ImpactNode(
            node_id="A",
            node_type="Service",
            name="Service A",
        )
    )

    service = RelationshipService(repository)

    path = service.find_impact_path("UNKNOWN", "A")

    assert path == []


def test_find_impact_path_unknown_target_returns_empty_path():
    repository = ImpactRepository()

    repository.add_node(
        ImpactNode(
            node_id="A",
            node_type="Service",
            name="Service A",
        )
    )

    service = RelationshipService(repository)

    path = service.find_impact_path("A", "UNKNOWN")

    assert path == []


def test_find_impact_path_no_path_returns_empty_path():
    repository = ImpactRepository()

    for node_id in ["A", "B", "C"]:
        repository.add_node(
            ImpactNode(
                node_id=node_id,
                node_type="Service",
                name=f"Service {node_id}",
            )
        )

    repository.add_edge(
        ImpactEdge(
            source_id="A",
            target_id="B",
            relationship="DEPENDS_ON",
        )
    )

    service = RelationshipService(repository)

    path = service.find_impact_path("A", "C")

    assert path == []
