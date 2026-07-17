"""
IC-07 Masking Rule Model

Defines rules used to mask sensitive test data.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List, Optional


@dataclass
class MaskingRule:
    """
    Represents a data masking rule.
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
    # Masking Configuration
    # ------------------------------------------------------------------

    masking_strategy: str = "full"

    mask_character: str = "*"

    visible_prefix: int = 0

    visible_suffix: int = 0

    replacement_value: Optional[Any] = None

    preserve_length: bool = True

    enabled: bool = True

    # ------------------------------------------------------------------
    # Classification
    # ------------------------------------------------------------------

    sensitive_level: str = "Confidential"

    applies_to: List[str] = field(default_factory=list)

    tags: List[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Utility Methods
    # ------------------------------------------------------------------

    def add_target(self, target: str) -> None:
        """Add an applicable dataset or entity."""
        if target not in self.applies_to:
            self.applies_to.append(target)

    def add_tag(self, tag: str) -> None:
        """Add a classification tag."""
        if tag not in self.tags:
            self.tags.append(tag)

    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MaskingRule":
        """Create model from dictionary."""
        return cls(**data)
