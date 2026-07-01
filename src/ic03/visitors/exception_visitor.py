from visitors.base_visitor import BaseVisitor


class ExceptionVisitor(BaseVisitor):

    def __init__(self):
        super().__init__()

        self.exceptions = []
