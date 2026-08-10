from pathlib import Path

from ct_platform.analyzers.architecture_analyzer import ArchitectureAnalyzer
from ct_platform.reporters.architecture_reporter import ArchitectureReporter
from ct_platform.services.circular_dependency_detector import (
    CircularDependencyDetector,
)
from ct_platform.services.dependency_graph_service import (
    DependencyGraphService,
)

engine = Path("src/ic08")

graph = DependencyGraphService().build(engine)

graph = CircularDependencyDetector().detect(graph)

report = ArchitectureAnalyzer().analyze(graph)

ArchitectureReporter().print(report)
