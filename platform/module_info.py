from dataclasses import dataclass, field
from typing import List


@dataclass
class ModuleInfo:
    """
    Represents a discovered Python module.
    """

    ic_name: str
    module_name: str
    module_path: str
    module_type: str

    imports: List[str] = field(default_factory=list)
    classes: List[str] = field(default_factory=list)
    functions: List[str] = field(default_factory=list)
    methods: List[str] = field(default_factory=list)
    def __str__(self) -> str:
        return (
            f"{self.ic_name} | "
            f"{self.module_type} | "
            f"{self.module_name}"
        )
