import ast


class BaseVisitor(ast.NodeVisitor):
    """
    Base class for all AST visitors.
    """

    def __init__(self):
        super().__init__()
