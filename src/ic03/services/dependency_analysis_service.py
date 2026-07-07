import ast
from pathlib import Path
from collections import Counter

from src.ic03.builders.dependency_builder import DependencyBuilder
from src.ic03.repository.dependency_repository import DependencyRepository
from src.ic03.visitors.class_visitor import ClassVisitor
from src.ic03.analyzers.inheritance_builder import InheritanceBuilder


class DependencyAnalysisService:
    """
    Service responsible for analyzing dependencies in Python source files.
    """

    def __init__(self):
        self.repository = DependencyRepository()
        self.builder = DependencyBuilder(self.repository)

        self.inheritance_builder = InheritanceBuilder()
        self.classes = []

    def analyze_file(self, source_file: Path):
        """
        Analyze import dependencies in a Python source file.
        """
        self.builder.build(source_file)

    def analyze_classes(self, source_file: Path):
        """
        Analyze class definitions in a Python source file.
        """

        with open(source_file, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read())

        visitor = ClassVisitor()
        visitor.visit(tree)

        self.classes.extend(visitor.get_classes())

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
            self.analyze_classes(python_file)

        # Build inheritance hierarchy after all classes are collected
        self.inheritance_builder.build(self.classes)

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

    def get_classes(self):
        """
        Return all discovered classes.
        """
        return self.classes

    def get_inheritance_hierarchy(self):
        """
        Return the inheritance hierarchy.
        """
        return self.inheritance_builder.get_hierarchy()

    def get_children(self, parent_name):
        """
        Return all child classes of a parent.
        """
        return self.inheritance_builder.get_children(parent_name)

    def clear(self):
        """
        Clear all collected analysis results.
        """
        self.repository.clear()

        self.classes.clear()

        self.inheritance_builder.parent_to_children.clear()
        self.inheritance_builder.child_to_parents.clear()
