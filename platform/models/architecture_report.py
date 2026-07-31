"""
architecture_report.py

Architecture Intelligence Report
"""

from dataclasses import dataclass, field
from typing import Dict, List

from platform.framework.base_report import BaseReport


@dataclass
class ArchitectureReport(BaseReport):
    """
    Architecture-specific report.
    """

    #
    # Project Information
    #
    engine_id: str = ""

    total_python_files: int = 0

    #
    # Dependency Metrics
    #
    total_dependencies: int = 0

    internal_dependencies: int = 0

    external_dependencies: int = 0

    standard_library_dependencies: int = 0

    #
    # Dependency Analysis
    #
    circular_dependencies: List[List[str]] = field(
        default_factory=list
    )

    fan_in: Dict[str, int] = field(
        default_factory=dict
    )

    fan_out: Dict[str, int] = field(
        default_factory=dict
    )

    hotspots: List[str] = field(
        default_factory=list
    )

    dead_code: List[str] = field(
        default_factory=list
    )
    dependency_intelligence: object = None

    #
    # Architecture Health
    #
    health_score: float = 0.0

    rating: str = ""

    recommendations: List[str] = field(
        default_factory=list
    )

    warnings: List[str] = field(
        default_factory=list
    )

    def __post_init__(self):
        """
        Initialize BaseReport defaults.
        """
        self.report_name = "Architecture Intelligence Report"
        self.analyzer_name = "ArchitectureAnalyzer"
