
from src.ic03.models.module_model import ModuleModel


class ModuleBuilder:
    """
    Builds a ModuleModel from parsed module information.
    """

    def build_module(
        self,
        name,
        imports,
        classes,
        functions,
        path="",
        language="Python",
    ):
        return ModuleModel(
            name=name,
            imports=imports,
            classes=classes,
            functions=functions,
            path=path,
            language=language,
        )
