from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict


@dataclass
class Edge:
    """
    Represents a Knowledge Graph relationship.
    """

    source: str
    target: str
    relationship: str

    source_ic: str = "UNKNOWN"

    confidence: float = 1.0

    weight: float = 1.0

    properties: Dict[str, Any] = field(default_factory=dict)

    created_at: datetime = field(
        default_factory=datetime.now
    )

    updated_at: datetime = field(
        default_factory=datetime.now
    )

    # ---------------------------------------------------------

    def add_property(
        self,
        key: str,
        value: Any,
    ) -> None:

        self.properties[key] = value

        self.update_timestamp()

    # ---------------------------------------------------------

    def get_property(
        self,
        key: str,
        default=None,
    ):

        return self.properties.get(key, default)

    # ---------------------------------------------------------

    def update_timestamp(self):

        self.updated_at = datetime.now()

    # ---------------------------------------------------------

    def __str__(self):

        return (
            f"Edge("
            f"{self.source}"
            f" --{self.relationship}--> "
            f"{self.target}, "
            f"source_ic={self.source_ic}, "
            f"confidence={self.confidence:.2f}, "
            f"weight={self.weight:.2f})"
        )
