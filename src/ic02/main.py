from src.ic02.models.requirement import Requirement
from src.ic02.engine.test_design_engine import TestDesignEngine


def main():

    requirement = Requirement(
        requirement_id="REQ-001",
        title="Login",
        description="User shall login using valid credentials.",
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

                print(f"        Test Case ID      : {testcase.testcase_id}")
                print(f"        Requirement ID   : {testcase.requirement_id}")
                print(f"        Scenario ID      : {testcase.scenario_id}")
                print(f"        Condition ID     : {testcase.condition_id}")
                print(f"        Title            : {testcase.title}")
                print(f"        Priority         : {testcase.priority}")
                print(f"        Test Type        : {testcase.test_type}")
                print(f"        Automation       : {testcase.automation_candidate}")

                print("\n        Preconditions:")

                for precondition in testcase.preconditions:
                    print(f"            - {precondition}")

                print("\n        Steps:")

                for index, step in enumerate(testcase.steps, start=1):
                    print(f"            {index}. {step}")

                print("\n        Expected Results:")

                for result in testcase.expected_results:
                    print(f"            - {result}")

                print()

        print()


if __name__ == "__main__":
    main()
