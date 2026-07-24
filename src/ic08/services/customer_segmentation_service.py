"""
customer_segmentation_service.py

Customer Segmentation Engine

Provides customer segmentation based on usage patterns.
"""

from __future__ import annotations

import logging
from collections import Counter
from typing import Any

from src.ic08.services.customer_journey_builder import (
    CustomerJourneyBuilder,
)

logger = logging.getLogger(__name__)


class CustomerSegmentationService:
    """
    Customer Segmentation Service.
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
            "CustomerSegmentationService initialized."
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

    def _customers(
        self,
    ) -> list[str]:
        """
        Returns unique customer ids.
        """

        return sorted(
            {
                journey["customer_id"]
                for journey in self._journeys()
            }
        )

    ####################################################################
    # Customer Profiles
    ####################################################################

    def customer_profile(
        self,
        customer_id: str,
    ) -> dict[str, Any]:
        """
        Builds a customer profile.
        """

        journeys = [
            journey
            for journey in self._journeys()
            if journey["customer_id"] == customer_id
        ]

        workflows = Counter(
            journey["workflow"]
            for journey in journeys
        )

        total_events = sum(
            journey["event_count"]
            for journey in journeys
        )

        return {
            "customer_id": customer_id,
            "journeys": len(journeys),
            "events": total_events,
            "workflows": dict(workflows),
            "completed_journeys": sum(
                1
                for journey in journeys
                if journey["completed"]
            ),
        }

    def all_customer_profiles(
        self,
    ) -> list[dict[str, Any]]:
        """
        Returns all customer profiles.
        """

        return [
            self.customer_profile(customer)
            for customer in self._customers()
        ]

    ####################################################################
    # Health Check
    ####################################################################

    def health_check(
        self,
    ) -> dict[str, Any]:

        return {
            "status": "healthy",
            "service": "CustomerSegmentationService",
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
            "service": "CustomerSegmentationService",
            "module": "IC-08 Customer Usage Intelligence",
            "version": "1.0",
            "status": "Ready",
        }

         ####################################################################
    # Customer Segmentation
    ####################################################################

    def customer_segment(
        self,
        customer_id: str,
    ) -> str:
        """
        Determines the segment for a customer.
        """

        profile = self.customer_profile(customer_id)

        journeys = profile["journeys"]
        events = profile["events"]
        completed = profile["completed_journeys"]

        if journeys == 0:
            return "Inactive"

        if journeys == 1:
            return "New"

        if journeys >= 10 and events >= 100:
            return "Power User"

        if completed >= max(1, journeys * 0.8):
            return "Active"

        return "At Risk"

    def all_segments(
        self,
    ) -> dict[str, str]:
        """
        Returns the segment for every customer.
        """

        return {
            customer: self.customer_segment(customer)
            for customer in self._customers()
        }

    def segment_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns statistics for customer segments.
        """

        segments = Counter(
            self.all_segments().values()
        )

        total = sum(segments.values())

        percentages = {}

        if total > 0:
            percentages = {
                segment: round(
                    count * 100 / total,
                    2,
                )
                for segment, count in segments.items()
            }

        return {
            "total_customers": total,
            "segment_counts": dict(segments),
            "segment_percentages": percentages,
        }

         ####################################################################
    # Segment Reporting
    ####################################################################

    def segment_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns a summary of customer segmentation.
        """

        statistics = self.segment_statistics()

        counts = statistics["segment_counts"]

        if counts:
            largest_segment = max(
                counts,
                key=counts.get,
            )

            smallest_segment = min(
                counts,
                key=counts.get,
            )
        else:
            largest_segment = None
            smallest_segment = None

        return {
            "total_customers":
                statistics["total_customers"],
            "largest_segment":
                largest_segment,
            "smallest_segment":
                smallest_segment,
            "segment_counts":
                counts,
            "segment_percentages":
                statistics["segment_percentages"],
        }

    def customer_segment_report(
        self,
    ) -> list[dict[str, Any]]:
        """
        Returns customer segmentation report.
        """

        report = []

        for profile in self.all_customer_profiles():

            report.append(
                {
                    "customer_id":
                        profile["customer_id"],
                    "segment":
                        self.customer_segment(
                            profile["customer_id"],
                        ),
                    "journeys":
                        profile["journeys"],
                    "events":
                        profile["events"],
                    "completed_journeys":
                        profile["completed_journeys"],
                }
            )

        return report

    ####################################################################
    # Dashboard
    ####################################################################

    def dashboard_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns dashboard-ready segmentation summary.
        """

        return {
            "summary":
                self.segment_summary(),
            "customer_count":
                len(self._customers()),
            "journey_count":
                len(self._journeys()),
        }

         ####################################################################
    # Export APIs
    ####################################################################

    def export_statistics(
        self,
    ) -> dict[str, Any]:
        """
        Returns complete segmentation analytics.
        """

        return {
            "summary":
                self.segment_summary(),
            "customer_report":
                self.customer_segment_report(),
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
        Returns a high-level service summary.
        """

        return {
            "service":
                "CustomerSegmentationService",
            "ready":
                self.health_check()["status"] == "healthy",
            "health":
                self.health_check(),
            "information":
                self.service_information(),
            "statistics":
                self.segment_statistics(),
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


