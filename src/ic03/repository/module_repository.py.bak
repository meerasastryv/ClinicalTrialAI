from ..models.module_model import ModuleModel


class ModuleRepository:

    def __init__(self):
        self.modules = []

    def add(self, module: ModuleModel):
        self.modules.append(module)

    def get_all(self):
        return self.modules

    def find_by_name(self, name):
        for module in self.modules:
            if module.name == name:
                return module
        return None
