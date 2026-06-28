"""
Boundary Repository

Stores all generated Boundary Value Analysis (BVA) test cases.
"""

from typing import List

from src.ic02.models.boundary_model import BoundaryModel


class BoundaryRepository:
    """
    Repository for BoundaryModel objects.
    """

    def __init__(self):
        self._boundaries: List[BoundaryModel] = []

    def add(self, boundary: BoundaryModel):
        """
        Add a boundary test case.
        """
        self._boundaries.append(boundary)

    def get_all(self) -> List[BoundaryModel]:
        """
        Return all boundary test cases.
        """
        return self._boundaries

    def clear(self):
        """
        Remove all stored boundary test cases.
        """
        self._boundaries.clear()
