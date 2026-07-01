
from models.module_model import ModuleModel


class ModuleBuilder:
    """
    Builds ModuleModel objects.
    """

    def build(self, name: str, path: str) -> ModuleModel:

        return ModuleModel(
            name=name,
            path=path,
        )
