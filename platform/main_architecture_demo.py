from pathlib import Path

from platform.analyzers.architecture_analyzer import ArchitectureAnalyzer
from platform.reporters.architecture_reporter import ArchitectureReporter
from platform.services.circular_dependency_detector import (
    CircularDependencyDetector,
)
from platform.services.dependency_graph_service import (
    DependencyGraphService,
)

engine = Path("src/ic08")

graph = DependencyGraphService().build(engine)

graph = CircularDependencyDetector().detect(graph)

report = ArchitectureAnalyzer().analyze(graph)

ArchitectureReporter().print(report)
