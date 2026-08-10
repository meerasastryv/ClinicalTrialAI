from src.ic02.generators.scenario_generator import ScenarioGenerator
from src.ic02.generators.condition_generator import ConditionGenerator
from src.ic02.generators.testcase_generator import TestCaseGenerator
from src.ic02.analyzers.coverage_analyzer import CoverageAnalyzer

from src.ic02.models.requirement import Requirement
from src.ic02.generators.test_data_generator import TestDataGenerator
class TestDesignEngine:
    def __init__(self):
        self.scenario_generator = ScenarioGenerator()
        self.condition_generator = ConditionGenerator()
        self.testcase_generator = TestCaseGenerator()
        self.coverage_analyzer = CoverageAnalyzer()
        self.test_data_generator = TestDataGenerator()
    def generate(self, requirement: Requirement) -> list:
        scenarios = self.scenario_generator.generate(requirement)
        #testdata = []
        #for testcase in testcases:
        #    testdata.append(
        #    self.test_data_generator.generate(testcase)
        #   )
        results = []
        for scenario in scenarios:
            conditions = self.condition_generator.generate(scenario)
            scenario_result = {
                "scenario": scenario,
                "conditions": []
            }
            for condition in conditions:
                testcases = self.testcase_generator.generate(
                    requirement.requirement_id,
                    condition
                )
                testdata = []
                for testcase in testcases:
                    testdata.append(self.test_data_generator.generate(testcase))
                scenario_result["conditions"].append({
                    "condition": condition,
                    "testcases": testcases,
                    "testdata": testdata
                })
            results.append(scenario_result)
        coverage = self.coverage_analyzer.analyze(results)
        print("\n========== COVERAGE REPORT ==========")
        for key, value in coverage.items():
            print(f"{key}: {value}")
        print("=====================================\n")
        return results


