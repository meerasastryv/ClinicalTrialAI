"""
Dependency Intelligence Models

Provides intelligent metrics over the dependency graph.

Author: ClinicalTrialAI Platform
"""

from dataclasses import dataclass, field
from typing import List, Dict


@dataclass
class ModuleMetrics:
    """
    Metrics for an individual module.
    """

    name: str

    fan_in: int = 0
    fan_out: int = 0

    instability: float = 0.0

    risk: str = "LOW"

    in_cycle: bool = False

    layer: str = ""

    dependencies: List[str] = field(default_factory=list)

    dependents: List[str] = field(default_factory=list)


@dataclass
class CircularDependency:
    """
    Represents a dependency cycle.
    """

    modules: List[str]


@dataclass
class LayerViolation:
    """
    Represents a layer violation.
    """

    source: str
    target: str
    reason: str


@dataclass
class Hotspot:
    """
    Architectural hotspot.
    """

    module: str

    score: float

    reason: str


@dataclass
class DependencyIntelligence:
    """
    Complete dependency intelligence report.
    """

    module_metrics: Dict[str, ModuleMetrics] = field(default_factory=dict)

    circular_dependencies: List[CircularDependency] = field(default_factory=list)

    layer_violations: List[LayerViolation] = field(default_factory=list)

    hotspots: List[Hotspot] = field(default_factory=list)

    recommendations: List[str] = field(default_factory=list)
