"""
Validation rule model.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ValidationRule:
    """
    Represents a validation rule for a dataset.
    """

    name: str
    description: str
    rule_type: str

    column: str | None = None

    required: bool = False

    minimum: float | int | None = None

    maximum: float | int | None = None

    pattern: str | None = None

    allowed_values: list[Any] = field(default_factory=list)

    length: int | None = None

    custom_function: Any = None
