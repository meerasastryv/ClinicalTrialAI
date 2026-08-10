"""
Test Impact Service

Registers test artifacts into the impact graph.

Author: ClinicalTrialAI
"""

from src.ic09.models.impact_edge import ImpactEdge
from src.ic09.models.impact_node import ImpactNode
from src.ic09.repositories.impact_repository import ImpactRepository


class TestImpactService:
    """
    Registers test artifacts and relationships.
    """

    def __init__(self, repository: ImpactRepository) -> None:
        self._repository = repository

    def register_test_case(
        self,
        test_id: str,
        test_name: str,
    ) -> ImpactNode:
        """
        Register a test case.
        """
        node = self._repository.get_node(test_id)

        if node is None:
            node = ImpactNode(
                node_id=test_id,
                node_type="TestCase",
                name=test_name,
                confidence=1.0,
            )
            self._repository.add_node(node)

        return node

    def link_method_to_test(
        self,
        method_name: str,
        test_id: str,
    ) -> None:
        """
        Link a method to a test case.
        """
        self._repository.add_edge(
            ImpactEdge(
                source_id=method_name,
                target_id=test_id,
                relationship="TESTED_BY",
            )
        )

    def register_test_suite(
        self,
        suite_name: str,
    ) -> ImpactNode:
        """
        Register a test suite.
        """
        node = self._repository.get_node(suite_name)

        if node is None:
            node = ImpactNode(
                node_id=suite_name,
                node_type="TestSuite",
                name=suite_name,
                confidence=1.0,
            )
            self._repository.add_node(node)

        return node

    def link_test_to_suite(
        self,
        test_id: str,
        suite_name: str,
    ) -> None:
        """
        Associate a test case with a test suite.
        """
        self._repository.add_edge(
            ImpactEdge(
                source_id=test_id,
                target_id=suite_name,
                relationship="BELONGS_TO",
            )
        )
