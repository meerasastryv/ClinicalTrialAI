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

        print("=" * 70)
        print("               Dependency Analysis Report")
        print("=" * 70)

        print(f"Total Dependencies : {self.service.get_total_dependencies()}")
        print(f"Classes Found      : {len(self.service.get_classes())}")

        print()

        print("Top Imported Modules")
        print("-" * 70)

        for module, count in self.service.get_top_imports():
            print(f"{module:<40} {count}")

        print()

        print("Inheritance Hierarchy")
        print("-" * 70)

        hierarchy = self.service.get_inheritance_hierarchy()

        if hierarchy:

            for parent in sorted(hierarchy):

                print(parent)

                for child in sorted(hierarchy[parent]):
                    print(f"   └── {child}")

        else:
            print("No inheritance relationships found.")

        print()

        print("Summary")
        print("-" * 70)

        print(f"Dependencies           : {self.service.get_total_dependencies()}")
        print(f"Classes               : {len(self.service.get_classes())}")
        print(f"Inheritance Roots     : {len(hierarchy)}")

        print("=" * 70)
