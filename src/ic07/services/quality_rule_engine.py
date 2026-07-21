import re
from typing import Any, Iterable


class QualityRuleEngine:
    """
    Reusable validation rules for data quality assessment.
    """

    @staticmethod
    def is_missing(value: Any) -> bool:
        """
        Check whether a value should be treated as missing.
        """
        if value is None:
            return True

        if isinstance(value, str):
            return value.strip() == ""

        return False

    @staticmethod
    def is_duplicate(value: Any, existing_values: Iterable[Any]) -> bool:
        """
        Check whether a value already exists.
        """
        return value in existing_values

    @staticmethod
    def is_valid_range(
        value: float,
        minimum: float,
        maximum: float
    ) -> bool:
        """
        Validate numeric range.
        """
        return minimum <= value <= maximum

    @staticmethod
    def matches_pattern(
        value: str,
        pattern: str
    ) -> bool:
        """
        Validate using a regular expression.
        """
        return re.fullmatch(pattern, value) is not None

    @staticmethod
    def is_expected_type(
        value: Any,
        expected_type: type
    ) -> bool:
        """
        Validate Python data type.
        """
        return isinstance(value, expected_type)
