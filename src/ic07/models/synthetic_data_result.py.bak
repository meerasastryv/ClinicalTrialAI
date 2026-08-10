"""
Synthetic Data Result Model

Author : Meera Sastry
Project : ClinicalTrialAI
"""

from dataclasses import dataclass, field
from typing import List

import pandas as pd


@dataclass
class SyntheticDataResult:
    """
    Stores the outcome of synthetic data generation.
    """

    generated_dataframe: pd.DataFrame

    row_count: int

    column_count: int

    duplicate_count: int

    null_count: int

    invalid_count: int

    generation_time: float

    warnings: List[str] = field(default_factory=list)
