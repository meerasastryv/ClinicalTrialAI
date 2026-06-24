from src.ic02.models.requirement import Requirement
from src.ic02.generators.scenario_generator import ScenarioGenerator


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

    generator = ScenarioGenerator()

    scenarios = generator.generate(requirement)

    print("\nGenerated Scenarios\n")

    for scenario in scenarios:
        print(
            f"{scenario.scenario_id} | "
            f"{scenario.scenario_name} | "
            f"{scenario.scenario_type}"
        )


if __name__ == "__main__":
    main()
