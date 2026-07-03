
from pathlib import Path
from collections import Counter
from src.ic03.builders.dependency_builder import DependencyBuilder
from src.ic03.repositories.dependency_repository import DependencyRepository


class DependencyAnalysisService:
    """
    Service responsible for analyzing dependencies in Python source files.
    """

    def __init__(self):
        self.repository = DependencyRepository()
        self.builder = DependencyBuilder(self.repository)

    def analyze_file(self, source_file: Path):
        """
        Analyze a single Python source file.
        """
        self.builder.build(source_file)

    def analyze_project(self, project_path: Path):
        """
        Analyze every Python source file in a project.
        """

        self.clear()

        for python_file in project_path.rglob("*.py"):

            # Skip cache folders
            if "__pycache__" in python_file.parts:
                continue

            self.analyze_file(python_file)

    def get_dependencies(self):
        """
        Return all discovered dependencies.
        """
        return self.repository.get_all_dependencies()
    def get_total_dependencies(self) -> int:
        """
        Return the total number of discovered dependencies.
        """
        return len(self.repository.get_all_dependencies())

    def get_import_statistics(self) -> Counter:
        """
        Return import frequency statistics.
        """
        counter = Counter()

        for dependency in self.repository.get_all_dependencies():
            counter[dependency.target] += 1

        return counter

    def get_top_imports(self, top_n: int = 10):
        """
        Return the most frequently imported modules.
        """
        return self.get_import_statistics().most_common(top_n)



    def clear(self):
        """
        Clear all collected dependencies.
        """
        self.repository.clear()
