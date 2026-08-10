"""
main_m07.py

IC-08
Milestone 7

Trend Analytics Engine Demo
"""

from __future__ import annotations

import logging

# ==========================================================
# Repositories
# ==========================================================

from src.ic08.repositories.session_repository import (
    SessionRepository,
)

from src.ic08.repositories.usage_repository import (
    UsageRepository,
)

from src.ic08.repositories.workflow_repository import (
    WorkflowRepository,
)

# ==========================================================
# Services
# ==========================================================

from src.ic08.services.session_tracking_service import (
    SessionTrackingService,
)

from src.ic08.services.usage_event_service import (
    UsageEventService,
)

from src.ic08.services.workflow_tracking_service import (
    WorkflowTrackingService,
)

from src.ic08.services.customer_journey_builder import (
    CustomerJourneyBuilder,
)

from src.ic08.services.trend_analytics_service import (
    TrendAnalyticsService,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


def print_heading(title: str) -> None:
    print()
    print("=" * 70)
    print(title)
    print("=" * 70)


def print_kv(label: str, value) -> None:
    """
    Prints a KPI in a consistent format.
    """

    print(f"{label:<35}: {value}")


def main() -> None:

    ############################################################
    # Repositories
    ############################################################

    usage_repository = UsageRepository()

    session_repository = SessionRepository()

    workflow_repository = WorkflowRepository()

    ############################################################
    # Services
    ############################################################

    usage_service = UsageEventService(
        usage_repository,
    )

    session_service = SessionTrackingService(
        session_repository,
    )

    workflow_service = WorkflowTrackingService(
        workflow_repository,
    )

    ############################################################
    # Journey Builder
    ############################################################

    journey_builder = CustomerJourneyBuilder(
        usage_event_service=usage_service,
        session_tracking_service=session_service,
        workflow_tracking_service=workflow_service,
    )

    ############################################################
    # Trend Analytics Service
    ############################################################

    trend_service = TrendAnalyticsService(
        journey_builder=journey_builder,
    )

    ############################################################
    # Customer Growth Trend
    ############################################################

    print_heading("Customer Growth Trend")

    customer_growth = trend_service.customer_growth_trend()

    print_kv(
        "Total Customers",
        customer_growth["total_customers"],
    )

    print_kv(
        "New Customers",
        customer_growth["new_customers"],
    )

    print_kv(
        "Returning Customers",
        customer_growth["returning_customers"],
    )

    ############################################################
    # Journey Trend
    ############################################################

    print_heading("Journey Trend")

    journey_trend = trend_service.journey_trend()

    print_kv(
        "Total Journeys",
        journey_trend["total_journeys"],
    )

    print_kv(
        "Completed Journeys",
        journey_trend["completed_journeys"],
    )

    print_kv(
        "Completion Rate",
        f'{journey_trend["completion_rate"]}%',
    )

    ############################################################
    # Usage Trend
    ############################################################

    print_heading("Usage Trend")

    usage_trend = trend_service.usage_trend()

    print_kv(
        "Total Events",
        usage_trend["total_events"],
    )

    print_kv(
        "Average Events / Journey",
        usage_trend["average_events_per_journey"],
    )

    ############################################################
    # Workflow Trend
    ############################################################

    print_heading("Workflow Trend")

    workflow_trend = trend_service.workflow_trend()

    workflow_usage = workflow_trend["workflow_usage"]

    if workflow_usage:

        for workflow, count in workflow_usage.items():
            print_kv(
                workflow,
                count,
            )

    else:

        print("No workflow usage available.")

    ############################################################
    # Feature Adoption Trend
    ############################################################

    print_heading("Feature Adoption Trend")

    feature_trend = trend_service.feature_adoption_trend()

    print_kv(
        "Feature Count",
        feature_trend["feature_count"],
    )

    if feature_trend["features"]:

        for feature, count in feature_trend["features"].items():
            print_kv(
                feature,
                count,
            )

    else:

        print("No feature adoption available.")

    ############################################################
    # Customer Engagement
    ############################################################

    print_heading("Customer Engagement")

    engagement = trend_service.customer_engagement_trend()

    print_kv(
        "Average Events / Customer",
        engagement["average_events_per_customer"],
    )

    print_kv(
        "Engaged Customers",
        engagement["engaged_customers"],
    )


    ############################################################
    # Active Customer Trend
    ############################################################

    print_heading("Active Customer Trend")

    active = trend_service.active_customer_trend()

    print_kv(
        "Active Customers",
        active["active_customers"],
    )

    print_kv(
        "Inactive Customers",
        active["inactive_customers"],
    )

    ############################################################
    # Dashboard Summary
    ############################################################

    print_heading("Dashboard Summary")

    dashboard = trend_service.dashboard_summary()

    print_kv(
        "Customers",
        dashboard["customers"],
    )

    print_kv(
        "Journeys",
        dashboard["journeys"],
    )

    ############################################################
    # Health Check
    ############################################################

    print_heading("Health Check")

    health = trend_service.health_check()

    print_kv(
        "Status",
        health["status"],
    )

    print_kv(
        "Customers",
        health["customers"],
    )

    print_kv(
        "Journeys",
        health["journeys"],
    )

    ############################################################
    # Service Information
    ############################################################

    print_heading("Service Information")

    info = trend_service.service_information()

    print_kv(
        "Service",
        info["service"],
    )

    print_kv(
        "Module",
        info["module"],
    )

    print_kv(
        "Version",
        info["version"],
    )

    print_kv(
        "Status",
        info["status"],
    )

    ############################################################
    # Service Summary
    ############################################################

    print_heading("Service Summary")

    summary = trend_service.service_summary()

    print_kv(
        "Ready",
        summary["ready"],
    )

    ############################################################
    # Demo Complete
    ############################################################

    print()
    print("=" * 70)
    print("Trend Analytics Demo Completed Successfully")
    print("=" * 70)


if __name__ == "__main__":
    main()    
