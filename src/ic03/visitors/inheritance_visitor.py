from visitors.base_visitor import BaseVisitor


class InheritanceVisitor(BaseVisitor):

    def __init__(self):
        super().__init__()

        self.inheritance = []
