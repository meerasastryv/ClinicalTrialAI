from pathlib import Path

from ..builders.class_dependency_builder import ClassDependencyBuilder
from ..repositories.dependency_repository import DependencyRepository


class ClassDependencyAnalysisService:
    """
    Performs class dependency analysis on a file or project.
    """

    def __init__(self):

        self.repository = DependencyRepository()

        self.builder = ClassDependencyBuilder(self.repository)

    def analyze_file(self, source_file: Path):

        self.builder.build(source_file)

    def analyze_project(self, project_root: Path):

        for file in project_root.rglob("*.py"):

            self.builder.build(file)

    def get_dependencies(self):

        return self.repository.get_all_dependencies()

    def get_total_dependencies(self):

        return len(self.repository.get_all_dependencies())
