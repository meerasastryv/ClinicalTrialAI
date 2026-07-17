"""
IC-07 Test Data Model

Represents a single test data record used by the
Test Data Intelligence Engine.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any, Dict, List, Optional


@dataclass
class TestData:
    """
    Represents a single test data record.
    """

    # ------------------------------------------------------------------
    # Identification
    # ------------------------------------------------------------------

    data_id: str
    name: str
    description: str = ""

    # ------------------------------------------------------------------
    # Dataset Information
    # ------------------------------------------------------------------

    dataset_name: str = ""
    source: str = ""
    environment: str = ""

    # ------------------------------------------------------------------
    # Data Values
    # ------------------------------------------------------------------

    values: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Classification
    # ------------------------------------------------------------------

    category: str = "General"

    tags: List[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Security
    # ------------------------------------------------------------------

    contains_sensitive_data: bool = False

    masking_required: bool = False

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    is_valid: bool = True

    validation_errors: List[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    created_by: str = "System"

    created_at: datetime = field(default_factory=datetime.utcnow)

    updated_at: Optional[datetime] = None

    version: str = "1.0"

    # ------------------------------------------------------------------
    # Utility Methods
    # ------------------------------------------------------------------

    def add_value(self, field_name: str, value: Any) -> None:
        """
        Add or update a field value.
        """
        self.values[field_name] = value

    def get_value(self, field_name: str) -> Any:
        """
        Retrieve a field value.
        """
        return self.values.get(field_name)

    def remove_value(self, field_name: str) -> None:
        """
        Remove a field if it exists.
        """
        self.values.pop(field_name, None)

    def add_tag(self, tag: str) -> None:
        """
        Add a tag if not already present.
        """
        if tag not in self.tags:
            self.tags.append(tag)

    def add_validation_error(self, message: str) -> None:
        """
        Record a validation error.
        """
        self.validation_errors.append(message)
        self.is_valid = False

    def clear_validation_errors(self) -> None:
        """
        Clear validation state.
        """
        self.validation_errors.clear()
        self.is_valid = True

    def to_dict(self) -> Dict[str, Any]:
        """
        Convert model to dictionary.
        """
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "TestData":
        """
        Create TestData from a dictionary.
        """
        return cls(**data)
