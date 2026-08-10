"""
IC-07 Data Field Model

Represents metadata about a single field in a dataset.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional


@dataclass
class DataField:
    """
    Represents a field within a dataset.
    """

    # ------------------------------------------------------------------
    # Identification
    # ------------------------------------------------------------------

    field_name: str

    display_name: str = ""

    description: str = ""

    # ------------------------------------------------------------------
    # Data Definition
    # ------------------------------------------------------------------

    data_type: str = "string"

    length: Optional[int] = None

    precision: Optional[int] = None

    scale: Optional[int] = None

    nullable: bool = True

    default_value: Any = None

    # ------------------------------------------------------------------
    # Constraints
    # ------------------------------------------------------------------

    required: bool = False

    unique: bool = False

    primary_key: bool = False

    foreign_key: bool = False

    allowed_values: List[Any] = field(default_factory=list)

    validation_pattern: str = ""

    minimum_value: Any = None

    maximum_value: Any = None

    # ------------------------------------------------------------------
    # Security
    # ------------------------------------------------------------------

    sensitive: bool = False

    masking_rule: Optional[str] = None

    encrypted: bool = False

    # ------------------------------------------------------------------
    # Classification
    # ------------------------------------------------------------------

    category: str = "General"

    tags: List[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Utility Methods
    # ------------------------------------------------------------------

    def add_allowed_value(self, value: Any) -> None:
        """Add an allowed value."""
        if value not in self.allowed_values:
            self.allowed_values.append(value)

    def add_tag(self, tag: str) -> None:
        """Add a classification tag."""
        if tag not in self.tags:
            self.tags.append(tag)

    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "DataField":
        """Create model from dictionary."""
        return cls(**data)
