from dataclasses import dataclass


@dataclass
class DependencyNode:
    """
    Represents a module in the dependency graph.
    """

    id: str
    name: str
    module_type: str
    ic_name: str
