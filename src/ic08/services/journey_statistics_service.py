from __future__ import annotations

import logging
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
from src.ic08.services.dropoff_analysis_service import (
    DropoffAnalysisService,
)

logger = logging.getLogger(__name__)


class JourneyStatisticsService:
    """
    Aggregates customer journey statistics from all analytics services.
    """

    ####################################################################
    # Constructor
    ####################################################################

    def __init__(
        self,
        journey_builder: CustomerJourneyBuilder,
        navigation_service: NavigationAnalyticsService,
        funnel_service: FunnelAnalysisService,
        dropoff_service: DropoffAnalysisService,
    ) -> None:
        """
        Initializes the Journey Statistics Service.
        """

        self._journey_builder = journey_builder
        self._navigation_service = navigation_service
        self._funnel_service = funnel_service
        self._dropoff_service = dropoff_service

    ####################################################################
    # Service Access
    ####################################################################

    def _journeys(
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

    def _navigation(
        self,
    ) -> NavigationAnalyticsService:
        """
        Returns the navigation analytics service.
        """

        return self._navigation_service

    def _funnels(
        self,
    ) -> FunnelAnalysisService:
        """
        Returns the funnel analysis service.
        """

        return self._funnel_service

    def _dropoffs(
        self,
    ) -> DropoffAnalysisService:
        """
        Returns the drop-off analysis service.
        """

        return self._dropoff_service

    ####################################################################
    # Validation
    ####################################################################

    def _validate(
        self,
    ) -> bool:
        """
        Returns True if journey data is available.
        """

        return len(
            self._journeys()
        ) > 0

    ####################################################################
    # Helper Methods
    ####################################################################

    def total_journeys(
        self,
    ) -> int:
        """
        Returns the total number of journeys.
        """

        return len(
            self._journeys()
        )

    def total_customers(
        self,
    ) -> int:
        """
        Returns the total number of unique customers.
        """

        return len(
            {
                journey["customer_id"]
                for journey in self._journeys()
            }
        )

    def total_workflows(
        self,
    ) -> int:
        """
        Returns the total number of unique workflows.
        """

        return len(
            {
                journey["workflow"]
                for journey in self._journeys()
            }
        )

         ####################################################################
    # Journey Statistics
    ####################################################################

    def journey_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns overall journey statistics.
        """

        journeys = self._journeys()

        if not journeys:
            return {
                "total_journeys": 0,
                "completed_journeys": 0,
                "abandoned_journeys": 0,
                "completion_rate": 0.0,
                "abandonment_rate": 0.0,
            }

        completed = sum(
            1
            for journey in journeys
            if journey.get("completed", False)
        )

        abandoned = len(journeys) - completed

        return {
            "total_journeys": len(journeys),
            "completed_journeys": completed,
            "abandoned_journeys": abandoned,
            "completion_rate": round(
                completed * 100 / len(journeys),
                2,
            ),
            "abandonment_rate": round(
                abandoned * 100 / len(journeys),
                2,
            ),
        }

    def average_journey_duration(
        self,
    ) -> float:
        """
        Returns the average journey duration in seconds.
        """

        journeys = self._journeys()

        durations = [
            journey.get("duration_seconds", 0)
            for journey in journeys
            if journey.get("duration_seconds") is not None
        ]

        if not durations:
            return 0.0

        return round(
            sum(durations) / len(durations),
            2,
        )

    def longest_journey(
        self,
    ) -> dict[str, Any] | None:
        """
        Returns the longest customer journey.
        """

        journeys = self._journeys()

        if not journeys:
            return None

        return max(
            journeys,
            key=lambda journey: journey.get(
                "duration_seconds",
                0,
            ),
        )

    def shortest_journey(
        self,
    ) -> dict[str, Any] | None:
        """
        Returns the shortest customer journey.
        """

        journeys = self._journeys()

        if not journeys:
            return None

        return min(
            journeys,
            key=lambda journey: journey.get(
                "duration_seconds",
                0,
            ),
        )

    def journey_duration_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns journey duration statistics.
        """

        return {
            "average_duration_seconds":
                self.average_journey_duration(),
            "longest_journey":
                self.longest_journey(),
            "shortest_journey":
                self.shortest_journey(),
        }

    def journey_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns a summary of journey statistics.
        """

        return {
            "journey_statistics":
                self.journey_statistics(),
            "journey_duration_statistics":
                self.journey_duration_statistics(),
            "total_customers":
                self.total_customers(),
            "total_workflows":
                self.total_workflows(),
        }


         ####################################################################
    # Navigation Statistics
    ####################################################################

    def navigation_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns aggregated navigation statistics.
        """

        navigation = self._navigation()

        return {
            "page_statistics":
                navigation.page_statistics(),
            "entry_exit_statistics":
                navigation.entry_exit_statistics(),
            "transition_statistics":
                navigation.navigation_statistics(),
            "bounce_statistics":
                navigation.bounce_statistics(),
        }

    ####################################################################
    # Funnel Statistics
    ####################################################################

    def funnel_statistics(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns aggregated funnel statistics.
        """

        funnel_service = self._funnels()

        return {
            "funnel_summary":
                funnel_service.funnel_summary(
                    funnel,
                ),
            "conversion_statistics":
                funnel_service.conversion_statistics(
                    funnel,
                ),
            "dropoff_statistics":
                funnel_service.dropoff_statistics(
                    funnel,
                ),
        }

    ####################################################################
    # Combined Statistics
    ####################################################################

    def navigation_funnel_statistics(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns combined navigation and funnel statistics.
        """

        return {
            "navigation_statistics":
                self.navigation_statistics(),
            "funnel_statistics":
                self.funnel_statistics(
                    funnel,
                ),
        }

    def navigation_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns a navigation summary.
        """

        navigation = self._navigation()

        return {
            "page_statistics":
                navigation.page_statistics(),
            "transition_statistics":
                navigation.navigation_statistics(),
        }

    def funnel_summary(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns a funnel summary.
        """

        return self._funnels().funnel_summary(
            funnel,
        )

    def overall_navigation_funnel_summary(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns an overall summary of navigation and funnel analytics.
        """

        return {
            "navigation":
                self.navigation_summary(),
            "funnel":
                self.funnel_summary(
                    funnel,
                ),
        }

         ####################################################################
    # Customer Statistics
    ####################################################################

    def customer_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns aggregated customer statistics.
        """

        dropoff = self._dropoffs()

        return {
            "total_customers":
                self.total_customers(),
            "customer_dropoff_counts":
                dropoff.customer_dropoff_counts(),
            "highest_dropoff_customer":
                dropoff.highest_dropoff_customer(),
        }

    ####################################################################
    # Workflow Statistics
    ####################################################################

    def workflow_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns aggregated workflow statistics.
        """

        dropoff = self._dropoffs()

        return {
            "total_workflows":
                self.total_workflows(),
            "workflow_dropoff_counts":
                dropoff.workflow_dropoff_counts(),
            "highest_dropoff_workflow":
                dropoff.highest_dropoff_workflow(),
        }

    ####################################################################
    # Drop-off Statistics
    ####################################################################

    def dropoff_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns aggregated drop-off statistics.
        """

        dropoff = self._dropoffs()

        return {
            "page_statistics":
                dropoff.page_statistics(),
            "customer_workflow_statistics":
                dropoff.customer_workflow_statistics(),
            "time_statistics":
                dropoff.time_statistics(),
            "root_cause_statistics":
                dropoff.root_cause_statistics(),
        }

    ####################################################################
    # Combined Customer Statistics
    ####################################################################

    def customer_workflow_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns customer and workflow summary statistics.
        """

        return {
            "customer_statistics":
                self.customer_statistics(),
            "workflow_statistics":
                self.workflow_statistics(),
            "dropoff_statistics":
                self.dropoff_statistics(),
        }

    def platform_statistics(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns consolidated platform statistics.
        """

        return {
            "journey_statistics":
                self.journey_summary(),
            "navigation_statistics":
                self.navigation_summary(),
            "funnel_statistics":
                self.funnel_summary(
                    funnel,
                ),
            "customer_workflow_statistics":
                self.customer_workflow_summary(),
        }

    def platform_kpis(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns high-level platform KPIs.
        """

        return {
            "total_journeys":
                self.total_journeys(),
            "total_customers":
                self.total_customers(),
            "total_workflows":
                self.total_workflows(),
            "platform_statistics":
                self.platform_statistics(
                    funnel,
                ),
        }


         ####################################################################
    # Dashboard
    ####################################################################

    def dashboard_summary(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns a dashboard-ready summary of journey analytics.
        """

        return {
            "journey_summary":
                self.journey_summary(),
            "navigation_summary":
                self.navigation_summary(),
            "funnel_summary":
                self.funnel_summary(
                    funnel,
                ),
            "customer_workflow_summary":
                self.customer_workflow_summary(),
        }

    ####################################################################
    # Export APIs
    ####################################################################

    def export_statistics(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Exports complete journey statistics.
        """

        return {
            "journey_statistics":
                self.journey_summary(),
            "navigation_statistics":
                self.navigation_statistics(),
            "funnel_statistics":
                self.funnel_statistics(
                    funnel,
                ),
            "customer_statistics":
                self.customer_statistics(),
            "workflow_statistics":
                self.workflow_statistics(),
            "dropoff_statistics":
                self.dropoff_statistics(),
        }

    def export_dashboard(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Exports dashboard-ready analytics.
        """

        return {
            "dashboard":
                self.dashboard_summary(
                    funnel,
                ),
            "platform_kpis":
                self.platform_kpis(
                    funnel,
                ),
        }

    ####################################################################
    # Platform Summary
    ####################################################################

    def overall_statistics(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns complete platform statistics.
        """

        return {
            "platform_kpis":
                self.platform_kpis(
                    funnel,
                ),
            "dashboard":
                self.dashboard_summary(
                    funnel,
                ),
            "statistics":
                self.export_statistics(
                    funnel,
                ),
        }

    def analytics_summary(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Returns an analytics summary.
        """

        return {
            "journey":
                self.journey_summary(),
            "navigation":
                self.navigation_summary(),
            "funnel":
                self.funnel_summary(
                    funnel,
                ),
            "customer_workflow":
                self.customer_workflow_summary(),
            "platform":
                self.platform_kpis(
                    funnel,
                ),
        }

    def export_all(
        self,
        funnel: list[str],
    ) -> dict[str, Any]:
        """
        Exports all available analytics.
        """

        return {
            "dashboard":
                self.export_dashboard(
                    funnel,
                ),
            "statistics":
                self.export_statistics(
                    funnel,
                ),
            "overall":
                self.overall_statistics(
                    funnel,
                ),
        }


         ####################################################################
    # Health Check
    ####################################################################

    def health_check(
        self,
    ) -> dict[str, Any]:
        """
        Returns the health status of the Journey Statistics Service.
        """

        journeys = self._journeys()

        return {
            "status": "healthy",
            "service": "JourneyStatisticsService",
            "journeys_processed": len(journeys),
            "customers": self.total_customers(),
            "workflows": self.total_workflows(),
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
            "service": "JourneyStatisticsService",
            "module": "IC-08 Customer Usage Intelligence",
            "version": "1.0",
            "status": "Ready",
            "supported_operations": [
                "Journey Statistics",
                "Navigation Statistics",
                "Funnel Statistics",
                "Customer Statistics",
                "Workflow Statistics",
                "Drop-off Statistics",
                "Platform KPIs",
                "Dashboard Summary",
                "Export Statistics",
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

    def service_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns a high-level service summary.
        """

        return {
            "service": "JourneyStatisticsService",
            "ready": self.is_ready(),
            "health": self.health_check(),
            "service_information":
                self.service_information(),
            "totals": {
                "journeys": self.total_journeys(),
                "customers": self.total_customers(),
                "workflows": self.total_workflows(),
            },
        }
