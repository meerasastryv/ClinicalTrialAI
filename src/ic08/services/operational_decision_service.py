import uuid

from src.ic08.models.action_plan import ActionPlan
from src.ic08.models.intelligence_report import IntelligenceReport
from src.ic08.models.operational_decision import OperationalDecision
from src.ic08.repositories.operational_decision_repository import (
    OperationalDecisionRepository,
)


class OperationalDecisionService:
    """
    Service responsible for creating the final
    Operational Decision from the Intelligence Report
    and Action Plan.
    """

    def __init__(
        self,
        operational_decision_repository: OperationalDecisionRepository,
    ):
        self.operational_decision_repository = (
            operational_decision_repository
        )

    def generate_operational_decision(
        self,
        report: IntelligenceReport,
        action_plan: ActionPlan,
    ) -> OperationalDecision:
        """
        Generate the final operational decision.
        """

        decision = OperationalDecision(
            decision_id=str(uuid.uuid4()),
            customer_id=report.customer_id,
            organization_name=report.organization_name,
            overall_score=report.overall_score,
            risk_level=report.risk_level,
            decision_status=self._determine_status(
                report.overall_score
            ),
            executive_summary=report.executive_summary,
            recommended_actions=list(action_plan.actions),
            expected_outcome=action_plan.expected_outcome,
        )

        self.operational_decision_repository.save(decision)

        return decision

    def _determine_status(
        self,
        overall_score: float
    ) -> str:
        """
        Determine decision status.
        """

        if overall_score >= 90:
            return "APPROVED"

        if overall_score >= 75:
            return "REVIEW"

        return "ESCALATE"

    def get_decision(
        self,
        decision_id: str
    ):
        return self.operational_decision_repository.get_decision(
            decision_id
        )

    def get_all_decisions(self):
        return (
            self.operational_decision_repository
            .get_all_decisions()
        )

    def delete_decision(
        self,
        decision_id: str
    ) -> bool:
        return (
            self.operational_decision_repository
            .delete_decision(decision_id)
        )

    def decision_count(self) -> int:
        return (
            self.operational_decision_repository.count()
        )
