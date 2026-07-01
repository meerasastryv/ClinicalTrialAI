from dataclasses import dataclass, field

@dataclass
class ModuleModel:
    name: str
    path: str

    imports: list = field(default_factory=list)
    classes: list = field(default_factory=list)
    functions: list = field(default_factory=list)

    docstring: str = ""
