"""
Privacy Rule Model

Represents a masking rule for a sensitive column.
"""

from dataclasses import dataclass


@dataclass
class PrivacyRule:
    """
    Represents one privacy masking rule.
    """

    column_name: str
    data_type: str
    privacy_type: str
    masking_method: str
    priority: int = 1
    enabled: bool = True
    notes: str = ""
