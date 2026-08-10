import ast

from src.ic03.models.dependency import Dependency
from src.ic03.models.dependency_type import DependencyType
from .base_visitor import BaseVisitor


class ImportVisitor(BaseVisitor):
    """
    Visits Python import statements and extracts dependency information.
    """

    def __init__(self, source_file: str):
        super().__init__()

        self.source_file = source_file

        # Keep both representations:
        # - imports: unique module names
        # - dependencies: rich dependency objects
        self.imports: set[str] = set()
        self.dependencies: list[Dependency] = []

    def visit_Import(self, node: ast.Import):
        """
        Handles statements such as:

            import os
            import json
            import numpy as np
        """

        for alias in node.names:
            module_name = alias.name

            self.imports.add(module_name)

            dependency = Dependency(
                source=self.source_file,
                target=module_name,
                dependency_type=DependencyType.IMPORT.value
            )

            self.dependencies.append(dependency)

        self.generic_visit(node)

    def visit_ImportFrom(self, node: ast.ImportFrom):
        """
        Handles statements such as:

            from pathlib import Path
            from src.ic03.models import Dependency
        """

        if node.module is None:
            self.generic_visit(node)
            return

        module_name = node.module

        self.imports.add(module_name)

        dependency = Dependency(
            source=self.source_file,
            target=module_name,
            dependency_type=DependencyType.IMPORT.value
        )

        self.dependencies.append(dependency)

        self.generic_visit(node)

    def get_imports(self) -> list[str]:
        """
        Returns all imported module names.
        """
        return sorted(self.imports)

    def get_dependencies(self) -> list[Dependency]:
        """
        Returns all discovered dependency objects.
        """
        return self.dependencies
