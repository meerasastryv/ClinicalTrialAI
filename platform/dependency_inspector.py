import ast
from pathlib import Path
from typing import List

from platform.module_info import ModuleInfo
from platform.project_scanner import ProjectScanner


class DependencyInspector:
    """
    Performs project discovery and AST inspection.
    """

    def __init__(self):
        self.scanner = ProjectScanner()

    def scan(self) -> List[ModuleInfo]:

        modules = self.scanner.discover_python_modules()

        for module in modules:
            self.inspect_module(module)

        return modules
    """
    def inspect_module(self, module: ModuleInfo):

        path = Path(module.module_path)

        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))

        except Exception:
            return

        for node in ast.walk(tree):

            if isinstance(node, ast.Import):

                for alias in node.names:
                    module.imports.append(alias.name)

            elif isinstance(node, ast.ImportFrom):

                if node.module:
                    module.imports.append(node.module)

            elif isinstance(node, ast.ClassDef):

                module.classes.append(node.name)

            elif isinstance(node, ast.FunctionDef):

                module.functions.append(node.name)
    """
    def inspect_module(self, module: ModuleInfo):
        path = Path(module.module_path)
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except Exception:
            return
        for node in tree.body:
            if isinstance(node, ast.Import):
                for alias in node.names:
                    module.imports.append(alias.name)
            elif isinstance(node, ast.ImportFrom):
                if node.module:
                    module.imports.append(node.module)
            elif isinstance(node, ast.ClassDef):
                module.classes.append(node.name)
                for item in node.body:
                    if isinstance(item, ast.FunctionDef):
                        module.methods.append(item.name)
            elif isinstance(node, ast.FunctionDef):
                module.functions.append(node.name)
