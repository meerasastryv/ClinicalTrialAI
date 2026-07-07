from ..models.class_model import ClassModel


class ClassBuilder:
    """
    Builds ClassModel objects from visitor output.
    """

    def build_class(self, class_data: ClassModel) -> ClassModel:
        """
        Return the ClassModel produced by the visitor.
        """

        return class_data
