from src.ic02.models.requirement import Requirement
from src.ic02.engine.test_design_engine import TestDesignEngine

from src.ic02.generators.boundary_value_generator import BoundaryValueGenerator


def main():

    requirement = Requirement(
        requirement_id="REQ-001",
        title="Login",
        # Change this temporarily for Boundary Value testing
        description="Age must be between 18 and 60.",
        priority="High",
        business_rules=[
            "Password length >= 8"
        ],
        acceptance_criteria=[
            "User lands on dashboard"
        ]
    )

    engine = TestDesignEngine()
    results = engine.generate(requirement)

    print("\nGenerated Scenarios\n")

    boundary_generator = BoundaryValueGenerator()
    boundary_cases = boundary_generator.generate(requirement)

    for scenario_result in results:

        scenario = scenario_result["scenario"]

        print(
            f"{scenario.scenario_id} | "
            f"{scenario.scenario_name} | "
            f"{scenario.scenario_type}"
        )

        for condition_result in scenario_result["conditions"]:

            condition = condition_result["condition"]

            print(
                f"    {condition.condition_id} | "
                f"{condition.description}"
            )

            for testcase in condition_result["testcases"]:

                print(f"        Test Case ID    : {testcase.test_case_id}")
                print(f"        Requirement ID : {testcase.requirement_id}")
                print(f"        Scenario ID    : {testcase.scenario_id}")
                print(f"        Condition ID   : {testcase.condition_id}")
                print(f"        Title          : {testcase.title}")
                print(f"        Priority       : {testcase.priority}")
                print(f"        Test Type      : {testcase.test_type}")
                print(f"        Automation     : {testcase.automation_candidate}")

                print("\n        Preconditions:")
                for precondition in testcase.preconditions:
                    print(f"            - {precondition}")

                print("\n        Steps:")
                for index, step in enumerate(testcase.steps, start=1):
                    print(f"            {index}. {step}")

                print("\n        Expected Results:")
                for expected in testcase.expected_results:
                    print(f"            - {expected}")

                print("\n        Test Data:")
                for data in condition_result["testdata"]:
                    if data.testcase_id == testcase.test_case_id:
                        for key, value in data.input_data.items():
                            print(f"            {key}: {value}")

                print()

    print("\n" + "=" * 80)
    print("BOUNDARY VALUE TEST CASES")
    print("=" * 80)

    for boundary in boundary_cases:
        print(
            f"{boundary.requirement_id:10}"
            f"{boundary.boundary_type:15}"
            f"{boundary.input_value:10}"
            f"{boundary.expected_result}"
        )


if __name__ == "__main__":
    main()
