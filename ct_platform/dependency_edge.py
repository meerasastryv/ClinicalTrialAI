from dataclasses import dataclass


@dataclass
class DependencyEdge:
    """
    Represents a dependency relationship.
    """

    source: str
    target: str
