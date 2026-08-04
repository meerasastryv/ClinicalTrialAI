from pathlib import Path
from platform.analyzers.architecture_analyzer import (
    ArchitectureAnalyzer,
)

from platform.reporters.architecture_reporter import (
    ArchitectureReporter,
)

from platform.services.circular_dependency_detector import (
    CircularDependencyDetector,
)

from platform.services.dependency_graph_service import (
    DependencyGraphService,
)


def main():

    engine = Path("src")

    graph = (
        DependencyGraphService()
        .build(engine)
    )
    graph = (
        CircularDependencyDetector()
        .detect(graph)
    )
    result = (
        ArchitectureAnalyzer()
        .execute(graph)
    )
    report = (
        ArchitectureAnalyzer.get_report(result)
    )
    output_dir = Path("platform/output")
    reporter = ArchitectureReporter(
        output_dir
    )
    reporter.print(report)
    reporter.generate(
        result,
        "architecture_report.json",
        "architecture_report.md",
    )

if __name__ == "__main__":
    main()
