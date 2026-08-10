"""
Privacy Repository

Stores privacy rules, detected sensitive fields,
and masking execution results.
"""

from typing import List, Optional

from src.ic07.models.privacy_rule import PrivacyRule
from src.ic07.models.sensitive_field import SensitiveField
from src.ic07.models.masking_result import MaskingResult


class PrivacyRepository:
    """
    Repository for privacy-related metadata.
    """

    def __init__(self) -> None:
        self._rules: List[PrivacyRule] = []
        self._sensitive_fields: List[SensitiveField] = []
        self._masking_results: List[MaskingResult] = []

    # ---------------------------------------------------------
    # Privacy Rules
    # ---------------------------------------------------------

    def save_rule(self, rule: PrivacyRule) -> None:
        """Save a privacy rule."""
        self._rules.append(rule)

    def get_rules(self) -> List[PrivacyRule]:
        """Return all privacy rules."""
        return list(self._rules)

    # ---------------------------------------------------------
    # Sensitive Fields
    # ---------------------------------------------------------

    def save_detection(self, field: SensitiveField) -> None:
        """Save a detected sensitive field."""
        self._sensitive_fields.append(field)

    def get_sensitive_fields(self) -> List[SensitiveField]:
        """Return detected sensitive fields."""
        return list(self._sensitive_fields)

    def clear_sensitive_fields(self) -> None:
        """Clear detected sensitive fields."""
        self._sensitive_fields.clear()

    # ---------------------------------------------------------
    # Masking Results
    # ---------------------------------------------------------

    def save_result(self, result: MaskingResult) -> None:
        """Save a masking execution result."""
        self._masking_results.append(result)

    def get_last_result(self) -> Optional[MaskingResult]:
        """Return the latest masking result."""
        if not self._masking_results:
            return None
        return self._masking_results[-1]

    def get_results(self) -> List[MaskingResult]:
        """Return all masking results."""
        return list(self._masking_results)

    # ---------------------------------------------------------
    # Utility
    # ---------------------------------------------------------

    def clear(self) -> None:
        """Reset the repository."""
        self._rules.clear()
        self._sensitive_fields.clear()
        self._masking_results.clear()
