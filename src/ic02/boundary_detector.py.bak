"""
boundary_detector.py

Extracts boundary constraints from natural language requirements.

Author: Meera Sastry
Project: ClinicalTrialAI - IC-02 Test Design Engine
"""

import re
from typing import Optional

from boundary_models import BoundaryConstraint


class BoundaryDetector:
    """
    Detects numeric boundary constraints from a requirement.
    """

    def detect(self, requirement: str) -> Optional[BoundaryConstraint]:

        text = requirement.lower()

        # Pattern: between X and Y
        match = re.search(r"(\w+).*between\s+(\d+)\s+and\s+(\d+)", text)

        if match:
            return BoundaryConstraint(
                parameter=match.group(1),
                minimum=float(match.group(2)),
                maximum=float(match.group(3))
            )

        # Pattern: X-Y
        match = re.search(r"(\w+).*?(\d+)\s*-\s*(\d+)", text)

        if match:
            return BoundaryConstraint(
                parameter=match.group(1),
                minimum=float(match.group(2)),
                maximum=float(match.group(3))
            )

        # Pattern: at least X
        match = re.search(r"(\w+).*at least\s+(\d+)", text)

        if match:
            return BoundaryConstraint(
                parameter=match.group(1),
                minimum=float(match.group(2))
            )

        # Pattern: at most X
        match = re.search(r"(\w+).*at most\s+(\d+)", text)

        if match:
            return BoundaryConstraint(
                parameter=match.group(1),
                maximum=float(match.group(2))
            )

        return None


if __name__ == "__main__":

    detector = BoundaryDetector()

    samples = [
        "Age should be between 18 and 60.",
        "Password length should be 8-20 characters.",
        "Quantity should be at least 1.",
        "Discount should be at most 50."
    ]

    for sample in samples:
        print(detector.detect(sample))
