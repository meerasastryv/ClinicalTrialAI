from .base_visitor import BaseVisitor


class FunctionVisitor(BaseVisitor):

    def __init__(self):
        super().__init__()

        self.functions = []
