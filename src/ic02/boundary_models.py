"""
boundary_models.py

Data models for Boundary Value Analysis (BVA).

Author: Meera Sastry
Project: ClinicalTrialAI - IC-02 Test Design Engine
"""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class BoundaryConstraint:
    """
    Represents a detected boundary constraint.
    """
    parameter: str
    minimum: Optional[float] = None
    maximum: Optional[float] = None
    inclusive_min: bool = True
    inclusive_max: bool = True
    data_type: str = "integer"


@dataclass
class BoundaryValue:
    """
    Represents one generated boundary value.
    """
    label: str
    value: float
    expected_result: str


@dataclass
class BoundaryTestCase:
    """
    Represents one executable boundary test case.
    """
    test_id: str
    parameter: str
    input_value: float
    expected_result: str
    description: str


@dataclass
class BoundaryAnalysisResult:
    """
    Final result returned by the Boundary Value Generator.
    """
    constraint: BoundaryConstraint
    boundary_values: List[BoundaryValue] = field(default_factory=list)
    test_cases: List[BoundaryTestCase] = field(default_factory=list)
