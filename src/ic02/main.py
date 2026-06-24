from src.ic02.models.requirement import Requirement
from src.ic02.generators.scenario_generator import ScenarioGenerator
from src.ic02.generators.condition_generator import ConditionGenerator

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

    # generator = ScenarioGenerator()

    # scenarios = generator.generate(requirement)

    scenario_generator = ScenarioGenerator()
    condition_generator = ConditionGenerator()

    scenarios = scenario_generator.generate(requirement)
    
    print("\nGenerated Scenarios\n")

    #for scenario in scenarios:
    #    print(
    #        f"{scenario.scenario_id} | "
    #         f"{scenario.scenario_name} | "
     #       f"{scenario.scenario_type}"
     #   )

    # print("\nGenerated Scenarios\n")

    for scenario in scenarios:
        print(
             f"{scenario.scenario_id} | "
             f"{scenario.scenario_name} | "
             f"{scenario.scenario_type}"
        )

        conditions = condition_generator.generate(scenario)

        for condition in conditions:

            print(f"    {condition.condition_id} | "
                  f"{condition.description}"
            )

    print()

if __name__ == "__main__":
    main()
