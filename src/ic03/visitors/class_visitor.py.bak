import ast

from .base_visitor import BaseVisitor
from src.ic03.models.class_model import ClassModel


class ClassVisitor(BaseVisitor):
    """
    Visits Python class definitions and builds ClassModel objects.
    """

    def __init__(self):
        super().__init__()
        self.classes: list[ClassModel] = []

    def visit_ClassDef(self, node: ast.ClassDef):
        """
        Extract information about a class.
        """

        base_classes = []

        for base in node.bases:

            if isinstance(base, ast.Name):
                base_classes.append(base.id)

            elif isinstance(base, ast.Attribute):
                base_classes.append(base.attr)

        class_model = ClassModel(
            name=node.name,
            base_classes=base_classes,
            line_number=node.lineno,
            docstring=ast.get_docstring(node) or "",
        )

        self.classes.append(class_model)

        self.generic_visit(node)

    def get_classes(self) -> list[ClassModel]:
        """
        Return all discovered classes.
        """
        return self.classes
