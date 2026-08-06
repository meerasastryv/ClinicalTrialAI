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


class ImpactService:
    """
    Performs end-to-end impact analysis.
    """

    def __init__(self, repository: ImpactRepository) -> None:
        self._repository = repository
        self._relationship_service = RelationshipService(repository)

    def analyze(self, request: ChangeRequest) -> ImpactResult:
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
        if source_node:
            result.add_node(source_node)

        # Discover transitive impacts
        impacted_nodes = self._relationship_service.get_transitive_impacts(
            request.artifact_id
        )

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
