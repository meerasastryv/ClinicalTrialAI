"""
IC-07 Generation Rule Model

Defines rules used for synthetic and constraint-based
test data generation.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional


@dataclass
class GenerationRule:
    """
    Represents a rule for generating test data.
    """

    # ------------------------------------------------------------------
    # Identification
    # ------------------------------------------------------------------

    rule_id: str

    name: str

    description: str = ""

    # ------------------------------------------------------------------
    # Target Information
    # ------------------------------------------------------------------

    field_name: str = ""

    data_type: str = "string"

    # ------------------------------------------------------------------
    # Generation Rules
    # ------------------------------------------------------------------

    strategy: str = "random"

    minimum_value: Optional[Any] = None

    maximum_value: Optional[Any] = None

    allowed_values: List[Any] = field(default_factory=list)

    default_value: Optional[Any] = None

    pattern: str = ""

    nullable: bool = True

    unique: bool = False

    # ------------------------------------------------------------------
    # AI Configuration
    # ------------------------------------------------------------------

    use_ai_generation: bool = False

    prompt_template: str = ""

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    enabled: bool = True

    priority: int = 1

    tags: List[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Utility Methods
    # ------------------------------------------------------------------

    def add_allowed_value(self, value: Any) -> None:
        """Add an allowed value."""
        if value not in self.allowed_values:
            self.allowed_values.append(value)

    def add_tag(self, tag: str) -> None:
        """Add a tag."""
        if tag not in self.tags:
            self.tags.append(tag)

    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "GenerationRule":
        """Create model from dictionary."""
        return cls(**data)
