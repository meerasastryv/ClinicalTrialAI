"""
Test Case Generation Engine

Converts test scenarios into executable test cases.
"""

from typing import List

from src.ic02.models import TestScenario, TestCase


class TestCaseEngine:
    """
    Generates test cases from test scenarios.
    """

    def generate(self, scenarios: List[TestScenario]) -> List[TestCase]:

        test_cases = []

        for index, scenario in enumerate(scenarios, start=1):

            tc = TestCase(
                test_case_id=f"TC{index:03}",
                scenario_id=scenario.scenario_id,
                title=scenario.title,
                objective=scenario.description,
                preconditions=[
                    "Application is available",
                    "User has required permissions"
                ],
                test_steps=[
                    "Execute the scenario",
                    "Observe the application behavior"
                ],
                expected_results=[
                    "System behaves as expected"
                ],
                priority=scenario.priority,
                severity="Medium",
                test_type="Functional"
            )

            test_cases.append(tc)

        return test_cases
