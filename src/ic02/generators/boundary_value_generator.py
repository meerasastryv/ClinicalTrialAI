"""
Boundary Value Generator

Generates Boundary Value Analysis (BVA) test cases from
requirements containing numeric ranges.
"""

import re

from src.ic02.models.boundary_model import BoundaryModel
from src.ic02.repositories.boundary_repository import BoundaryRepository


class BoundaryValueGenerator:
    """
    Generates boundary value test cases.
    """

    def __init__(self):
        self.repository = BoundaryRepository()

    def generate(self, requirement):
        """
        Generate boundary value test cases for a single requirement.
        """

        self.repository.clear()

        self._process_requirement(requirement)

        return self.repository.get_all()

    def _process_requirement(self, requirement):
        """
        Process one requirement.
        """

        text = requirement.description

        pattern = r"between\s+(\d+)\s+and\s+(\d+)"

        match = re.search(pattern, text, re.IGNORECASE)

        if not match:
            return

        minimum = int(match.group(1))
        maximum = int(match.group(2))

        self._generate_numeric_boundaries(
            requirement,
            minimum,
            maximum,
        )

    def _generate_numeric_boundaries(
        self,
        requirement,
        minimum,
        maximum,
    ):
        """
        Generate numeric boundary value test cases.
        """

        boundary_cases = [
            ("Minimum - 1", minimum - 1, "Invalid"),
            ("Minimum", minimum, "Valid"),
            ("Minimum + 1", minimum + 1, "Valid"),
            ("Maximum - 1", maximum - 1, "Valid"),
            ("Maximum", maximum, "Valid"),
            ("Maximum + 1", maximum + 1, "Invalid"),
        ]

        for boundary_type, value, expected in boundary_cases:

            boundary = BoundaryModel(
                requirement_id=requirement.requirement_id,
                parameter="Value",
                boundary_type=boundary_type,
                input_value=str(value),
                expected_result=expected,
            )

            self.repository.add(boundary)
