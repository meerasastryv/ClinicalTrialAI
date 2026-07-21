"""
Data cleansing action model.
"""

from dataclasses import dataclass


@dataclass
class CleansingAction:
    """
    Represents one cleansing action performed on a dataset.
    """

    column: str

    action: str

    description: str

    rows_affected: int

    status: str
