"""
Sensitive Field Model

Represents a detected sensitive field within a dataset.
"""

from dataclasses import dataclass


@dataclass
class SensitiveField:
    """
    Represents one detected sensitive column.
    """

    column_name: str
    confidence: float
    privacy_category: str
    recommended_mask: str
    reason: str
