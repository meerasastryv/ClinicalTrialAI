"""
Requirement Impact Service

Builds impact graph information from requirement intelligence.

Author: ClinicalTrialAI
"""

from typing import List

from src.ic09.models.impact_node import ImpactNode
from src.ic09.models.impact_edge import ImpactEdge
from src.ic09.repositories.impact_repository import ImpactRepository


class RequirementImpactService:
    """
    Creates impact graph entries from requirement information.
    """

    def __init__(self, repository: ImpactRepository) -> None:
        self._repository = repository

    def register_requirement(
        self,
        requirement_id: str,
        requirement_name: str
    ) -> ImpactNode:
        """
        Register a requirement node.
        """
        node = ImpactNode(
            node_id=requirement_id,
            node_type="Requirement",
            name=requirement_name,
            severity="LOW",
            confidence=1.0,
        )

        self._repository.add_node(node)

        return node

    def link_requirement_to_file(
        self,
        requirement_id: str,
        file_name: str
    ) -> None:
        """
        Link a requirement to a source file.
        """
        file_node = self._repository.get_node(file_name)

        if file_node is None:
            file_node = ImpactNode(
                node_id=file_name,
                node_type="File",
                name=file_name,
                confidence=1.0,
            )
            self._repository.add_node(file_node)

        edge = ImpactEdge(
            source_id=requirement_id,
            target_id=file_name,
            relationship="IMPLEMENTED_BY",
        )

        self._repository.add_edge(edge)

    def get_requirement_impacts(
        self,
        requirement_id: str
    ) -> List[ImpactNode]:
        """
        Return artifacts directly impacted by a requirement.
        """
        return self._repository.get_connected_nodes(requirement_id)
