"""
Test Case Repository
Stores generated test cases.
"""

import json
from dataclasses import asdict
from typing import List
from src.ic02.models import TestCase

class TestCaseRepository:
    """
    Repository for storing generated test cases.
    """
    def save(self, test_cases: List[TestCase], output_file: str) -> None:
        """
        Save test cases to a JSON file.
        """
        with open(output_file, "w", encoding="utf-8") as file:
            json.dump(
                [asdict(tc) for tc in test_cases],
                file,
                indent=4
            )
        print(f"Saved {len(test_cases)} test cases to {output_file}")
