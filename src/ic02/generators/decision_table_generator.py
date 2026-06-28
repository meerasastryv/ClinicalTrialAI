"""
Decision Table Generator

Generates Decision Table rules from Requirement business rules.
"""

from src.ic02.models.decision_table_model import DecisionTableModel
from src.ic02.repositories.decision_table_repository import (
    DecisionTableRepository,
)


class DecisionTableGenerator:
    """
    Generates Decision Table rules from business rules.
    """

    def __init__(self):
        self.repository = DecisionTableRepository()

    def generate(self, requirement):
        """
        Generate decision table rules for a requirement.

        Parameters
        ----------
        requirement : Requirement

        Returns
        -------
        list[DecisionTableModel]
        """

        self.repository.clear()

        business_rules = requirement.business_rules

        if not business_rules:
            return self.repository.get_all()

        rule_number = 1

        for rule in business_rules:

            decision_rule = DecisionTableModel(
                requirement_id=requirement.requirement_id,
                rule_id=f"DT-{rule_number:03}",
                conditions=[
                    "Condition 1 = TRUE",
                    "Condition 2 = TRUE",
                ],
                actions=[
                    rule
                ],
                expected_result="Rule Satisfied",
            )

            self.repository.add(decision_rule)

            rule_number += 1

        return self.repository.get_all()
