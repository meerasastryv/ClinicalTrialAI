"""
Test Case Service

Coordinates test case generation and persistence.
"""

from typing import List

from src.ic02.models import TestScenario, TestCase
from src.ic02.generators.test_case_engine import TestCaseEngine
from src.ic02.repositories.test_case_repository import TestCaseRepository


class TestCaseService:
    """
    Service for generating and saving test cases.
    """

    def __init__(self):
        self.engine = TestCaseEngine()
        self.repository = TestCaseRepository()

    def generate_test_cases(
        self,
        scenarios: List[TestScenario],
        output_file: str
    ) -> List[TestCase]:
        """
        Generate test cases and save them.
        """

        test_cases = self.engine.generate(scenarios)

        self.repository.save(
            test_cases,
            output_file
        )

        return test_cases
