"""
Decision Table Repository

Stores all generated Decision Table rules.
"""

from typing import List

from src.ic02.models.decision_table_model import DecisionTableModel


class DecisionTableRepository:
    """
    Repository for DecisionTableModel objects.
    """

    def __init__(self):
        self._rules: List[DecisionTableModel] = []

    def add(self, rule: DecisionTableModel):
        """
        Add a decision table rule.
        """
        self._rules.append(rule)

    def get_all(self) -> List[DecisionTableModel]:
        """
        Return all generated decision table rules.
        """
        return self._rules

    def clear(self):
        """
        Remove all stored decision table rules.
        """
        self._rules.clear()
