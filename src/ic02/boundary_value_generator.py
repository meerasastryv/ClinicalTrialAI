"""
boundary_value_generator.py

Facade for Boundary Value Analysis (BVA).

Coordinates:
1. Boundary Detection
2. Boundary Rule Generation
3. Boundary Test Case Generation

Author: Meera Sastry
Project: ClinicalTrialAI - IC-02 Test Design Engine
"""
from boundary_exporter import BoundaryExporter
from boundary_detector import BoundaryDetector
from boundary_rules import BoundaryRuleEngine
from boundary_models import (
    BoundaryAnalysisResult,
    BoundaryTestCase,
)


class BoundaryValueGenerator:
    """
    Facade for generating Boundary Value Analysis results.
    """

    def __init__(self):
        self.detector = BoundaryDetector()
        self.rule_engine = BoundaryRuleEngine()

    def generate(self, requirement: str) -> BoundaryAnalysisResult | None:

        constraint = self.detector.detect(requirement)

        if constraint is None:
            return None

        boundary_values = self.rule_engine.generate(constraint)

        test_cases = []

        for index, value in enumerate(boundary_values, start=1):

            test_cases.append(
                BoundaryTestCase(
                    test_id=f"TC_BVA_{index:03}",
                    parameter=constraint.parameter,
                    input_value=value.value,
                    expected_result=value.expected_result,
                    description=f"Verify {constraint.parameter} with {value.label}"
                )
            )

        return BoundaryAnalysisResult(
            constraint=constraint,
            boundary_values=boundary_values,
            test_cases=test_cases
        )


if __name__ == "__main__":

    generator = BoundaryValueGenerator()

    requirement = "Age should be between 18 and 60."

    result = generator.generate(requirement)

    print("\nDetected Constraint")
    print("-------------------")
    print(result.constraint)

    print("\nBoundary Values")
    print("-------------------")

    for value in result.boundary_values:
        print(value)

    print("\nBoundary Test Cases")
    print("-------------------")

    for testcase in result.test_cases:
        print(testcase)
    exporter = BoundaryExporter()

    exporter.export_to_json(
        result,
        "src/ic02/output/boundary_analysis.json"
    )
