from collections import Counter

from ..services.class_dependency_analysis_service import (
    ClassDependencyAnalysisService,
)


class ClassDependencyReport:
    """
    Prints a summary of class dependencies.
    """

    def __init__(self, service: ClassDependencyAnalysisService):

        self.service = service

    def print_report(self):

        print("=" * 70)
        print("          Class Dependency Report")
        print("=" * 70)

        dependencies = self.service.get_dependencies()

        print(f"\nTotal Class Dependencies : {len(dependencies)}")

        counter = Counter()

        for dependency in dependencies:
            counter[dependency.target] += 1

        print("\nMost Used Classes")
        print("-" * 70)

        for cls, count in counter.most_common(10):
            print(f"{cls:<35} {count}")

        print("=" * 70)
