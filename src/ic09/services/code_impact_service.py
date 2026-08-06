"""
Code Impact Service

Builds impact graph information from source code artifacts.

Author: ClinicalTrialAI
"""

from src.ic09.models.impact_edge import ImpactEdge
from src.ic09.models.impact_node import ImpactNode
from src.ic09.repositories.impact_repository import ImpactRepository


class CodeImpactService:
    """
    Registers source code artifacts in the impact graph.
    """

    def __init__(self, repository: ImpactRepository) -> None:
        self._repository = repository

    def register_file(self, file_name: str) -> ImpactNode:
        """
        Register a source file.
        """
        node = self._repository.get_node(file_name)

        if node is None:
            node = ImpactNode(
                node_id=file_name,
                node_type="File",
                name=file_name,
                confidence=1.0,
            )
            self._repository.add_node(node)

        return node

    def register_class(
        self,
        file_name: str,
        class_name: str,
    ) -> ImpactNode:
        """
        Register a class and connect it to its file.
        """
        node = self._repository.get_node(class_name)

        if node is None:
            node = ImpactNode(
                node_id=class_name,
                node_type="Class",
                name=class_name,
                confidence=1.0,
            )
            self._repository.add_node(node)

        self._repository.add_edge(
            ImpactEdge(
                source_id=file_name,
                target_id=class_name,
                relationship="CONTAINS",
            )
        )

        return node

    def register_method(
        self,
        class_name: str,
        method_name: str,
    ) -> ImpactNode:
        """
        Register a method and connect it to its class.
        """
        node = self._repository.get_node(method_name)

        if node is None:
            node = ImpactNode(
                node_id=method_name,
                node_type="Method",
                name=method_name,
                confidence=1.0,
            )
            self._repository.add_node(node)

        self._repository.add_edge(
            ImpactEdge(
                source_id=class_name,
                target_id=method_name,
                relationship="HAS_METHOD",
            )
        )

        return node

    def register_method_call(
        self,
        caller_method: str,
        callee_method: str,
    ) -> None:
        """
        Register a method call relationship.
        """
        self._repository.add_edge(
            ImpactEdge(
                source_id=caller_method,
                target_id=callee_method,
                relationship="CALLS",
            )
        )
