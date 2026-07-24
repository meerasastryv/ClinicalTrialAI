"""
Trend Analytics Service

IC-08
Milestone 7
"""

from __future__ import annotations

import logging
from typing import Any

from src.ic08.services.customer_journey_builder import (
    CustomerJourneyBuilder,
)

logger = logging.getLogger(__name__)


class TrendAnalyticsService:
    """
    Customer usage trend analytics.
    """

    def __init__(
        self,
        journey_builder: CustomerJourneyBuilder,
    ) -> None:

        self._journey_builder = journey_builder

        logger.info(
            "TrendAnalyticsService initialized."
        )

    ####################################################################
    # Internal Helpers
    ####################################################################

    def _journeys(
        self,
    ) -> list[dict[str, Any]]:

        return self._journey_builder.build_all_journeys()

    def _customers(
        self,
    ) -> set[str]:

        return {
            journey["customer_id"]
            for journey in self._journeys()
        }

    ####################################################################
    # Health Check
    ####################################################################

    def health_check(
        self,
    ) -> dict[str, Any]:

        return {
            "status": "healthy",
            "customers": len(self._customers()),
            "journeys": len(self._journeys()),
        }

    ####################################################################
    # Service Information
    ####################################################################

    def service_information(
        self,
    ) -> dict[str, Any]:

        return {
            "service": "TrendAnalyticsService",
            "module": "IC-08 Customer Usage Intelligence",
            "version": "1.0",
            "status": "Ready",
        }

         ####################################################################
    # Customer Trends
    ####################################################################

    def customer_growth_trend(
        self,
    ) -> dict[str, Any]:
        """
        Returns customer growth statistics.
        """

        customers = self._customers()

        return {
            "total_customers": len(customers),
            "new_customers": len(customers),
            "returning_customers": 0,
        }

    ####################################################################
    # Journey Trends
    ####################################################################

    def journey_trend(
        self,
    ) -> dict[str, Any]:
        """
        Returns journey trend statistics.
        """

        journeys = self._journeys()

        completed = sum(
            1
            for journey in journeys
            if journey.get("completed", False)
        )

        return {
            "total_journeys": len(journeys),
            "completed_journeys": completed,
            "completion_rate": (
                round(
                    completed * 100 / len(journeys),
                    2,
                )
                if journeys
                else 0
            ),
        }

    ####################################################################
    # Usage Trends
    ####################################################################

    def usage_trend(
        self,
    ) -> dict[str, Any]:
        """
        Returns usage statistics.
        """

        journeys = self._journeys()

        total_events = sum(
            len(journey.get("events", []))
            for journey in journeys
        )

        average_events = (
            round(
                total_events / len(journeys),
                2,
            )
            if journeys
            else 0
        )

        return {
            "total_events": total_events,
            "average_events_per_journey": average_events,
        }

    ####################################################################
    # Workflow Trends
    ####################################################################

    def workflow_trend(
        self,
    ) -> dict[str, Any]:
        """
        Returns workflow usage statistics.
        """

        journeys = self._journeys()

        workflow_count = {}

        for journey in journeys:

            workflow = journey.get(
                "workflow",
                "Unknown",
            )

            workflow_count[workflow] = (
                workflow_count.get(workflow, 0) + 1
            )

        return {
            "workflow_usage": workflow_count,
        }

    ####################################################################
    # Overall Trend Summary
    ####################################################################

    def trend_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns an overall trend summary.
        """

        return {
            "customer_growth":
                self.customer_growth_trend(),
            "journey_trend":
                self.journey_trend(),
            "usage_trend":
                self.usage_trend(),
            "workflow_trend":
                self.workflow_trend(),
        }



          ####################################################################
    # Feature Adoption
    ####################################################################

    def feature_adoption_trend(
        self,
    ) -> dict[str, Any]:
        """
        Returns feature adoption statistics.
        """

        journeys = self._journeys()

        feature_usage = {}

        for journey in journeys:

            for event in journey.get(
                "events",
                [],
            ):

                feature = event.get(
                    "feature",
                    "Unknown",
                )

                feature_usage[feature] = (
                    feature_usage.get(feature, 0) + 1
                )

        return {
            "features": feature_usage,
            "feature_count": len(feature_usage),
        }

    ####################################################################
    # Customer Engagement
    ####################################################################

    def customer_engagement_trend(
        self,
    ) -> dict[str, Any]:
        """
        Returns customer engagement metrics.
        """

        journeys = self._journeys()

        if not journeys:

            return {
                "average_events_per_customer": 0,
                "engaged_customers": 0,
            }

        total_events = sum(
            len(journey.get("events", []))
            for journey in journeys
        )

        customers = self._customers()

        average = (
            round(
                total_events / len(customers),
                2,
            )
            if customers
            else 0
        )

        engaged = sum(
            1
            for journey in journeys
            if len(journey.get("events", [])) > 0
        )

        return {
            "average_events_per_customer": average,
            "engaged_customers": engaged,
        }

    ####################################################################
    # Active Customer Trend
    ####################################################################

    def active_customer_trend(
        self,
    ) -> dict[str, Any]:
        """
        Returns active customer statistics.
        """

        customers = self._customers()

        return {
            "active_customers": len(customers),
            "inactive_customers": 0,
        }

    ####################################################################
    # Adoption Summary
    ####################################################################

    def adoption_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns a complete adoption summary.
        """

        return {
            "feature_adoption":
                self.feature_adoption_trend(),
            "customer_engagement":
                self.customer_engagement_trend(),
            "active_customers":
                self.active_customer_trend(),
            "trend_summary":
                self.trend_summary(),
        }

         ####################################################################
    # Dashboard Summary
    ####################################################################

    def dashboard_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns dashboard-ready trend analytics.
        """

        return {
            "customers":
                len(self._customers()),
            "journeys":
                len(self._journeys()),
            "customer_growth":
                self.customer_growth_trend(),
            "journey_trend":
                self.journey_trend(),
            "usage_trend":
                self.usage_trend(),
            "feature_adoption":
                self.feature_adoption_trend(),
        }

    ####################################################################
    # Export APIs
    ####################################################################

    def export_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns all analytics for export.
        """

        return {
            "trend_summary":
                self.trend_summary(),
            "adoption_summary":
                self.adoption_summary(),
            "dashboard":
                self.dashboard_summary(),
        }

    ####################################################################
    # Service Summary
    ####################################################################

    def service_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns a high-level summary of the service.
        """

        return {
            "service":
                "TrendAnalyticsService",
            "ready":
                self.is_ready(),
            "health":
                self.health_check(),
            "information":
                self.service_information(),
            "dashboard":
                self.dashboard_summary(),
        }

    ####################################################################
    # Readiness
    ####################################################################

    def is_ready(
        self,
    ) -> bool:
        """
        Returns True if the service is operational.
        """

        return (
            self.health_check()["status"]
            == "healthy"
        )

     
