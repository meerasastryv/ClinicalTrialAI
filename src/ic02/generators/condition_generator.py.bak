from typing import List

from src.ic02.models.test_condition import TestCondition
from src.ic02.models.scenario import Scenario
from src.ic02.data.condition_repository import CONDITION_LIBRARY


class ConditionGenerator:

    #def generate(self, scenario: Scenario) -> List[TestCondition]:
    from typing import List
    from src.ic02.models.scenario import Scenario
    from src.ic02.models.test_condition import TestCondition

    def generate(self, scenario: Scenario) -> List[TestCondition]:
        conditions = []

        condition_counter = 1

        condition_descriptions = CONDITION_LIBRARY.get(
            scenario.scenario_name,
            []
        )

        for description in condition_descriptions:

            conditions.append(
                TestCondition(
                    condition_id=f"TCND-{condition_counter:03}",
                    scenario_id=scenario.scenario_id,
                    description=description
                )
            )

            condition_counter += 1

        return conditions
