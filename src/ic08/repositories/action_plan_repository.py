from typing import Dict, List, Optional

from src.ic08.models.action_plan import ActionPlan


class ActionPlanRepository:
    """
    Repository for Action Plans.
    """

    def __init__(self):
        self._action_plans: Dict[str, ActionPlan] = {}

    def save(self, action_plan: ActionPlan) -> None:
        """
        Save or update an action plan.
        """
        self._action_plans[action_plan.action_plan_id] = action_plan

    def get_action_plan(
        self,
        action_plan_id: str
    ) -> Optional[ActionPlan]:
        """
        Retrieve an action plan by ID.
        """
        return self._action_plans.get(action_plan_id)

    def get_all_action_plans(self) -> List[ActionPlan]:
        """
        Return all action plans.
        """
        return list(self._action_plans.values())

    def delete_action_plan(
        self,
        action_plan_id: str
    ) -> bool:
        """
        Delete an action plan.
        """
        if action_plan_id in self._action_plans:
            del self._action_plans[action_plan_id]
            return True
        return False

    def exists(
        self,
        action_plan_id: str
    ) -> bool:
        """
        Check whether an action plan exists.
        """
        return action_plan_id in self._action_plans

    def count(self) -> int:
        """
        Return total number of action plans.
        """
        return len(self._action_plans)

    def clear(self) -> None:
        """
        Remove all action plans.
        """
        self._action_plans.clear()
