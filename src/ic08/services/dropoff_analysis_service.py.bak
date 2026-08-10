from __future__ import annotations

import logging
from collections import Counter
from typing import Any

from src.ic08.services.customer_journey_builder import (
    CustomerJourneyBuilder,
)
from src.ic08.services.navigation_analytics_service import (
    NavigationAnalyticsService,
)
from src.ic08.services.funnel_analysis_service import (
    FunnelAnalysisService,
)

logger = logging.getLogger(__name__)


class DropoffAnalysisService:
    """
    Provides advanced drop-off analytics for customer journeys.
    """

    ####################################################################
    # Constructor
    ####################################################################

    def __init__(
        self,
        journey_builder: CustomerJourneyBuilder,
        navigation_service: NavigationAnalyticsService,
        funnel_service: FunnelAnalysisService,
    ) -> None:
        """
        Initializes the Drop-off Analysis Service.
        """

        self._journey_builder = journey_builder
        self._navigation_service = navigation_service
        self._funnel_service = funnel_service

    ####################################################################
    # Data Collection
    ####################################################################

    def _collect_journeys(
        self,
    ) -> list[dict[str, Any]]:
        """
        Returns all customer journeys.
        """

        journeys = self._journey_builder.build_all_journeys()

        logger.debug(
            "Collected %d journeys.",
            len(journeys),
        )

        return journeys

    def _collect_navigation(
        self,
    ) -> NavigationAnalyticsService:
        """
        Returns the navigation analytics service.
        """

        return self._navigation_service

    def _collect_funnels(
        self,
    ) -> FunnelAnalysisService:
        """
        Returns the funnel analysis service.
        """

        return self._funnel_service

    ####################################################################
    # Validation
    ####################################################################

    def _validate_data(
        self,
    ) -> bool:
        """
        Returns True if journey data exists.
        """

        return len(
            self._collect_journeys()
        ) > 0

    ####################################################################
    # Helper Methods
    ####################################################################

    def _exit_pages(
        self,
    ) -> list[str]:
        """
        Returns all exit pages.
        """

        return [
            journey["exit_page"]
            for journey in self._collect_journeys()
            if journey["exit_page"]
        ]

    def _workflows(
        self,
    ) -> list[str]:
        """
        Returns workflow names.
        """

        return [
            journey["workflow"]
            for journey in self._collect_journeys()
        ]

    def _customers(
        self,
    ) -> list[str]:
        """
        Returns customer identifiers.
        """

        return [
            journey["customer_id"]
            for journey in self._collect_journeys()
        ]


         ####################################################################
    # Page Drop-off Analytics
    ####################################################################

    def dropoff_pages(
        self,
    ) -> list[str]:
        """
        Returns all pages where customer journeys ended.
        """

        return self._exit_pages()

    def dropoff_page_counts(
        self,
    ) -> dict[str, int]:
        """
        Returns the number of drop-offs for each exit page.
        """

        return dict(
            Counter(
                self.dropoff_pages()
            )
        )

    def highest_dropoff_pages(
        self,
        top_n: int = 10,
    ) -> list[tuple[str, int]]:
        """
        Returns the pages with the highest number of drop-offs.
        """

        return Counter(
            self.dropoff_pages()
        ).most_common(top_n)

    def lowest_dropoff_pages(
        self,
        bottom_n: int = 10,
    ) -> list[tuple[str, int]]:
        """
        Returns the pages with the lowest number of drop-offs.
        """

        counts = self.dropoff_page_counts()

        return sorted(
            counts.items(),
            key=lambda item: item[1],
        )[:bottom_n]

    def page_dropoff_rate(
        self,
        page: str,
    ) -> float:
        """
        Returns the percentage of journeys that exited on the given page.
        """

        journeys = self._collect_journeys()

        if not journeys:
            return 0.0

        exits = len(
            [
                journey
                for journey in journeys
                if journey.get("exit_page") == page
            ]
        )

        return round(
            exits * 100 / len(journeys),
            2,
        )

    def page_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns page-level drop-off statistics.
        """

        counts = self.dropoff_page_counts()

        return {
            "total_exit_pages": len(counts),
            "total_dropoffs": sum(
                counts.values()
            ),
            "highest_dropoff_pages":
                self.highest_dropoff_pages(),
            "lowest_dropoff_pages":
                self.lowest_dropoff_pages(),
            "page_dropoff_counts": counts,
        }



         ####################################################################
    # Customer & Workflow Analytics
    ####################################################################

    def customer_dropoffs(
        self,
    ) -> dict[str, list[dict[str, Any]]]:
        """
        Groups dropped journeys by customer.
        """

        result: dict[str, list[dict[str, Any]]] = {}

        for journey in self._collect_journeys():
            customer = journey.get("customer_id")

            result.setdefault(
                customer,
                [],
            ).append(journey)

        return result

    def workflow_dropoffs(
        self,
    ) -> dict[str, list[dict[str, Any]]]:
        """
        Groups dropped journeys by workflow.
        """

        result: dict[str, list[dict[str, Any]]] = {}

        for journey in self._collect_journeys():
            workflow = journey.get("workflow")

            result.setdefault(
                workflow,
                [],
            ).append(journey)

        return result

    def customer_dropoff_counts(
        self,
    ) -> dict[str, int]:
        """
        Returns the number of drop-offs per customer.
        """

        return {
            customer: len(journeys)
            for customer, journeys in
            self.customer_dropoffs().items()
        }

    def workflow_dropoff_counts(
        self,
    ) -> dict[str, int]:
        """
        Returns the number of drop-offs per workflow.
        """

        return {
            workflow: len(journeys)
            for workflow, journeys in
            self.workflow_dropoffs().items()
        }

    def highest_dropoff_customer(
        self,
    ) -> tuple[str, int] | None:
        """
        Returns the customer with the highest number of drop-offs.
        """

        counts = self.customer_dropoff_counts()

        if not counts:
            return None

        return max(
            counts.items(),
            key=lambda item: item[1],
        )

    def highest_dropoff_workflow(
        self,
    ) -> tuple[str, int] | None:
        """
        Returns the workflow with the highest number of drop-offs.
        """

        counts = self.workflow_dropoff_counts()

        if not counts:
            return None

        return max(
            counts.items(),
            key=lambda item: item[1],
        )

    def customer_workflow_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns customer and workflow drop-off statistics.
        """

        return {
            "customer_dropoff_counts":
                self.customer_dropoff_counts(),
            "workflow_dropoff_counts":
                self.workflow_dropoff_counts(),
            "highest_dropoff_customer":
                self.highest_dropoff_customer(),
            "highest_dropoff_workflow":
                self.highest_dropoff_workflow(),
        }


         ####################################################################
    # Temporal Analytics
    ####################################################################

    def dropoffs_by_day(
        self,
    ) -> dict[str, int]:
        """
        Returns drop-off counts grouped by day.
        """

        counts: Counter[str] = Counter()

        for journey in self._collect_journeys():
            timestamp = journey.get("end_time")

            if timestamp:
                counts[str(timestamp.date())] += 1

        return dict(counts)

    def dropoffs_by_hour(
        self,
    ) -> dict[int, int]:
        """
        Returns drop-off counts grouped by hour.
        """

        counts: Counter[int] = Counter()

        for journey in self._collect_journeys():
            timestamp = journey.get("end_time")

            if timestamp:
                counts[timestamp.hour] += 1

        return dict(counts)

    def dropoff_trends(
        self,
    ) -> dict[str, Any]:
        """
        Returns temporal drop-off trends.
        """

        return {
            "daily_dropoffs":
                self.dropoffs_by_day(),
            "hourly_dropoffs":
                self.dropoffs_by_hour(),
        }

    def peak_dropoff_period(
        self,
    ) -> dict[str, Any]:
        """
        Returns the busiest drop-off day and hour.
        """

        daily = self.dropoffs_by_day()
        hourly = self.dropoffs_by_hour()

        peak_day = (
            max(
                daily.items(),
                key=lambda item: item[1],
            )
            if daily
            else None
        )

        peak_hour = (
            max(
                hourly.items(),
                key=lambda item: item[1],
            )
            if hourly
            else None
        )

        return {
            "peak_day": peak_day,
            "peak_hour": peak_hour,
        }

    def time_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns temporal drop-off statistics.
        """

        return {
            "daily_dropoffs":
                self.dropoffs_by_day(),
            "hourly_dropoffs":
                self.dropoffs_by_hour(),
            "peak_dropoff_period":
                self.peak_dropoff_period(),
        }



         ####################################################################
    # Root Cause Analytics
    ####################################################################

    def common_exit_paths(
        self,
        top_n: int = 10,
    ) -> list[tuple[str, int]]:
        """
        Returns the most common journey exit paths.
        """

        paths = []

        for journey in self._collect_journeys():
            navigation_path = journey.get(
                "navigation_path",
                [],
            )

            if navigation_path:
                paths.append(
                    " -> ".join(navigation_path)
                )

        return Counter(paths).most_common(top_n)

    def abandonment_patterns(
        self,
    ) -> dict[str, int]:
        """
        Returns abandonment counts grouped by exit page.
        """

        return self.dropoff_page_counts()

    def root_cause_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns consolidated root-cause analytics.
        """

        return {
            "common_exit_paths":
                self.common_exit_paths(),
            "abandonment_patterns":
                self.abandonment_patterns(),
            "highest_dropoff_pages":
                self.highest_dropoff_pages(),
            "highest_dropoff_workflow":
                self.highest_dropoff_workflow(),
            "peak_dropoff_period":
                self.peak_dropoff_period(),
        }

    ####################################################################
    # Dashboard
    ####################################################################

    def dashboard_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns dashboard-ready drop-off analytics.
        """

        return {
            "page_statistics":
                self.page_statistics(),
            "customer_workflow_statistics":
                self.customer_workflow_statistics(),
            "time_statistics":
                self.time_statistics(),
            "root_cause_statistics":
                self.root_cause_statistics(),
        }

    ####################################################################
    # Export
    ####################################################################

    def export_dropoff_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Exports all drop-off analytics.
        """

        return {
            "dashboard":
                self.dashboard_summary(),
            "page_statistics":
                self.page_statistics(),
            "customer_workflow_statistics":
                self.customer_workflow_statistics(),
            "time_statistics":
                self.time_statistics(),
            "root_cause_statistics":
                self.root_cause_statistics(),
        }


         ####################################################################
    # Health Check
    ####################################################################

    def health_check(
        self,
    ) -> dict[str, Any]:
        """
        Returns the health status of the Drop-off Analysis Service.
        """

        journeys = self._collect_journeys()

        return {
            "status": "healthy",
            "service": "DropoffAnalysisService",
            "journeys_processed": len(journeys),
            "exit_pages": len(
                self.dropoff_page_counts()
            ),
            "workflows": len(
                self.workflow_dropoff_counts()
            ),
            "customers": len(
                self.customer_dropoff_counts()
            ),
        }

    ####################################################################
    # Service Information
    ####################################################################

    def service_information(
        self,
    ) -> dict[str, Any]:
        """
        Returns metadata about the service.
        """

        return {
            "service": "DropoffAnalysisService",
            "module": "IC-08 Customer Usage Intelligence",
            "version": "1.0",
            "status": "Ready",
            "supported_operations": [
                "Page Drop-off Analytics",
                "Customer Drop-off Analytics",
                "Workflow Drop-off Analytics",
                "Temporal Analytics",
                "Root Cause Analytics",
                "Dashboard Summary",
                "Export Drop-off Statistics",
                "Health Check",
            ],
        }

    ####################################################################
    # Readiness
    ####################################################################

    def is_ready(
        self,
    ) -> bool:
        """
        Returns True if the service is ready.
        """

        return (
            self.health_check()["status"]
            == "healthy"
        )

    def total_dropoffs(
        self,
    ) -> int:
        """
        Returns the total number of drop-offs.
        """

        return len(
            self.dropoff_pages()
        )

    def service_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns a high-level service summary.
        """

        return {
            "service": "DropoffAnalysisService",
            "ready": self.is_ready(),
            "total_dropoffs": self.total_dropoffs(),
            "health": self.health_check(),
            "service_information":
                self.service_information(),
        }
