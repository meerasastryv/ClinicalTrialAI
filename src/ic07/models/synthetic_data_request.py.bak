"""
Synthetic Data Request Model

Author : Meera Sastry
Project : ClinicalTrialAI
"""

from dataclasses import dataclass


@dataclass
class SyntheticDataRequest:
    """
    Configuration for synthetic data generation.
    """

    rows: int = 1000

    include_nulls: bool = True

    include_duplicates: bool = False

    include_invalid_values: bool = False

    include_boundary_values: bool = False

    preserve_distribution: bool = True

    random_seed: int | None = None

    output_format: str = "csv"
