import uuid

from src.ic08.models.customer_intelligence import CustomerIntelligence
from src.ic08.models.intelligence_report import IntelligenceReport
from src.ic08.repositories.report_repository import ReportRepository


class IntelligenceReportService:
    """
    Service responsible for generating intelligence reports
    from Customer Intelligence dashboards.
    """

    def __init__(self, report_repository: ReportRepository):
        self.report_repository = report_repository

    def generate_report(
        self,
        dashboard: CustomerIntelligence,
        report_format: str = "TEXT"
    ) -> IntelligenceReport:
        """
        Generate an intelligence report from a dashboard.
        """

        metrics = {
            "Health Score": dashboard.health_score,
            "Engagement Score": dashboard.engagement_score,
            "Adoption Score": dashboard.adoption_score,
            "Workflow Score": dashboard.workflow_score,
            "Journey Score": dashboard.journey_score,
            "Study Health Score": dashboard.study_health_score,
            "Overall Score": dashboard.overall_score,
        }

        report = IntelligenceReport(
            report_id=str(uuid.uuid4()),
            customer_id=dashboard.customer_id,
            organization_name=dashboard.organization_name,
            overall_score=dashboard.overall_score,
            risk_level=dashboard.risk_level,
            metrics=metrics,
            recommendations=list(dashboard.recommendations),
            executive_summary=dashboard.executive_summary,
            report_format=report_format,
        )

        self.report_repository.save(report)

        return report

    def get_report(
        self,
        report_id: str
    ):
        return self.report_repository.get_report(report_id)

    def get_all_reports(self):
        return self.report_repository.get_all_reports()

    def delete_report(
        self,
        report_id: str
    ) -> bool:
        return self.report_repository.delete_report(report_id)

    def report_count(self) -> int:
        return self.report_repository.count()
