from pathlib import Path

from src.ic03.services.project_analysis_service import ProjectAnalysisService
from src.ic03.services.dependency_analysis_service import DependencyAnalysisService
from src.ic03.reports.dependency_report import DependencyReport


def main():
    print("=" * 70)
    print("           IC-03 Code Intelligence Engine")
    print("=" * 70)

    project_path = Path(".")

    #
    # Build Code Model
    #
    print("\nBuilding Code Model...")

    project_service = ProjectAnalysisService()

    code_model = project_service.analyze(project_path)

    print("✓ Code Model Generated")

    print(f"Project : {code_model.project_name}")
    print(f"Files   : {len(code_model.source_files)}")
    print(f"Modules : {len(code_model.modules)}")
    print(f"Classes : {len(code_model.classes)}")
    print(f"Functions : {len(code_model.functions)}")

    #
    # Dependency Analysis
    #
    print("\nRunning Dependency Analysis...")

    dependency_service = DependencyAnalysisService()

    dependency_service.analyze_project(project_path)

    report = DependencyReport(dependency_service)

    print()

    report.print_report()

    print("\n✓ IC-03 analysis completed successfully.")


if __name__ == "__main__":
    main()
