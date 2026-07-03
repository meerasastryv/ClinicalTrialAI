from ..repository.class_repository import ClassRepository
from ..repository.function_repository import FunctionRepository
from ..repository.method_repository import MethodRepository


class SearchService:
    """
    Provides search operations across the parsed codebase.
    """

    def __init__(self):
        self.class_repository = ClassRepository()
        self.function_repository = FunctionRepository()
        self.method_repository = MethodRepository()

    def find_class(self, name):
        return self.class_repository.find_by_name(name)

    def get_functions(self):
        return self.function_repository.get_all()

    def get_methods(self):
        return self.method_repository.get_all()
