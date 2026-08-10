import uuid

from src.ic08.models.action_plan import ActionPlan
from src.ic08.models.intelligence_report import IntelligenceReport
from src.ic08.repositories.action_plan_repository import ActionPlanRepository


class ActionPlanService:
    """
    Service responsible for generating Action Plans
    from Intelligence Reports.
    """

    def __init__(self, action_plan_repository: ActionPlanRepository):
        self.action_plan_repository = action_plan_repository

    def generate_action_plan(
        self,
        report: IntelligenceReport
    ) -> ActionPlan:
        """
        Generate an action plan from an intelligence report.
        """

        priority = self._determine_priority(report.overall_score)

        expected_outcome = (
            f"Improve overall intelligence score from "
            f"{report.overall_score:.2f} while reducing operational risk."
        )

        action_plan = ActionPlan(
            action_plan_id=str(uuid.uuid4()),
            customer_id=report.customer_id,
            organization_name=report.organization_name,
            overall_score=report.overall_score,
            risk_level=report.risk_level,
            priority=priority,
            actions=list(report.recommendations),
            expected_outcome=expected_outcome,
        )

        self.action_plan_repository.save(action_plan)

        return action_plan

    def _determine_priority(
        self,
        overall_score: float
    ) -> str:
        """
        Determine priority based on overall score.
        """

        if overall_score >= 90:
            return "LOW"

        if overall_score >= 75:
            return "MEDIUM"

        return "HIGH"

    def get_action_plan(
        self,
        action_plan_id: str
    ):
        return self.action_plan_repository.get_action_plan(
            action_plan_id
        )

    def get_all_action_plans(self):
        return self.action_plan_repository.get_all_action_plans()

    def delete_action_plan(
        self,
        action_plan_id: str
    ) -> bool:
        return self.action_plan_repository.delete_action_plan(
            action_plan_id
        )

    def action_plan_count(self) -> int:
        return self.action_plan_repository.count()
