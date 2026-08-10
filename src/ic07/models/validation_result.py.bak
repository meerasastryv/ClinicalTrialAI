"""
IC-07 Validation Result Model

Represents the outcome of validating test data,
datasets, or generated records.
"""

from __future__ import annotations

from dataclasses import dataclass, field, asdict
from datetime import datetime
from typing import Any, Dict, List


@dataclass
class ValidationResult:
    """
    Represents the result of a validation operation.
    """

    # ------------------------------------------------------------------
    # Identification
    # ------------------------------------------------------------------

    validation_id: str

    target_id: str

    target_type: str = "record"

    # ------------------------------------------------------------------
    # Validation Status
    # ------------------------------------------------------------------

    is_valid: bool = True

    validation_score: float = 100.0

    # ------------------------------------------------------------------
    # Validation Messages
    # ------------------------------------------------------------------

    errors: List[str] = field(default_factory=list)

    warnings: List[str] = field(default_factory=list)

    information: List[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    rules_checked: int = 0

    rules_passed: int = 0

    rules_failed: int = 0

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    validated_by: str = "System"

    validated_at: datetime = field(default_factory=datetime.utcnow)

    execution_time_ms: float = 0.0

    additional_metrics: Dict[str, Any] = field(default_factory=dict)

    # ------------------------------------------------------------------
    # Utility Methods
    # ------------------------------------------------------------------

    def add_error(self, message: str) -> None:
        """Add a validation error."""
        self.errors.append(message)
        self.is_valid = False

    def add_warning(self, message: str) -> None:
        """Add a validation warning."""
        self.warnings.append(message)

    def add_information(self, message: str) -> None:
        """Add an informational message."""
        self.information.append(message)

    def add_metric(self, name: str, value: Any) -> None:
        """Add an additional validation metric."""
        self.additional_metrics[name] = value

    def calculate_score(self) -> float:
        """
        Calculate the validation score based on
        executed validation rules.
        """

        if self.rules_checked == 0:
            self.validation_score = 100.0
        else:
            self.validation_score = (
                self.rules_passed / self.rules_checked
            ) * 100

        return self.validation_score

    def to_dict(self) -> Dict[str, Any]:
        """Convert model to dictionary."""
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "ValidationResult":
        """Create model from dictionary."""
        return cls(**data)
