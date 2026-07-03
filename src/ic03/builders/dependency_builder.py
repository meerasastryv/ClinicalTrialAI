import ast
from pathlib import Path

from src.ic03.repositories.dependency_repository import DependencyRepository
from src.ic03.visitors.import_visitor import ImportVisitor


class DependencyBuilder:
    """
    Builds dependency information for a Python source file.
    """

    def __init__(self, repository: DependencyRepository):
        self.repository = repository

    def build(self, source_file: Path):
        """
        Analyze a Python source file and store discovered dependencies.
        """

        with open(source_file, "r", encoding="utf-8") as file:
            tree = ast.parse(file.read())

        visitor = ImportVisitor(str(source_file))
        visitor.visit(tree)

        for dependency in visitor.get_dependencies():
            self.repository.add_dependency(dependency)
