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

from src.ic03.services.dependency_visualization_service import (
    DependencyVisualizationService,
)

from src.ic03.services.architecture_metrics_service import (
    ArchitectureMetricsService,
)
from src.ic03.reports.architecture_metrics_report import (
    ArchitectureMetricsReport,
)

from src.ic03.services.advanced_architecture_analysis_service import (
    AdvancedArchitectureAnalysisService,
)
from src.ic03.reports.advanced_architecture_report import (
    AdvancedArchitectureReport,
)

from src.ic03.services.code_intelligence_query_service import (
    CodeIntelligenceQueryService,
)
from src.ic03.reports.code_intelligence_query_report import (
    CodeIntelligenceQueryReport,
)

from src.ic03.services.ai_code_assistant_service import (
    AICodeAssistantService,
)
from src.ic03.reports.ai_code_assistant_report import (
    AICodeAssistantReport,
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

    relationship_query_service = RelationshipQueryService(
        dependency_service.relationship_repository
    )

    relationship_query_report = RelationshipQueryReport(
        relationship_query_service
    )

    print()

    relationship_query_report.print_report()

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
    # Dependency Visualization Engine
    #
    print("\nRunning Dependency Visualization Engine...")

    visualization_service = DependencyVisualizationService(
        dependency_service.relationship_repository
    )

    print()

    visualization_service.export_all()

    #
    # Architecture Metrics Engine
    #
    print("\nRunning Architecture Metrics Engine...")

    metrics_service = ArchitectureMetricsService(
        traversal_service
    )

    metrics_report = ArchitectureMetricsReport(
        metrics_service
    )

    print()

    metrics_report.print_report()

    #
    # Advanced Architecture Analysis Engine
    #
    print("\nRunning Advanced Architecture Analysis Engine...")

    advanced_service = AdvancedArchitectureAnalysisService(
        traversal_service
    )

    advanced_report = AdvancedArchitectureReport(
        advanced_service
    )

    print()

    advanced_report.print_report()

    #
    # Code Intelligence Query Engine
    #
    print("\nRunning Code Intelligence Query Engine...")

    code_query_service = CodeIntelligenceQueryService(
        relationship_query_service,
        traversal_service,
        impact_service,
        metrics_service,
        advanced_service,
    )

    code_query_report = CodeIntelligenceQueryReport(
        code_query_service
    )

    print()

    code_query_report.print_report()

    #
    # AI Code Assistant
    #
    print("\nRunning AI Code Assistant...")

    ai_assistant = AICodeAssistantService(
        code_query_service
    )

    ai_report = AICodeAssistantReport(
        ai_assistant
    )

    print()

    ai_report.print_report()

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
