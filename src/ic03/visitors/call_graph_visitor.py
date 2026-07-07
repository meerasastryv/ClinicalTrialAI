import ast

from .base_visitor import BaseVisitor
from ..models.dependency import Dependency
from ..models.dependency_type import DependencyType


class CallGraphVisitor(BaseVisitor):
    """
    Builds a method call graph.

    Example:

        class OrderService:

            def process(self):
                self.validate()
                self.save()

            def validate(self):
                ...

            def save(self):
                ...

    Produces

        OrderService.process  ---> OrderService.validate
        OrderService.process  ---> OrderService.save
    """

    def __init__(self):
        super().__init__()

        self.current_class = None
        self.current_method = None

        self.calls = []

    def visit_ClassDef(self, node):

        previous = self.current_class
        self.current_class = node.name

        self.generic_visit(node)

        self.current_class = previous

    def visit_FunctionDef(self, node):

        previous = self.current_method
        self.current_method = node.name

        self.generic_visit(node)

        self.current_method = previous

    def visit_Call(self, node):

        if self.current_method:

            caller = self.current_method

            if self.current_class:
                caller = f"{self.current_class}.{caller}"

            #
            # self.method()
            #
            if isinstance(node.func, ast.Attribute):

                callee = node.func.attr

                if self.current_class:
                    callee = f"{self.current_class}.{callee}"

                self.calls.append(
                    Dependency(
                        source=caller,
                        target=callee,
                        dependency_type=DependencyType.METHOD_CALL.value,
                    )
                )

            #
            # function()
            #
            elif isinstance(node.func, ast.Name):

                self.calls.append(
                    Dependency(
                        source=caller,
                        target=node.func.id,
                        dependency_type=DependencyType.METHOD_CALL.value,
                    )
                )

        self.generic_visit(node)

    def get_calls(self):
        return self.calls
