import ast

from .base_visitor import BaseVisitor
from ..models.dependency import Dependency
from ..models.dependency_type import DependencyType


class ClassDependencyVisitor(BaseVisitor):
    """
    Detects class dependencies created through object instantiation.
    """

    def __init__(self):
        super().__init__()
        self.current_class = None
        self.dependencies = []

    def visit_ClassDef(self, node: ast.ClassDef):
        """
        Tracks the class currently being visited.
        """
        previous_class = self.current_class
        self.current_class = node.name

        self.generic_visit(node)

        self.current_class = previous_class

    def visit_Call(self, node: ast.Call):
        """
        Detect constructor calls inside a class while ignoring
        Python built-in functions.
        """

        if self.current_class is not None:

            if isinstance(node.func, ast.Name):

                ignored = {
                    "print",
                    "len",
                    "str",
                    "int",
                    "float",
                    "bool",
                    "list",
                    "dict",
                    "set",
                    "tuple",
                    "open",
                    "range",
                    "enumerate",
                    "zip",
                    "sorted",
                    "sum",
                    "min",
                    "max",
                    "abs",
                    "type",
                    "super",
                    "isinstance",
                    "issubclass",
                    "field",
                }

                if node.func.id not in ignored:

                    dependency = Dependency(
                        source=self.current_class,
                        target=node.func.id,
                        dependency_type=DependencyType.CLASS_DEPENDENCY.value,
                    )

                    self.dependencies.append(dependency)

        self.generic_visit(node)

    def get_dependencies(self):
        """
        Returns all discovered class dependencies.
        """
        return self.dependencies
