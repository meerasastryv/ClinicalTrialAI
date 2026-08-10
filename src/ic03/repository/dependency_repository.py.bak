from typing import List, Optional

from src.ic03.models.dependency import Dependency


class DependencyRepository:
    """
    Central repository for storing all relationships discovered during
    static code analysis.

    This repository stores relationships such as:

    - IMPORT
    - CLASS_DEPENDENCY
    - INHERITANCE
    - METHOD_CALL
    - ATTRIBUTE
    - ANNOTATION

    Future ICs can reuse this repository for:
    - Impact Analysis
    - Traceability
    - Knowledge Graph
    - Risk Intelligence
    """

    def __init__(self):
        self._dependencies: List[Dependency] = []

    # ---------------------------------------------------------
    # CRUD Operations
    # ---------------------------------------------------------

    def add_dependency(self, dependency: Dependency):
        """
        Add a discovered dependency.
        """
        self._dependencies.append(dependency)

    def get_all_dependencies(self) -> List[Dependency]:
        """
        Return all stored dependencies.
        """
        return self._dependencies

    def clear(self):
        """
        Remove all stored dependencies.
        """
        self._dependencies.clear()

    # ---------------------------------------------------------
    # Query Operations
    # ---------------------------------------------------------

    def get_by_source(self, source: str) -> List[Dependency]:
        """
        Return all dependencies originating from a source.
        """
        return [
            dependency
            for dependency in self._dependencies
            if dependency.source == source
        ]

    def get_by_target(self, target: str) -> List[Dependency]:
        """
        Return all dependencies pointing to a target.
        """
        return [
            dependency
            for dependency in self._dependencies
            if dependency.target == target
        ]

    def get_by_type(self, dependency_type: str) -> List[Dependency]:
        """
        Return all dependencies of a specific type.
        """
        return [
            dependency
            for dependency in self._dependencies
            if dependency.dependency_type == dependency_type
        ]

    def find(
        self,
        source: str,
        target: str,
    ) -> Optional[Dependency]:
        """
        Find a dependency between two entities.
        """
        for dependency in self._dependencies:

            if (
                dependency.source == source
                and dependency.target == target
            ):
                return dependency

        return None

    def exists(
        self,
        source: str,
        target: str,
    ) -> bool:
        """
        Check whether a dependency already exists.
        """
        return self.find(source, target) is not None

    def count(self) -> int:
        """
        Return total number of dependencies.
        """
        return len(self._dependencies)
