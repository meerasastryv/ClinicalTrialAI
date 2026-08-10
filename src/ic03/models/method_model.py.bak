from dataclasses import dataclass, field


@dataclass
class MethodModel:
    name: str

    parameters: list[str] = field(default_factory=list)
    decorators: list[str] = field(default_factory=list)

    line_number: int = 0

    docstring: str = ""
