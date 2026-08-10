from typing import Dict, List, Optional

from src.ic08.models.intelligence_report import IntelligenceReport


class ReportRepository:
    """
    Repository for Intelligence Reports.
    """

    def __init__(self):
        self._reports: Dict[str, IntelligenceReport] = {}

    def save(self, report: IntelligenceReport) -> None:
        """
        Save or update a report.
        """
        self._reports[report.report_id] = report

    def get_report(
        self,
        report_id: str
    ) -> Optional[IntelligenceReport]:
        """
        Retrieve report by report ID.
        """
        return self._reports.get(report_id)

    def get_all_reports(self) -> List[IntelligenceReport]:
        """
        Return all reports.
        """
        return list(self._reports.values())

    def delete_report(
        self,
        report_id: str
    ) -> bool:
        """
        Delete report.
        """
        if report_id in self._reports:
            del self._reports[report_id]
            return True
        return False

    def exists(
        self,
        report_id: str
    ) -> bool:
        """
        Check whether report exists.
        """
        return report_id in self._reports

    def count(self) -> int:
        """
        Total reports.
        """
        return len(self._reports)

    def clear(self) -> None:
        """
        Remove all reports.
        """
        self._reports.clear()
