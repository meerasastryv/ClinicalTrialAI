"""
Validation engine service.
"""

import pandas as pd

from src.ic07.models.validation_rule import ValidationRule
from src.ic07.repositories.validation_repository import ValidationRepository


class ValidationEngine:
    """
    High-level service for dataset validation.
    """

    def __init__(self) -> None:
        self.repository = ValidationRepository()

    def validate_dataset(
        self,
        dataframe: pd.DataFrame,
        rules: list[ValidationRule],
    ) -> dict:

        issues = self.repository.validate(
            dataframe,
            rules,
        )

        return {
            "rows": len(dataframe),
            "columns": len(dataframe.columns),
            "rules": len(rules),
            "issues": issues,
            "summary": self.repository.summary(),
        }
