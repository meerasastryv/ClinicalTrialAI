from typing import Dict, List, Optional

from src.ic08.models.operational_decision import OperationalDecision


class OperationalDecisionRepository:
    """
    Repository for Operational Decisions.
    """

    def __init__(self):
        self._decisions: Dict[str, OperationalDecision] = {}

    def save(self, decision: OperationalDecision) -> None:
        """
        Save or update an operational decision.
        """
        self._decisions[decision.decision_id] = decision

    def get_decision(
        self,
        decision_id: str
    ) -> Optional[OperationalDecision]:
        """
        Retrieve an operational decision by ID.
        """
        return self._decisions.get(decision_id)

    def get_all_decisions(self) -> List[OperationalDecision]:
        """
        Return all operational decisions.
        """
        return list(self._decisions.values())

    def delete_decision(
        self,
        decision_id: str
    ) -> bool:
        """
        Delete an operational decision.
        """
        if decision_id in self._decisions:
            del self._decisions[decision_id]
            return True
        return False

    def exists(
        self,
        decision_id: str
    ) -> bool:
        """
        Check whether an operational decision exists.
        """
        return decision_id in self._decisions

    def count(self) -> int:
        """
        Return total operational decisions.
        """
        return len(self._decisions)

    def clear(self) -> None:
        """
        Remove all operational decisions.
        """
        self._decisions.clear()
