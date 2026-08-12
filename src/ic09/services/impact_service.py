"""
Impact Service

Core orchestration service for performing impact analysis.

Author: ClinicalTrialAI
"""

import time
import uuid

from src.ic09.models.change_request import ChangeRequest
from src.ic09.models.impact_result import ImpactResult
from src.ic09.models.impact_node import ImpactNode
from src.ic09.repositories.impact_repository import ImpactRepository
from src.ic09.services.relationship_service import RelationshipService
from src.ic09.services.requirement_impact_service import (
    RequirementImpactService,
)
from src.ic09.services.code_impact_service import CodeImpactService

from src.ic09.services.runtime_impact_service import RuntimeImpactService
from src.ic09.services.test_impact_service import TestImpactService

class ImpactService:
    """
    Performs end-to-end impact analysis.
    """





    def __init__(self, repository: ImpactRepository) -> None:
        """
        Initialize the impact service.
        """
        self._repository = repository
        self._relationship_service = RelationshipService(repository)
        self._requirement_service = RequirementImpactService(repository)
        self._code_service = CodeImpactService(repository)
        self._runtime_service = RuntimeImpactService(repository)
        self._test_service = TestImpactService(repository)
    def register_requirement(self,requirement_id: str,requirement_name: str,) -> ImpactNode:
        """
        Register a requirement in the impact graph.
        """
        return self._requirement_service.register_requirement(requirement_id,requirement_name,)
    def link_requirement_to_file(self,requirement_id: str,file_name: str,) -> None:
        """
        Link a requirement to its implementing source file.
        """
        self._requirement_service.link_requirement_to_file(requirement_id,file_name,)


    def register_file( self, file_name: str,) -> ImpactNode:
        """
        Register a source file.
        """
        return self._code_service.register_file(file_name)
    def register_class( self,file_name: str, class_name: str,) -> ImpactNode:
        """
        Register a class.
        """
        return self._code_service.register_class(   file_name, class_name,)
    def register_method(  self,  class_name: str,  method_name: str,) -> ImpactNode:
        """
        Register a method.
        """
        return self._code_service.register_method(  class_name, method_name, )
    def register_method_call(self,  caller_method: str, callee_method: str,) -> None:
        """
        Register a method call relationship.
        """
        self._code_service.register_method_call(  caller_method,     callee_method, )


    def register_runtime_flow(self,flow_name: str,) -> ImpactNode:
        """
        Register a runtime flow.
        """
        return self._runtime_service.register_runtime_flow(flow_name)

    def link_method_to_runtime( self,  method_name: str,   runtime_flow: str,) -> None:
        """
        Link a method to a runtime flow.
        """
        self._runtime_service.link_method_to_runtime(  method_name,   runtime_flow, )
    def register_api( self,   api_name: str,) -> ImpactNode:
        """
        Register an API endpoint.
        """
        return self._runtime_service.register_api(api_name)
    def link_runtime_to_api( self, runtime_flow: str,  api_name: str,) -> None:
        """
        Link a runtime flow to an API.
        """
        self._runtime_service.link_runtime_to_api(   runtime_flow,    api_name,  )
    def register_database(  self, database_object: str,) -> ImpactNode:
        """
        Register a database object.
        """
        return self._runtime_service.register_database(  database_object, )
    def link_api_to_database(self,  api_name: str, database_object: str,) -> None:
        """
        Link an API to a database object.
        """
        self._runtime_service.link_api_to_database( api_name, database_object,)
    def register_test_case(self,test_id: str,test_name: str,) -> ImpactNode:
        """
        Register a test case.
        """
        return self._test_service.register_test_case(test_id,test_name,)
    def link_method_to_test( self,  method_name: str,  test_id: str,) -> None:
        """
        Link a method to a test case.
        """
        self._test_service.link_method_to_test(  method_name,     test_id,  )
    def register_test_suite(   self,  suite_name: str,) -> ImpactNode:
        """
        Register a test suite.
        """
        return self._test_service.register_test_suite(suite_name,)
    def link_test_to_suite( self,  test_id: str,suite_name: str,) -> None:
        """
        Link a test case to a test suite.
        """
        self._test_service.link_test_to_suite(test_id,   suite_name, )


    def analyze(self, request: ChangeRequest,direction: str = "downstream",) -> ImpactResult:
    #def analyze(self, request: ChangeRequest) -> ImpactResult:
        """
        Analyze the impact of a change request.
        """
        start_time = time.perf_counter()

        result = ImpactResult(
            analysis_id=str(uuid.uuid4()),
            source_artifact=request.artifact_id,
            source_type=request.artifact_type,
        )

        # Add the source artifact if it exists in the repository
        source_node = self._repository.get_node(request.artifact_id)


        # Discover transitive impacts
        if direction == "downstream":
            impacted_nodes = self._relationship_service.get_transitive_impacts(request.artifact_id)
        elif direction == "upstream":
            impacted_nodes = self._relationship_service.get_upstream_impacts(request.artifact_id)
        else:
            raise ValueError(f"Unsupported impact direction: {direction}")
        # Discover transitive impacts

        for node in impacted_nodes:
            result.add_node(node)

        # Include all traversed relationships
        for edge in self._repository.get_all_edges():
            if (
                edge.source_id == request.artifact_id
                or edge.source_id in {n.node_id for n in impacted_nodes}
            ):
                result.add_relationship(edge)

        # Simple placeholder risk calculation
        result.risk_score = self._calculate_risk(result)

        result.execution_time = round(
            time.perf_counter() - start_time,
            4
        )

        return result

    def _calculate_risk(self, result: ImpactResult) -> float:
        """
        Basic risk calculation.

        This implementation will be replaced with a more
        advanced scoring engine in a later milestone.
        """
        impact_count = result.total_impacts

        if impact_count == 0:
            return 0.0

        return min(1.0, impact_count / 25.0)
