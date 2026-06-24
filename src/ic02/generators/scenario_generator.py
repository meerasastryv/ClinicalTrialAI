from typing import List

from src.ic02.models.scenario import Scenario
from src.ic02.models.requirement import Requirement
from src.ic02.data.scenario_repository import SCENARIO_LIBRARY


class ScenarioGenerator:

    def generate(self, requirement: Requirement) -> List[Scenario]:

        scenarios = []

        description = requirement.description.lower()

        scenario_counter = 1

        for keyword, scenario_list in SCENARIO_LIBRARY.items():

            if keyword in description:

                for scenario_name, scenario_type in scenario_list:

                    scenarios.append(
                        Scenario(
                            scenario_id=f"SCN-{scenario_counter:03}",
                            requirement_id=requirement.requirement_id,
                            scenario_name=scenario_name,
                            scenario_type=scenario_type
                        )
                    )

                    scenario_counter += 1

        return scenarios
