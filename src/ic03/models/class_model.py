
from dataclasses import dataclass, field
from .method_model import MethodModel


@dataclass
class ClassModel:
    name: str

    base_classes: list[str] = field(default_factory=list)
    methods: list[MethodModel] = field(default_factory=list)

    line_number: int = 0
    docstring: str = ""
