import ast

from .base_visitor import BaseVisitor


class ClassVisitor(BaseVisitor):
    """
    Visits Python class definitions.
    """

    def __init__(self):
        super().__init__()

        self.classes = []

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

        class_info = {
            "name": node.name,
            "bases": base_classes,
            "line_number": node.lineno,
            "docstring": ast.get_docstring(node),
        }

        self.classes.append(class_info)

        self.generic_visit(node)
