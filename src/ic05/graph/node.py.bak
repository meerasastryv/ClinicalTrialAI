from dataclasses import dataclass, field
from datetime import datetime
from typing import Any, Dict, List


@dataclass
class Node:
    """
    Represents a Knowledge Graph Node.
    """

    node_id: str
    node_type: str
    name: str

    source: str = "UNKNOWN"

    labels: List[str] = field(default_factory=list)

    tags: List[str] = field(default_factory=list)

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

    def add_label(
        self,
        label: str,
    ) -> None:

        if label not in self.labels:

            self.labels.append(label)

            self.update_timestamp()

    # ---------------------------------------------------------

    def remove_label(
        self,
        label: str,
    ) -> None:

        if label in self.labels:

            self.labels.remove(label)

            self.update_timestamp()

    # ---------------------------------------------------------

    def add_tag(
        self,
        tag: str,
    ) -> None:

        if tag not in self.tags:

            self.tags.append(tag)

            self.update_timestamp()

    # ---------------------------------------------------------

    def remove_tag(
        self,
        tag: str,
    ) -> None:

        if tag in self.tags:

            self.tags.remove(tag)

            self.update_timestamp()

    # ---------------------------------------------------------

    def update_timestamp(self):

        self.updated_at = datetime.now()

    # ---------------------------------------------------------

    def __str__(self):

        return (
            f"Node("
            f"id={self.node_id}, "
            f"type={self.node_type}, "
            f"name={self.name}, "
            f"source={self.source})"
        )
