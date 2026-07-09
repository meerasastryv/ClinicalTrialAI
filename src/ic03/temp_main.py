from pathlib import Path

from src.ic03.services.project_analysis_service import (
    ProjectAnalysisService,
)

from src.ic03.services.dependency_analysis_service import (
    DependencyAnalysisService,
)
from src.ic03.reports.dependency_report import (
    DependencyReport,
)

from src.ic03.services.relationship_query_service import (
    RelationshipQueryService,
)
from src.ic03.reports.relationship_query_report import (
    RelationshipQueryReport,
)

from src.ic03.services.graph_traversal_service import (
    GraphTraversalService,
)
from src.ic03.reports.graph_traversal_report import (
    GraphTraversalReport,
)

from src.ic03.services.impact_analysis_service import (
    ImpactAnalysisService,
)
from src.ic03.reports.impact_analysis_report import (
    ImpactAnalysisReport,
)

from src.ic03.services.class_dependency_analysis_service import (
    ClassDependencyAnalysisService,
)
from src.ic03.reports.class_dependency_report import (
    ClassDependencyReport,
)


def main():
    print("=" * 70)
    print("              IC-03 Code Intelligence Engine")
    print("=" * 70)

    project_path = Path(".")

    #
    # Build Code Model
    #
    print("\nBuilding Code Model...")

    project_service = ProjectAnalysisService()

    code_model = project_service.analyze(project_path)

    print("✓ Code Model Generated")

    print(f"Project   : {code_model.project_name}")
    print(f"Files     : {len(code_model.source_files)}")
    print(f"Modules   : {len(code_model.modules)}")
    print(f"Classes   : {len(code_model.classes)}")
    print(f"Functions : {len(code_model.functions)}")

    #
    # Dependency Analysis
    #
    print("\nRunning Dependency Analysis...")

    dependency_service = DependencyAnalysisService()

    dependency_service.analyze_project(project_path)

    dependency_report = DependencyReport(
        dependency_service
    )

    print()

    dependency_report.print_report()

    #
    # Relationship Query Engine
    #
    print("\nRunning Relationship Query Engine...")

    query_service = RelationshipQueryService(
        dependency_service.relationship_repository
    )

    query_report = RelationshipQueryReport(
        query_service
    )

    print()

    query_report.print_report()

    #
    # Graph Traversal Engine
    #
    print("\nRunning Graph Traversal Engine...")

    traversal_service = GraphTraversalService(
        dependency_service.relationship_repository
    )

    traversal_report = GraphTraversalReport(
        traversal_service
    )

    print()

    traversal_report.print_report()

    #
    # Impact Analysis Engine
    #
    print("\nRunning Impact Analysis Engine...")

    impact_service = ImpactAnalysisService(
        traversal_service
    )

    impact_report = ImpactAnalysisReport(
        impact_service
    )

    print()

    impact_report.print_report()

    #
    # Class Dependency Analysis
    #
    print("\nRunning Class Dependency Analysis...")

    class_service = ClassDependencyAnalysisService()

    class_service.analyze_project(project_path)

    class_report = ClassDependencyReport(
        class_service
    )

    print()

    class_report.print_report()

    print("\n✓ IC-03 analysis completed successfully.")


if __name__ == "__main__":
    main()
