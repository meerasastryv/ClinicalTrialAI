"""
customer_intelligence_dashboard_service.py

Customer Intelligence Dashboard Service

Provides a unified dashboard for Customer Usage Intelligence.
"""

from __future__ import annotations

import logging
from typing import Any

from src.ic08.services.customer_journey_builder import (
    CustomerJourneyBuilder,
)

logger = logging.getLogger(__name__)


class CustomerIntelligenceDashboardService:
    """
    Customer Intelligence Dashboard Service.
    """

    ####################################################################
    # Constructor
    ####################################################################

    def __init__(
        self,
        journey_builder: CustomerJourneyBuilder,
    ) -> None:

        self._journey_builder = journey_builder

        logger.info(
            "CustomerIntelligenceDashboardService initialized."
        )

    ####################################################################
    # Internal Helpers
    ####################################################################

    def _journeys(
        self,
    ) -> list[dict[str, Any]]:
        """
        Returns all customer journeys.
        """

        return self._journey_builder.build_all_journeys()

    ####################################################################
    # Health Check
    ####################################################################

    def health_check(
        self,
    ) -> dict[str, Any]:
        """
        Returns service health.
        """

        return {
            "status": "healthy",
            "service":
                "CustomerIntelligenceDashboardService",
            "journeys":
                len(self._journeys()),
        }

    ####################################################################
    # Service Information
    ####################################################################

    def service_information(
        self,
    ) -> dict[str, Any]:
        """
        Returns service metadata.
        """

        return {
            "service":
                "CustomerIntelligenceDashboardService",
            "module":
                "IC-08 Customer Usage Intelligence",
            "version":
                "1.0",
            "status":
                "Ready",
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


         ####################################################################
    # Customer Overview
    ####################################################################

    def customer_overview(
        self,
    ) -> dict[str, Any]:
        """
        Returns high-level customer overview.
        """

        journeys = self._journeys()

        customers = {
            journey["customer_id"]
            for journey in journeys
        }

        completed = sum(
            1
            for journey in journeys
            if journey["completed"]
        )

        return {
            "total_customers":
                len(customers),
            "total_journeys":
                len(journeys),
            "completed_journeys":
                completed,
            "completion_rate":
                round(
                    completed * 100 / len(journeys),
                    2,
                )
                if journeys
                else 0,
        }

    ####################################################################
    # Usage Overview
    ####################################################################

    def usage_overview(
        self,
    ) -> dict[str, Any]:
        """
        Returns overall usage statistics.
        """

        journeys = self._journeys()

        total_events = sum(
            journey["event_count"]
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
            "total_events":
                total_events,
            "average_events_per_journey":
                average_events,
        }

    ####################################################################
    # Workflow Overview
    ####################################################################

    def workflow_overview(
        self,
    ) -> dict[str, Any]:
        """
        Returns workflow usage.
        """

        workflow_usage = {}

        for journey in self._journeys():

            workflow = journey["workflow"]

            workflow_usage[workflow] = (
                workflow_usage.get(
                    workflow,
                    0,
                )
                + 1
            )

        return {
            "workflow_usage":
                workflow_usage,
        }

    ####################################################################
    # Feature Overview
    ####################################################################

    def feature_overview(
        self,
    ) -> dict[str, Any]:
        """
        Returns feature adoption.
        """

        features = {}

        for journey in self._journeys():

            for feature in journey["features"]:

                features[feature] = (
                    features.get(
                        feature,
                        0,
                    )
                    + 1
                )

        return {
            "feature_count":
                len(features),
            "features":
                features,
        }

         ####################################################################
    # Dashboard Summary
    ####################################################################

    def dashboard_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns the complete dashboard summary.
        """

        return {
            "customer_overview":
                self.customer_overview(),
            "usage_overview":
                self.usage_overview(),
            "workflow_overview":
                self.workflow_overview(),
            "feature_overview":
                self.feature_overview(),
        }

    ####################################################################
    # Dashboard Statistics
    ####################################################################

    def dashboard_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns high-level dashboard statistics.
        """

        customer = self.customer_overview()
        usage = self.usage_overview()
        feature = self.feature_overview()

        return {
            "customers":
                customer["total_customers"],
            "journeys":
                customer["total_journeys"],
            "completed_journeys":
                customer["completed_journeys"],
            "events":
                usage["total_events"],
            "features":
                feature["feature_count"],
        }

    ####################################################################
    # Executive Summary
    ####################################################################

    def executive_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns executive-level customer intelligence summary.
        """

        customer = self.customer_overview()
        usage = self.usage_overview()
        feature = self.feature_overview()

        return {
            "platform_status":
                "Operational",
            "customers":
                customer["total_customers"],
            "journeys":
                customer["total_journeys"],
            "completion_rate":
                customer["completion_rate"],
            "usage_events":
                usage["total_events"],
            "feature_count":
                feature["feature_count"],
            "dashboard_ready":
                True,
        }


         ####################################################################
    # Export APIs
    ####################################################################

    def export_dashboard(
        self,
    ) -> dict[str, Any]:
        """
        Returns complete dashboard export.
        """

        return {
            "dashboard_summary":
                self.dashboard_summary(),
            "dashboard_statistics":
                self.dashboard_statistics(),
            "executive_summary":
                self.executive_summary(),
        }

    ####################################################################
    # Service Summary
    ####################################################################

    def service_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns a high-level service summary.
        """

        return {
            "service":
                "CustomerIntelligenceDashboardService",
            "ready":
                self.is_ready(),
            "health":
                self.health_check(),
            "information":
                self.service_information(),
            "statistics":
                self.dashboard_statistics(),
        }

     
