from typing import Optional

from src.ic08.models.customer_intelligence import CustomerIntelligence
from src.ic08.repositories.intelligence_repository import IntelligenceRepository


class CustomerIntelligenceService:
    """
    Aggregates intelligence from multiple IC-08 services into a
    consolidated dashboard.

    NOTE:
    This service will eventually become StudyIntelligenceService
    during the IC-08 refactoring phase.
    """

    def __init__(
        self,
        repository: IntelligenceRepository
    ):
        self.repository = repository

    def build_dashboard(
        self,
        customer_id: str,
        organization_name: str,
        study_id: str = "",
        study_name: str = ""
    ) -> CustomerIntelligence:
        """
        Build and store a consolidated intelligence dashboard.
        """

        dashboard = CustomerIntelligence(
            customer_id=customer_id,
            organization_name=organization_name,
            study_id=study_id,
            study_name=study_name
        )

        self._populate_dashboard(dashboard)

        dashboard.overall_score = self._calculate_overall_score(dashboard)

        dashboard.risk_level = self._determine_risk_level(
            dashboard.overall_score
        )

        self.repository.save(dashboard)

        return dashboard

    def get_dashboard(
        self,
        customer_id: str
    ) -> Optional[CustomerIntelligence]:

        return self.repository.get_by_customer_id(customer_id)

    def get_all_dashboards(self):

        return self.repository.get_all()

    def _populate_dashboard(
        self,
        dashboard: CustomerIntelligence
    ) -> None:
        """
        Populate dashboard with intelligence metrics.

        Initially uses sample values.
        Future versions will gather data from:
        - Customer Health Service
        - Engagement Service
        - Workflow Service
        - Journey Service
        - Feature Adoption Service
        - Study Health Service
        - Recommendation Service
        """

        dashboard.health_score = 85.0
        dashboard.engagement_score = 81.0
        dashboard.adoption_score = 79.0
        dashboard.workflow_score = 88.0
        dashboard.journey_score = 84.0
        dashboard.study_health_score = 91.0

        dashboard.total_users = 42
        dashboard.active_sessions = 318
        dashboard.average_session_duration = 28.4

        dashboard.workflow_completion = 90.0
        dashboard.journey_completion = 87.0
        dashboard.drop_off_rate = 5.0

        dashboard.top_features = [
            "Study Builder",
            "Metadata Repository",
            "Risk Dashboard"
        ]

        dashboard.least_used_features = [
            "Export Wizard"
        ]

        dashboard.trend_summary = {
            "weekly_growth": 8.2,
            "monthly_growth": 21.6
        }

        dashboard.recommendations = [
            "Increase Metadata Repository adoption.",
            "Reduce workflow drop-offs.",
            "Promote Risk Dashboard usage."
        ]

    def _calculate_overall_score(
        self,
        dashboard: CustomerIntelligence
    ) -> float:

        weights = {
            "health": 0.25,
            "engagement": 0.15,
            "adoption": 0.15,
            "workflow": 0.15,
            "journey": 0.10,
            "study_health": 0.20
        }

        score = (
            dashboard.health_score * weights["health"]
            + dashboard.engagement_score * weights["engagement"]
            + dashboard.adoption_score * weights["adoption"]
            + dashboard.workflow_score * weights["workflow"]
            + dashboard.journey_score * weights["journey"]
            + dashboard.study_health_score * weights["study_health"]
        )

        return round(score, 2)

    def _determine_risk_level(
        self,
        score: float
    ) -> str:

        if score >= 90:
            return "LOW"

        if score >= 70:
            return "MEDIUM"

        return "HIGH"


