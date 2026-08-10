from dataclasses import dataclass


@dataclass
class Dependency:
    """
    Represents a dependency between two Python modules.
    """

    source: str

    target: str

    dependency_type: str
