from ..models.function_model import FunctionModel


class FunctionBuilder:
    """
    Builds FunctionModel objects from visitor output.
    """

    def build_function(self, function_data: dict) -> FunctionModel:
        return FunctionModel(
            name=function_data["name"],
            parameters=function_data["parameters"],
            decorators=function_data["decorators"],
            line_number=function_data["line_number"],
            docstring=function_data["docstring"],
        )



