from pathlib import Path

from platform.config.configuration_loader import ConfigurationLoader
from platform.config.environment import Environment
from platform.discovery.project_discovery import ProjectDiscovery


def main() -> None:
    project_root = Path(".")

    print("=" * 60)
    print("ClinicalTrialAI - PF-01 Platform Validation")
    print("=" * 60)

    # Load configuration
    loader = ConfigurationLoader()
    config = loader.load(
        project_root=project_root,
        environment=Environment.DEVELOPMENT,
    )

    print(f"Platform: {config.platform_name}")
    print(f"Version : {config.platform_version}")
    print(f"Project : {config.project_root}")
    print()

    # Run discovery
    discovery = ProjectDiscovery()
    result = discovery.discover(project_root)

    print("Discovery Results")
    print("-----------------")
    print(f"Packages            : {result.total_packages}")
    print(f"Modules             : {result.total_modules}")
    print(f"Python Files        : {result.total_python_files}")
    print(f"Configuration Files : {result.total_configuration_files}")
    print(f"Total Files         : {result.total_files}")
    print()

    print("First 10 Packages")
    for package in result.packages[:10]:
        print(f"  {package}")

    print()

    print("First 10 Modules")
    for module in result.modules[:10]:
        print(f"  {module}")

    print()
    print("PF-01 validation completed successfully.")


if __name__ == "__main__":
    main()
