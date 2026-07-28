"""
IC-08 - Platform Usage Intelligence
Milestone 16 - Study Health Service
"""

from src.ic08.models.study_health import StudyHealth
from src.ic08.repositories.study_health_repository import (
    StudyHealthRepository,
)


class StudyHealthService:
    """
    Computes the overall Study Health Index for a clinical study.
    """

    def __init__(self):
        self.repository = StudyHealthRepository()

    def calculate_health(
        self,
        study_id: str,
        programmer_productivity: float,
        workflow_completion: float,
        metadata_reuse: float,
        deliverable_completion: float,
        platform_usage_risk: float,
        history_count: int,
    ) -> StudyHealth:
        """
        Calculate the Study Health Index.
        """

        risk_contribution = 100 - platform_usage_risk

        health_score = (
            programmer_productivity * 0.30
            + workflow_completion * 0.25
            + metadata_reuse * 0.20
            + deliverable_completion * 0.15
            + risk_contribution * 0.10
        )

        health_score = round(health_score, 2)

        status = self._determine_status(health_score)
        risk_level = self._determine_risk(health_score)
        confidence = self._determine_confidence(history_count)

        study_health = StudyHealth(
            study_id=study_id,
            health_score=health_score,
            status=status,
            risk_level=risk_level,
            confidence=confidence,
        )

        self._add_indicators(
            study_health,
            programmer_productivity,
            workflow_completion,
            metadata_reuse,
            deliverable_completion,
            platform_usage_risk,
        )

        self.repository.save(study_health)

        return study_health

    def get_study(self, study_id: str):
        """
        Retrieve a study health record.
        """
        return self.repository.find_by_study(study_id)

    def get_all_studies(self):
        """
        Return all study health records.
        """
        return self.repository.find_all()

    def average_health(self):
        """
        Return average Study Health Index.
        """
        return self.repository.average_health()

    def top_healthy_studies(self, limit: int = 5):
        """
        Return healthiest studies.
        """
        return self.repository.top_healthy_studies(limit)

    def _determine_status(self, score: float) -> str:

        if score >= 90:
            return "Excellent"

        if score >= 80:
            return "Healthy"

        if score >= 70:
            return "Stable"

        if score >= 60:
            return "Needs Attention"

        return "Critical"

    def _determine_risk(self, score: float) -> str:

        if score >= 90:
            return "Low"

        if score >= 80:
            return "Moderate"

        if score >= 70:
            return "Elevated"

        return "High"

    def _determine_confidence(
        self,
        history_count: int
    ) -> float:

        if history_count >= 20:
            return 0.95

        if history_count >= 10:
            return 0.80

        return 0.60

    def _add_indicators(
        self,
        study_health: StudyHealth,
        programmer_productivity: float,
        workflow_completion: float,
        metadata_reuse: float,
        deliverable_completion: float,
        platform_usage_risk: float,
    ):

        if programmer_productivity >= 80:
            study_health.add_indicator(
                "High Programmer Productivity"
            )

        if workflow_completion >= 80:
            study_health.add_indicator(
                "Strong Workflow Completion"
            )

        if metadata_reuse >= 80:
            study_health.add_indicator(
                "Excellent Metadata Reuse"
            )

        if deliverable_completion >= 80:
            study_health.add_indicator(
                "Deliverables On Schedule"
            )

        if platform_usage_risk <= 20:
            study_health.add_indicator(
                "Low Platform Usage Risk"
            )

        if not study_health.indicators:
            study_health.add_indicator(
                "Study Requires Operational Review"
            )
