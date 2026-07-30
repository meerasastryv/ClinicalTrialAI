from typing import Dict, List, Optional

from platform.module_info import ModuleInfo


class DependencyResolver:
    """
    Resolves imports to project modules.
    """

    def __init__(self, modules: List[ModuleInfo]):

        self.modules = modules

        self.module_lookup: Dict[str, ModuleInfo] = {}

        self.full_lookup: Dict[str, ModuleInfo] = {}

        self._build_lookup()

    def _build_lookup(self):

        for module in self.modules:

            key = module.module_name

            self.module_lookup[key] = module

            full_name = f"{module.ic_name}.{module.module_type}.{module.module_name}"

            self.full_lookup[full_name] = module

    def resolve(self, import_name: str) -> Optional[ModuleInfo]:

        last = import_name.split(".")[-1]

        return self.module_lookup.get(last)

    def is_internal(self, import_name: str) -> bool:

        return self.resolve(import_name) is not None
