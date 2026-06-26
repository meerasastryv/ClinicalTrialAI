
from typing import List

from src.ic02.models.test_case import TestCase
from src.ic02.models.test_condition import TestCondition
from src.ic02.data.testcase_repository import TESTCASE_LIBRARY


class TestCaseGenerator:

    def __init__(self):

        self.testcase_counter = 1

    def generate(
        self,
        requirement_id: str,
        condition: TestCondition
    ) -> List[TestCase]:

        testcases = []

        testcase_data = TESTCASE_LIBRARY.get(condition.description)

        if testcase_data:

            # testcase = TestCase(
            #    testcase_id=f"TC-{self.testcase_counter:03}",
            #    requirement_id=requirement_id,
            #    scenario_id=condition.scenario_id,
            #    condition_id=condition.condition_id,
            #    title=testcase_data["title"],
            #    priority=testcase_data["priority"],
            #    test_type=testcase_data["test_type"],
            #    automation_candidate=testcase_data["automation_candidate"],
            #    preconditions=testcase_data["preconditions"],
            #    steps=testcase_data["steps"],
            #    expected_results=testcase_data["expected_results"]
            #)

            kwargs = {
                      "test_case_id": f"TC-{self.testcase_counter:03}",
                      "requirement_id": requirement_id,
                      "scenario_id": condition.scenario_id,
                      "condition_id": condition.condition_id,
                      "title": testcase_data["title"],
                      "priority": testcase_data["priority"],
                      "test_type": testcase_data["test_type"],
                      "automation_candidate": testcase_data["automation_candidate"],
                      "preconditions": testcase_data["preconditions"],
                      "steps": testcase_data["steps"],
                      "expected_results": testcase_data["expected_results"],
                     }

            testcase = TestCase(**kwargs)


            testcases.append(testcase)

            self.testcase_counter += 1

        return testcases
