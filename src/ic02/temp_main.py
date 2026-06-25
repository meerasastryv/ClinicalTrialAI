from src.ic02.models.requirement import Requirement
from src.ic02.generators.scenario_generator import ScenarioGenerator
from src.ic02.generators.condition_generator import ConditionGenerator
from src.ic02.generators.testcase_generator import TestCaseGenerator


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

    # Create Generators

    scenario_generator = ScenarioGenerator()
    condition_generator = ConditionGenerator()
    testcase_generator = TestCaseGenerator()

    # Generate Scenarios

    scenarios = scenario_generator.generate(requirement)

    print("\nGenerated Scenarios\n")

    # Process each Scenario

    for scenario in scenarios:

        print(
            f"{scenario.scenario_id} | "
            f"{scenario.scenario_name} | "
            f"{scenario.scenario_type}"
        )

        # Generate Conditions

        conditions = condition_generator.generate(scenario)

        for condition in conditions:

            print(
                f"    {condition.condition_id} | "
                f"{condition.description}"
            )

            # Generate Test Cases

            # testcases = testcase_generator.generate(condition)
            testcases = testcase_generator.generate(
                        requirement.requirement_id,
                        condition
            )
            # print(f"        DEBUG: {condition.description} -> {len(testcases)} testcase(s)")

            for testcase in testcases:

                #print(
                #    f"        {testcase.testcase_id} | "
                #    f"{testcase.title}"
                #)
                print(f"        Test Case ID        : {testcase.testcase_id}")
                print(f"        Requirement ID     : {testcase.requirement_id}")
                print(f"        Scenario ID        : {testcase.scenario_id}") 
                print(f"        Condition ID       : {testcase.condition_id}")
                print(f"        Title              : {testcase.title}")
                print(f"        Priority           : {testcase.priority}")
                print(f"        Test Type          : {testcase.test_type}")
                print(f"        Automation         : {testcase.automation_candidate}")
                print("          Preconditions:")

                for precondition in testcase.preconditions:
                    print(f"            - {precondition}")

                print("          Steps:")

                for index, step in enumerate(testcase.steps, start=1):
                    print(f"            {index}. {step}")

                print("          Expected Results:")

                for result in testcase.expected_results:
                    print(f"            - {result}")

                print()

        print()


if __name__ == "__main__":
    main()
