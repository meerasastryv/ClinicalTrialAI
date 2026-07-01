
import ast

from visitors.base_visitor import BaseVisitor


class MethodVisitor(BaseVisitor):
    """
    Visits methods inside classes.
    """

    def __init__(self):
        super().__init__()

        self.methods = {}

    def visit_ClassDef(self, node: ast.ClassDef):

        class_methods = []

        for item in node.body:

            if isinstance(item, ast.FunctionDef):

                class_methods.append({

                    "name": item.name,

                    "parameters": [
                        arg.arg
                        for arg in item.args.args
                    ],

                    "decorators": [
                        ast.unparse(d)
                        if hasattr(ast, "unparse")
                        else ""
                        for d in item.decorator_list
                    ],

                    "line_number": item.lineno,

                    "docstring": ast.get_docstring(item)

                })

        self.methods[node.name] = class_methods

        self.generic_visit(node)
