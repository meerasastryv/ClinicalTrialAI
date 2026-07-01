from dataclasses import dataclass, field
from models.method_model import MethodModel
@dataclass
class ClassModel:
    name: str

    base_classes: list = field(default_factory=list)
    # methods: list = field(default_factory=list)
    methods: list[MethodModel] = field(default_factory=list)
    docstring: str = ""
