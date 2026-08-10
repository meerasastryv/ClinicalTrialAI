"""
Dependency Edge Model

Represents a dependency relationship between two architecture components.
"""


class DependencyEdge:
    """
    Represents a dependency edge in the architecture graph.

    Example:
        Controller --> Service
        Service --> Repository
    """

    def __init__(
        self,
        source,
        target,
        dependency_type="uses"
    ):
        self.source = source
        self.target = target
        self.dependency_type = dependency_type

    def to_dict(self):
        """Convert object to dictionary."""

        return {
            "source": self.source,
            "target": self.target,
            "dependency_type": self.dependency_type
        }

    def __str__(self):
        return (
            f"{self.source} --> {self.target} "
            f"({self.dependency_type})"
        )

    def __repr__(self):
        return self.__str__()
