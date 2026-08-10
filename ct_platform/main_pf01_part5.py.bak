from pathlib import Path
from ct_platform.analyzers.architecture_analyzer import (
    ArchitectureAnalyzer,
)

from ct_platform.reporters.architecture_reporter import (
    ArchitectureReporter,
)

from ct_platform.services.circular_dependency_detector import (
    CircularDependencyDetector,
)

from ct_platform.services.dependency_graph_service import (
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
