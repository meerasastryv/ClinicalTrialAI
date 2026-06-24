from typing import List

from src.ic02.models.scenario import Scenario
from src.ic02.models.requirement import Requirement


class ScenarioGenerator:

    def generate(self, requirement: Requirement) -> List[Scenario]:

        scenarios = []

        scenarios.append(
            Scenario(
                scenario_id="SCN-001",
                requirement_id=requirement.requirement_id,
                scenario_name="Positive Flow",
                scenario_type="Positive"
            )
        )

        scenarios.append(
            Scenario(
                scenario_id="SCN-002",
                requirement_id=requirement.requirement_id,
                scenario_name="Negative Flow",
                scenario_type="Negative"
            )
        )

        return scenarios
