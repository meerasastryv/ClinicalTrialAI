class DependencyReport:
    """
    Generates a formatted dependency analysis report.
    """

    def __init__(self, dependency_service):
        self.service = dependency_service

    def print_report(self):
        """
        Print dependency statistics.
        """

        print("=" * 60)
        print("        Dependency Analysis Report")
        print("=" * 60)

        print(f"Total Dependencies : {self.service.get_total_dependencies()}")

        print()
        print("Top Imported Modules")
        print("-" * 60)

        for module, count in self.service.get_top_imports():
            print(f"{module:<35} {count}")

        print("=" * 60)
