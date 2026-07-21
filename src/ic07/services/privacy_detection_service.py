"""
Privacy Detection Service

Detects sensitive columns in a dataset and recommends
appropriate masking methods.
"""

from typing import List

import pandas as pd

from src.ic07.models.sensitive_field import SensitiveField
from src.ic07.repositories.privacy_repository import PrivacyRepository


class PrivacyDetectionService:
    """
    Detects sensitive columns using rule-based intelligence.
    """

    DETECTION_RULES = {
        "name": ("PII", "Name Replacement", 0.99),
        "firstname": ("PII", "Name Replacement", 0.99),
        "lastname": ("PII", "Name Replacement", 0.99),
        "patientname": ("PHI", "Name Replacement", 1.00),
        "subjectname": ("PHI", "Name Replacement", 1.00),

        "email": ("PII", "Email Masking", 0.99),

        "phone": ("PII", "Phone Masking", 0.98),
        "mobile": ("PII", "Phone Masking", 0.98),

        "dob": ("PII", "Date Generalization", 0.97),
        "birthdate": ("PII", "Date Generalization", 0.97),

        "age": ("PII", "Age Generalization", 0.92),

        "address": ("PII", "Address Masking", 0.95),
        "zipcode": ("PII", "ZIP Masking", 0.90),
        "zip": ("PII", "ZIP Masking", 0.90),

        "ssn": ("PII", "SSN Masking", 1.00),
        "passport": ("PII", "Passport Masking", 1.00),
        "pan": ("PII", "PAN Masking", 1.00),
        "aadhaar": ("PII", "Aadhaar Masking", 1.00),

        "creditcard": ("Financial", "Credit Card Masking", 1.00),
        "cardnumber": ("Financial", "Credit Card Masking", 1.00),

        "medicalrecord": ("PHI", "Medical Record Tokenization", 1.00),
        "patientid": ("PHI", "Identifier Tokenization", 1.00),
        "subjectid": ("Clinical", "Identifier Tokenization", 1.00),
    }

    def __init__(self,
                 repository: PrivacyRepository):
        self.repository = repository

    def detect_sensitive_fields(
            self,
            df: pd.DataFrame
    ) -> List[SensitiveField]:
        """
        Detect sensitive columns in a dataframe.
        """

        self.repository.clear_sensitive_fields()

        detected = []

        for column in df.columns:

            normalized = (
                column.lower()
                .replace("_", "")
                .replace(" ", "")
            )

            if normalized in self.DETECTION_RULES:

                category, mask, confidence = (
                    self.DETECTION_RULES[normalized]
                )

                field = SensitiveField(
                    column_name=column,
                    confidence=confidence,
                    privacy_category=category,
                    recommended_mask=mask,
                    reason=f"Matched rule '{normalized}'"
                )

                detected.append(field)

                self.repository.save_detection(field)

        return detected
