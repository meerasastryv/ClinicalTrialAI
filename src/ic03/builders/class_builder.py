from ..models.class_model import ClassModel


class ClassBuilder:
    """
    Builds ClassModel objects from visitor output.
    """

    def build_class(self, class_data: dict) -> ClassModel:
        return ClassModel(
            name=class_data["name"],
            base_classes=class_data["bases"],
            line_number=class_data["line_number"],
            docstring=class_data["docstring"],
        )

