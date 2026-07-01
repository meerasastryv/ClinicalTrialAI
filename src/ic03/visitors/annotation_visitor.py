from visitors.base_visitor import BaseVisitor


class AnnotationVisitor(BaseVisitor):

    def __init__(self):
        super().__init__()

        self.annotations = []
