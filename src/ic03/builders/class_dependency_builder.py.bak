from pathlib import Path

from ..repository.dependency_repository import DependencyRepository
from ..parsers.python_ast_parser import PythonASTParser
from ..visitors.class_dependency_visitor import ClassDependencyVisitor


class ClassDependencyBuilder:
    """
    Builds class dependency models for a source file.
    """

    def __init__(self, repository: DependencyRepository):

        self.repository = repository
        self.parser = PythonASTParser()

    def build(self, source_file: Path):

        tree = self.parser.parse(source_file)

        visitor = ClassDependencyVisitor()

        visitor.visit(tree)

        for dependency in visitor.get_dependencies():
            self.repository.add_dependency(dependency)
