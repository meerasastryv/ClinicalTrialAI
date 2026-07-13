from dataclasses import dataclass, field
from typing import Dict, Any


@dataclass
class Edge:
    """
    Represents a relationship between two nodes.
    """

    source: str
    target: str
    relationship: str
    properties: Dict[str, Any] = field(default_factory=dict)

    def add_property(self, key: str, value: Any) -> None:
        self.properties[key] = value

    def get_property(self, key: str, default=None):
        return self.properties.get(key, default)

    def __str__(self) -> str:
        return (
            f"Edge("
            f"{self.source}"
            f" --{self.relationship}--> "
            f"{self.target})"
        )
