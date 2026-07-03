from dataclasses import dataclass


@dataclass
class Dependency:
    """
    Represents a dependency between two software entities.
    """

    source: str
    target: str
    dependency_type: str
