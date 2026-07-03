from typing import List

from src.ic03.models.dependency import Dependency


class DependencyRepository:
    """
    Repository for storing discovered dependencies.
    """

    def __init__(self):
        self._dependencies: List[Dependency] = []

    def add_dependency(self, dependency: Dependency):
        """
        Add a dependency.
        """
        self._dependencies.append(dependency)

    def get_all_dependencies(self) -> List[Dependency]:
        """
        Return all dependencies.
        """
        return self._dependencies

    def clear(self):
        """
        Remove all stored dependencies.
        """
        self._dependencies.clear()
