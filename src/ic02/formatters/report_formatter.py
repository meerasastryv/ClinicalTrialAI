class ReportFormatter:
    """
    Responsible for printing all Test Design Engine reports.
    """

    def print_heading(self, title):
        print("\n" + "=" * 80)
        print(title)
        print("=" * 80)

    def print_scenarios(self, results):

        self.print_heading("Generated Scenarios")

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

    def print_boundary_cases(self, boundary_cases):

        self.print_heading("BOUNDARY VALUE TEST CASES")

        for boundary in boundary_cases:
            print(
                f"{boundary.requirement_id:10}"
                f"{boundary.boundary_type:15}"
                f"{boundary.input_value:10}"
                f"{boundary.expected_result}"
            )

    def print_decision_tables(self, decision_rules):

        self.print_heading("DECISION TABLE RULES")

        for rule in decision_rules:

            print(f"\nRule ID        : {rule.rule_id}")
            print(f"Requirement ID : {rule.requirement_id}")

            print("\nConditions")
            print("-" * 40)

            for condition in rule.conditions:
                print(f"  • {condition}")

            print("\nActions")
            print("-" * 40)

            for action in rule.actions:
                print(f"  • {action}")

            print("\nExpected Result")
            print("-" * 40)
            print(f"  {rule.expected_result}")

            print("-" * 80)
