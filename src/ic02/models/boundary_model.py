"""
Boundary Value Model

Represents a single Boundary Value Analysis (BVA) test case generated
from a requirement.
"""

from dataclasses import dataclass


@dataclass
class BoundaryModel:
    """
    Represents one boundary value test case.
    """

    requirement_id: str
    parameter: str
    boundary_type: str
    input_value: str
    expected_result: str
