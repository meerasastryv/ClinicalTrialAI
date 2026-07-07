import ast

from .base_visitor import BaseVisitor
from ..models.dependency import Dependency
from ..models.dependency_type import DependencyType


class InheritanceVisitor(BaseVisitor):
    """
    Discovers inheritance relationships between classes.

    Example:
        class Dog(Animal):
            ...

    Produces:
        Dog ----INHERITANCE----> Animal
    """

    def __init__(self):
        super().__init__()

        self.inheritance = []

    def visit_ClassDef(self, node: ast.ClassDef):
        """
        Visit every class definition and capture
        inheritance relationships.
        """

        child_class = node.name

        for base in node.bases:

            #
            # class A(B)
            #
            if isinstance(base, ast.Name):

                parent_class = base.id

                dependency = Dependency(
                    source=child_class,
                    target=parent_class,
                    dependency_type=DependencyType.INHERITANCE.value,
                )

                self.inheritance.append(dependency)

            #
            # class A(module.B)
            #
            elif isinstance(base, ast.Attribute):

                parent_class = base.attr

                dependency = Dependency(
                    source=child_class,
                    target=parent_class,
                    dependency_type=DependencyType.INHERITANCE.value,
                )

                self.inheritance.append(dependency)

        self.generic_visit(node)

    def get_inheritance(self):
        """
        Returns all inheritance relationships.
        """

        return self.inheritance
