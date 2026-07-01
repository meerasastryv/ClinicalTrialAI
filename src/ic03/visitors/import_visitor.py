import ast
from visitors.base_visitor import BaseVisitor

class ImportVisitor(BaseVisitor):
    """
    Visits import statements in a Python AST.
    """
    def __init__(self):
        super().__init__()
        # self.imports: list[str] = []
        self.imports: set[str] = set()
    def visit_Import(self, node: ast.Import):
        """
        Handles:
            import os
            import json
        """
        for alias in node.names:
            # self.imports.append(alias.name)
            self.imports.add(alias.name)
        self.generic_visit(node)
    def visit_ImportFrom(self, node: ast.ImportFrom):
        """
        Handles:
            from pathlib import Path
        """
        module = node.module or ""
        for alias in node.names:
            # self.imports.append(f"{module}.{alias.name}")
            self.imports.add(f"{module}.{alias.name}")
        self.generic_visit(node)
