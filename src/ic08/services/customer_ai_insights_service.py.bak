"""
customer_ai_insights_service.py

Customer AI Insights Service

Provides AI-style customer insights and recommendations
based on customer usage intelligence.
"""

from __future__ import annotations

import logging
from typing import Any

from src.ic08.services.customer_journey_builder import (
    CustomerJourneyBuilder,
)

logger = logging.getLogger(__name__)


class CustomerAIInsightsService:
    """
    Customer AI Insights Service.
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
            "CustomerAIInsightsService initialized."
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
            "service": "CustomerAIInsightsService",
            "journeys": len(self._journeys()),
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
            "service": "CustomerAIInsightsService",
            "module": "IC-08 Customer Usage Intelligence",
            "version": "1.0",
            "status": "Ready",
        }
         ####################################################################
    # Customer Insights
    ####################################################################

    def customer_insights(
        self,
    ) -> dict[str, Any]:
        """
        Generates customer usage insights.
        """

        journeys = self._journeys()

        total_customers = len(
            {
                journey["customer_id"]
                for journey in journeys
            }
        )

        total_journeys = len(journeys)

        completed = sum(
            1
            for journey in journeys
            if journey["completed"]
        )

        total_events = sum(
            journey["event_count"]
            for journey in journeys
        )

        completion_rate = (
            round(
                completed * 100 / total_journeys,
                2,
            )
            if total_journeys
            else 0
        )

        average_events = (
            round(
                total_events / total_journeys,
                2,
            )
            if total_journeys
            else 0
        )

        return {
            "customers":
                total_customers,
            "journeys":
                total_journeys,
            "completed_journeys":
                completed,
            "completion_rate":
                completion_rate,
            "usage_events":
                total_events,
            "average_events_per_journey":
                average_events,
        }

    ####################################################################
    # Workflow Insights
    ####################################################################

    def workflow_insights(
        self,
    ) -> dict[str, Any]:
        """
        Generates workflow insights.
        """

        workflows = {}

        for journey in self._journeys():

            workflow = journey["workflow"]

            workflows[workflow] = (
                workflows.get(
                    workflow,
                    0,
                )
                + 1
            )

        return {
            "workflow_count":
                len(workflows),
            "workflows":
                workflows,
        }

    ####################################################################
    # Feature Insights
    ####################################################################

    def feature_insights(
        self,
    ) -> dict[str, Any]:
        """
        Generates feature adoption insights.
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
    # Recommendations
    ####################################################################

    def recommendations(
        self,
    ) -> list[str]:
        """
        Generates AI-style recommendations.
        """

        insights = self.customer_insights()

        recommendations = []

        if insights["customers"] == 0:
            recommendations.append(
                "No customer activity detected. "
                "Collect usage data before generating insights."
            )

        if insights["completion_rate"] < 70:
            recommendations.append(
                "Improve customer journey completion "
                "through onboarding and guidance."
            )

        if insights["average_events_per_journey"] < 5:
            recommendations.append(
                "Encourage deeper product engagement "
                "through feature discovery."
            )

        feature = self.feature_insights()

        if feature["feature_count"] < 5:
            recommendations.append(
                "Increase adoption of additional "
                "product features."
            )

        workflow = self.workflow_insights()

        if workflow["workflow_count"] < 3:
            recommendations.append(
                "Promote broader workflow usage "
                "across customers."
            )

        if not recommendations:
            recommendations.append(
                "Customer engagement appears healthy."
            )

        return recommendations

    ####################################################################
    # Executive Summary
    ####################################################################

    def executive_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns executive AI insights.
        """

        insights = self.customer_insights()

        return {
            "platform_status":
                "Operational",
            "customers":
                insights["customers"],
            "journeys":
                insights["journeys"],
            "completion_rate":
                insights["completion_rate"],
            "recommendation_count":
                len(self.recommendations()),
            "ready":
                True,
        }

         ####################################################################
    # Export APIs
    ####################################################################

    def export_insights(
        self,
    ) -> dict[str, Any]:
        """
        Returns complete AI insights export.
        """

        return {
            "customer_insights":
                self.customer_insights(),
            "workflow_insights":
                self.workflow_insights(),
            "feature_insights":
                self.feature_insights(),
            "recommendations":
                self.recommendations(),
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
                "CustomerAIInsightsService",
            "ready":
                self.is_ready(),
            "health":
                self.health_check(),
            "information":
                self.service_information(),
            "customer_statistics":
                self.customer_insights(),
            "workflow_statistics":
                self.workflow_insights(),
            "feature_statistics":
                self.feature_insights(),
            "recommendation_count":
                len(self.recommendations()),
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


     
