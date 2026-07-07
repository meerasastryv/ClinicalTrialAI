import ast
from pathlib import Path
from collections import Counter

from src.ic03.builders.dependency_builder import DependencyBuilder
from src.ic03.repository.dependency_repository import DependencyRepository

from src.ic03.visitors.class_visitor import ClassVisitor
from src.ic03.visitors.call_graph_visitor import CallGraphVisitor

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
        self.call_graph = []

    def analyze_file(self, source_file: Path):
        """
        Analyze import dependencies.
        """
        self.builder.build(source_file)

    def analyze_classes(self, source_file: Path):
        """
        Analyze class definitions.
        """

        with open(source_file, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read())

        visitor = ClassVisitor()
        visitor.visit(tree)

        self.classes.extend(visitor.get_classes())

    def analyze_call_graph(self, source_file: Path):
        """
        Analyze method/function calls.
        """

        with open(source_file, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read())

        visitor = CallGraphVisitor()
        visitor.visit(tree)

        self.call_graph.extend(visitor.get_calls())

    def analyze_project(self, project_path: Path):
        """
        Analyze every Python source file in a project.
        """

        self.clear()

        for python_file in project_path.rglob("*.py"):

            if "__pycache__" in python_file.parts:
                continue

            self.analyze_file(python_file)
            self.analyze_classes(python_file)
            self.analyze_call_graph(python_file)

        self.inheritance_builder.build(self.classes)

    def get_dependencies(self):
        return self.repository.get_all_dependencies()

    def get_total_dependencies(self):
        return len(self.repository.get_all_dependencies())

    def get_import_statistics(self):
        counter = Counter()

        for dependency in self.repository.get_all_dependencies():
            counter[dependency.target] += 1

        return counter

    def get_top_imports(self, top_n=10):
        return self.get_import_statistics().most_common(top_n)

    def get_classes(self):
        return self.classes

    def get_inheritance_hierarchy(self):
        return self.inheritance_builder.get_hierarchy()

    def get_children(self, parent_name):
        return self.inheritance_builder.get_children(parent_name)

    #
    # ---------- Call Graph ----------
    #

    def get_call_graph(self):
        """
        Return every discovered method call.
        """
        return self.call_graph

    def get_total_method_calls(self):
        """
        Return total method/function calls.
        """
        return len(self.call_graph)

    def get_calls_from(self, caller):
        """
        Return calls originating from a method.
        """
        return [
            call
            for call in self.call_graph
            if call.source == caller
        ]

    def get_calls_to(self, callee):
        """
        Return calls targeting a method.
        """
        return [
            call
            for call in self.call_graph
            if call.target == callee
        ]

    def clear(self):
        """
        Clear all collected analysis results.
        """

        self.repository.clear()

        self.classes.clear()
        self.call_graph.clear()

        self.inheritance_builder.parent_to_children.clear()
        self.inheritance_builder.child_to_parents.clear()
