"""
Masking Result Model

Stores statistics from a masking operation.
"""

from dataclasses import dataclass


@dataclass
class MaskingResult:
    """
    Summary of a masking execution.
    """

    rows_processed: int
    columns_masked: int
    records_masked: int
    execution_time: float
    success: bool
    message: str
