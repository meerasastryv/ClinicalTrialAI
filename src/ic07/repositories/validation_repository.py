"""
Repository for dataset validation.
"""

import re
from typing import Any

import pandas as pd

from src.ic07.models.validation_issue import ValidationIssue
from src.ic07.models.validation_rule import ValidationRule


class ValidationRepository:
    """
    Executes validation rules against a dataset.
    """

    def __init__(self) -> None:
        self._issues: list[ValidationIssue] = []

    @property
    def issues(self) -> list[ValidationIssue]:
        return self._issues

    def clear(self) -> None:
        self._issues.clear()

    def validate(
        self,
        dataframe: pd.DataFrame,
        rules: list[ValidationRule],
    ) -> list[ValidationIssue]:
        """
        Execute all validation rules.
        """
        self.clear()

        for rule in rules:

            if rule.required:
                self._validate_required(dataframe, rule)

            if rule.minimum is not None or rule.maximum is not None:
                self._validate_range(dataframe, rule)

            if rule.pattern:
                self._validate_pattern(dataframe, rule)

            if rule.allowed_values:
                self._validate_allowed_values(dataframe, rule)

            if rule.length is not None:
                self._validate_length(dataframe, rule)

            if rule.rule_type == "duplicate":
                self._validate_duplicates(dataframe, rule)

            if rule.custom_function:
                self._validate_custom(dataframe, rule)

        return self._issues

    def _validate_required(
        self,
        df: pd.DataFrame,
        rule: ValidationRule,
    ) -> None:

        if rule.column not in df.columns:
            return

        for idx, value in df[rule.column].items():

            if pd.isna(value):

                self._issues.append(
                    ValidationIssue(
                        row=idx,
                        column=rule.column,
                        rule="Required",
                        message="Required value missing",
                        value=value,
                    )
                )

    def _validate_range(
        self,
        df: pd.DataFrame,
        rule: ValidationRule,
    ) -> None:

        if rule.column not in df.columns:
            return

        for idx, value in df[rule.column].items():

            if pd.isna(value):
                continue

            if (
                rule.minimum is not None
                and value < rule.minimum
            ):
                self._issues.append(
                    ValidationIssue(
                        idx,
                        rule.column,
                        "Range",
                        f"Value below minimum ({rule.minimum})",
                        value,
                    )
                )

            elif (
                rule.maximum is not None
                and value > rule.maximum
            ):
                self._issues.append(
                    ValidationIssue(
                        idx,
                        rule.column,
                        "Range",
                        f"Value above maximum ({rule.maximum})",
                        value,
                    )
                )

    def _validate_pattern(
        self,
        df: pd.DataFrame,
        rule: ValidationRule,
    ) -> None:

        if rule.column not in df.columns:
            return

        regex = re.compile(rule.pattern)

        for idx, value in df[rule.column].items():

            if pd.isna(value):
                continue

            if not regex.fullmatch(str(value)):
                self._issues.append(
                    ValidationIssue(
                        idx,
                        rule.column,
                        "Pattern",
                        "Pattern mismatch",
                        value,
                    )
                )

    def _validate_allowed_values(
        self,
        df: pd.DataFrame,
        rule: ValidationRule,
    ) -> None:

        if rule.column not in df.columns:
            return

        allowed = set(rule.allowed_values)

        for idx, value in df[rule.column].items():

            if pd.isna(value):
                continue

            if value not in allowed:

                self._issues.append(
                    ValidationIssue(
                        idx,
                        rule.column,
                        "Allowed Values",
                        "Unexpected value",
                        value,
                    )
                )

    def _validate_length(
        self,
        df: pd.DataFrame,
        rule: ValidationRule,
    ) -> None:

        if rule.column not in df.columns:
            return

        for idx, value in df[rule.column].items():

            if pd.isna(value):
                continue

            if len(str(value)) != rule.length:

                self._issues.append(
                    ValidationIssue(
                        idx,
                        rule.column,
                        "Length",
                        f"Expected length {rule.length}",
                        value,
                    )
                )

    def _validate_duplicates(self,df: pd.DataFrame,rule: ValidationRule,) -> None:
        if rule.column not in df.columns:
            return
        duplicates = df[df.duplicated(subset=[rule.column], keep="first")]
        for idx, row in duplicates.iterrows():
            self._issues.append(ValidationIssue(row=idx,column=rule.column,rule="Duplicate",message="Duplicate value found",value=row[rule.column],))
    def _validate_custom(
        self,
        df: pd.DataFrame,
        rule: ValidationRule,
    ) -> None:

        for idx, row in df.iterrows():

            try:

                valid = rule.custom_function(row)

                if not valid:

                    self._issues.append(
                        ValidationIssue(
                            idx,
                            rule.column or "",
                            "Custom Rule",
                            "Business rule violated",
                            None,
                        )
                    )

            except Exception:

                continue

    def summary(self) -> dict[str, Any]:

        return {
            "total_issues": len(self._issues),
            "required": sum(i.rule == "Required" for i in self._issues),
            "range": sum(i.rule == "Range" for i in self._issues),
            "pattern": sum(i.rule == "Pattern" for i in self._issues),
            "duplicates": sum(i.rule == "Duplicate" for i in self._issues),
            "allowed_values": sum(
                i.rule == "Allowed Values"
                for i in self._issues
            ),
            "length": sum(i.rule == "Length" for i in self._issues),
            "custom": sum(i.rule == "Custom Rule" for i in self._issues),
        }
