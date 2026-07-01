from visitors.base_visitor import BaseVisitor


class CallGraphVisitor(BaseVisitor):

    def __init__(self):
        super().__init__()

        self.calls = []
