"""
Runtime Impact Service

Registers runtime execution artifacts into the impact graph.

Author: ClinicalTrialAI
"""

from src.ic09.models.impact_edge import ImpactEdge
from src.ic09.models.impact_node import ImpactNode
from src.ic09.repositories.impact_repository import ImpactRepository


class RuntimeImpactService:
    """
    Registers runtime execution artifacts.
    """

    def __init__(self, repository: ImpactRepository) -> None:
        self._repository = repository

    def register_runtime_flow(
        self,
        flow_name: str,
    ) -> ImpactNode:
        """
        Register a runtime flow.
        """
        node = self._repository.get_node(flow_name)

        if node is None:
            node = ImpactNode(
                node_id=flow_name,
                node_type="RuntimeFlow",
                name=flow_name,
                confidence=1.0,
            )
            self._repository.add_node(node)

        return node

    def link_method_to_runtime(
        self,
        method_name: str,
        runtime_flow: str,
    ) -> None:
        """
        Link a method to a runtime flow.
        """
        self._repository.add_edge(
            ImpactEdge(
                source_id=method_name,
                target_id=runtime_flow,
                relationship="EXECUTES",
            )
        )

    def register_api(
        self,
        api_name: str,
    ) -> ImpactNode:
        """
        Register an API endpoint.
        """
        node = self._repository.get_node(api_name)

        if node is None:
            node = ImpactNode(
                node_id=api_name,
                node_type="API",
                name=api_name,
                confidence=1.0,
            )
            self._repository.add_node(node)

        return node

    def link_runtime_to_api(
        self,
        runtime_flow: str,
        api_name: str,
    ) -> None:
        """
        Connect runtime flow to API.
        """
        self._repository.add_edge(
            ImpactEdge(
                source_id=runtime_flow,
                target_id=api_name,
                relationship="INVOKES",
            )
        )

    def register_database(
        self,
        database_object: str,
    ) -> ImpactNode:
        """
        Register a database object.
        """
        node = self._repository.get_node(database_object)

        if node is None:
            node = ImpactNode(
                node_id=database_object,
                node_type="Database",
                name=database_object,
                confidence=1.0,
            )
            self._repository.add_node(node)

        return node

    def link_api_to_database(
        self,
        api_name: str,
        database_object: str,
    ) -> None:
        """
        Connect API to database.
        """
        self._repository.add_edge(
            ImpactEdge(
                source_id=api_name,
                target_id=database_object,
                relationship="ACCESSES",
            )
        )
