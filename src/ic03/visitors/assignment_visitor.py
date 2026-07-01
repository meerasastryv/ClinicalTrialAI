from visitors.base_visitor import BaseVisitor


class AssignmentVisitor(BaseVisitor):

    def __init__(self):
        super().__init__()

        self.assignments = []
