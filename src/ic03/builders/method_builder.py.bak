from ..models.method_model import MethodModel

class MethodBuilder:
    """
    Builds MethodModel objects from visitor output.
    """

    def build_method(self, method_data: dict) -> MethodModel:
        """
        Convert visitor output into a MethodModel.
        """

        return MethodModel(
            name=method_data["name"],
            parameters=method_data["parameters"],
            decorators=method_data["decorators"],
            line_number=method_data["line_number"],
            docstring=method_data["docstring"],
        )
