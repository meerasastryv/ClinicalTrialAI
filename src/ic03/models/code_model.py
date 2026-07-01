from dataclasses import dataclass, field

@dataclass
class CodeModel:

    project_name: str

    source_files: list = field(default_factory=list)

    modules: list = field(default_factory=list)

    classes: list = field(default_factory=list)

    functions: list = field(default_factory=list)
