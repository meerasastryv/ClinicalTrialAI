from .base_visitor import BaseVisitor


class DependencyVisitor(BaseVisitor):

    def __init__(self):
        super().__init__()

        self.dependencies = []
