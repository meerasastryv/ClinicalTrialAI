from src.ic09.models.change_request import ChangeRequest
from src.ic09.repositories.impact_repository import ImpactRepository
from src.ic09.services.impact_service import ImpactService
import pytest

def test_analyze_downstream_impact():
    repository = ImpactRepository()
    service = ImpactService(repository)

    service.register_file("service_a.py")
    service.register_file("service_b.py")
    service.register_file("service_c.py")

    service.register_method("ServiceA", "method_a")
    service.register_method("ServiceB", "method_b")
    service.register_method("ServiceC", "method_c")

    service.register_method_call(
        "method_a",
        "method_b",
    )

    service.register_method_call(
        "method_b",
        "method_c",
    )

    request = ChangeRequest(
        change_id="CR-001",
        title="Change method_a implementation",
        artifact_id="method_a",
        artifact_type="Method",
    )


    result = service.analyze(request)

    impacted_ids = {
        node.node_id
        for node in result.impacted_nodes
    }

    assert "method_b" in impacted_ids
    assert "method_c" in impacted_ids
    assert result.total_impacts == 2

def test_analyze_unknown_artifact():
    repository = ImpactRepository()
    service = ImpactService(repository)

    request = ChangeRequest(
        change_id="CR-002",
        title="Unknown artifact change",
        artifact_id="unknown_method",
        artifact_type="Method",
    )

    result = service.analyze(request)

    assert result.impacted_nodes == []
    assert result.total_impacts == 0



def test_analyze_upstream_impact():
    repository = ImpactRepository()
    service = ImpactService(repository)

    service.register_method("ServiceA", "method_a")
    service.register_method("ServiceB", "method_b")
    service.register_method("ServiceC", "method_c")

    service.register_method_call(
        "method_a",
        "method_b",
    )

    service.register_method_call(
        "method_b",
        "method_c",
    )

    request = ChangeRequest(
        change_id="CR-003",
        title="Change method_c implementation",
        artifact_id="method_c",
        artifact_type="Method",
    )

    result = service.analyze(
        request,
        direction="upstream",
    )

    impacted_ids = {
        node.node_id
        for node in result.impacted_nodes
    }

    assert "method_a" in impacted_ids
    assert "method_b" in impacted_ids
    assert "method_c" not in impacted_ids
    assert result.total_impacts == 2


def test_analyze_invalid_direction():
    repository = ImpactRepository()
    service = ImpactService(repository)

    service.register_method("ServiceA", "method_a")

    request = ChangeRequest(
        change_id="CR-004",
        title="Invalid direction test",
        artifact_id="method_a",
        artifact_type="Method",
    )

    with pytest.raises(
        ValueError,
        match="Unsupported impact direction",
    ):
        service.analyze(
            request,
            direction="sideways",
        )


def test_analyze_downstream_impact_includes_relationships():
    repository = ImpactRepository()
    service = ImpactService(repository)

    service.register_method("ServiceA", "method_a")
    service.register_method("ServiceB", "method_b")
    service.register_method("ServiceC", "method_c")

    service.register_method_call(
        "method_a",
        "method_b",
    )

    service.register_method_call(
        "method_b",
        "method_c",
    )

    request = ChangeRequest(
        change_id="CR-005",
        title="Change method_a implementation",
        artifact_id="method_a",
        artifact_type="Method",
    )

    result = service.analyze(request)

    relationship_pairs = {
        (edge.source_id, edge.target_id)
        for edge in result.relationships
    }

    assert ("method_a", "method_b") in relationship_pairs
    assert ("method_b", "method_c") in relationship_pairs


def test_analyze_requirement_downstream_impact_across_domains():
    repository = ImpactRepository()
    service = ImpactService(repository)

    # Requirement
    service.register_requirement(
        "REQ-001",
        "Patient data retrieval requirement",
    )

    # Code
    service.register_file("service_a.py")
    service.register_class("service_a.py", "ServiceA")
    service.register_method("ServiceA", "method_a")

    # Requirement -> Code
    service.link_requirement_to_file(
        "REQ-001",
        "service_a.py",
    )

    # Code -> Runtime
    service.register_runtime_flow("patient_retrieval_flow")
    service.link_method_to_runtime(
        "method_a",
        "patient_retrieval_flow",
    )

    service.register_api("GET /patients")
    service.link_runtime_to_api(
        "patient_retrieval_flow",
        "GET /patients",
    )

    service.register_database("patients_table")
    service.link_api_to_database(
        "GET /patients",
        "patients_table",
    )

    # Code -> Test
    service.register_test_case(
        "TC-001",
        "Verify patient retrieval",
    )
    service.link_method_to_test(
        "method_a",
        "TC-001",
    )

    service.register_test_suite("regression_suite")
    service.link_test_to_suite(
        "TC-001",
        "regression_suite",
    )

    # Change request originates at the requirement
    request = ChangeRequest(
        change_id="CR-006",
        title="Change patient data retrieval requirement",
        artifact_id="REQ-001",
        artifact_type="Requirement",
    )

    result = service.analyze(request)

    impacted_ids = {
        node.node_id
        for node in result.impacted_nodes
    }

    assert "service_a.py" in impacted_ids
    assert "ServiceA" in impacted_ids
    assert "method_a" in impacted_ids
    assert "patient_retrieval_flow" in impacted_ids
    assert "GET /patients" in impacted_ids
    assert "patients_table" in impacted_ids
    assert "TC-001" in impacted_ids
    assert "regression_suite" in impacted_ids

    assert "REQ-001" not in impacted_ids

    assert result.total_impacts == 8
