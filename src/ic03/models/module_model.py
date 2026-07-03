
from dataclasses import dataclass, field

from .class_model import ClassModel
from .function_model import FunctionModel

@dataclass
class ModuleModel:
    name: str

    imports: list = field(default_factory=list)

    classes: list[ClassModel] = field(default_factory=list)

    functions: list[FunctionModel] = field(default_factory=list)

    path: str = ""

    language: str = "Python"
