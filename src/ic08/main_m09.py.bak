"""
main_m09.py

IC-08
Milestone 9

Customer Intelligence Dashboard Demo
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

from src.ic08.services.customer_intelligence_dashboard_service import (
    CustomerIntelligenceDashboardService,
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
    # Customer Intelligence Dashboard Service
    ############################################################

    dashboard_service = (
        CustomerIntelligenceDashboardService(
            journey_builder=journey_builder,
        )
    )

    ############################################################
    # Customer Overview
    ############################################################

    print_heading("Customer Overview")

    customer = (
        dashboard_service.customer_overview()
    )

    print_kv(
        "Total Customers",
        customer["total_customers"],
    )

    print_kv(
        "Total Journeys",
        customer["total_journeys"],
    )

    print_kv(
        "Completed Journeys",
        customer["completed_journeys"],
    )

    print_kv(
        "Completion Rate",
        f'{customer["completion_rate"]}%',
    )

    ############################################################
    # Usage Overview
    ############################################################

    print_heading("Usage Overview")

    usage = (
        dashboard_service.usage_overview()
    )

    print_kv(
        "Total Events",
        usage["total_events"],
    )

    print_kv(
        "Average Events / Journey",
        usage[
            "average_events_per_journey"
        ],
    )

    ############################################################
    # Workflow Overview
    ############################################################

    print_heading("Workflow Overview")

    workflow = (
        dashboard_service.workflow_overview()
    )

    if workflow["workflow_usage"]:

        for name, count in (
            workflow["workflow_usage"].items()
        ):

            print_kv(
                name,
                count,
            )

    else:

        print("No workflow usage available.")

    ############################################################
    # Feature Overview
    ############################################################

    print_heading("Feature Overview")

    feature = (
        dashboard_service.feature_overview()
    )

    print_kv(
        "Feature Count",
        feature["feature_count"],
    )

    if feature["features"]:

        for name, count in (
            feature["features"].items()
        ):

            print_kv(
                name,
                count,
            )

    else:

        print("No feature adoption available.")


    ############################################################
    # Dashboard Summary
    ############################################################

    print_heading("Dashboard Summary")

    dashboard = (
        dashboard_service.dashboard_summary()
    )

    print(dashboard)

    ############################################################
    # Dashboard Statistics
    ############################################################

    print_heading("Dashboard Statistics")

    statistics = (
        dashboard_service.dashboard_statistics()
    )

    print_kv(
        "Customers",
        statistics["customers"],
    )

    print_kv(
        "Journeys",
        statistics["journeys"],
    )

    print_kv(
        "Completed Journeys",
        statistics["completed_journeys"],
    )

    print_kv(
        "Events",
        statistics["events"],
    )

    print_kv(
        "Features",
        statistics["features"],
    )

    ############################################################
    # Executive Summary
    ############################################################

    print_heading("Executive Summary")

    executive = (
        dashboard_service.executive_summary()
    )

    print_kv(
        "Platform Status",
        executive["platform_status"],
    )

    print_kv(
        "Customers",
        executive["customers"],
    )

    print_kv(
        "Journeys",
        executive["journeys"],
    )

    print_kv(
        "Completion Rate",
        f'{executive["completion_rate"]}%',
    )

    print_kv(
        "Usage Events",
        executive["usage_events"],
    )

    print_kv(
        "Feature Count",
        executive["feature_count"],
    )

    print_kv(
        "Dashboard Ready",
        executive["dashboard_ready"],
    )

    ############################################################
    # Export Dashboard
    ############################################################

    print_heading("Export Dashboard")

    export_dashboard = (
        dashboard_service.export_dashboard()
    )

    print(export_dashboard)

    ############################################################
    # Health Check
    ############################################################

    print_heading("Health Check")

    health = (
        dashboard_service.health_check()
    )

    print_kv(
        "Status",
        health["status"],
    )

    print_kv(
        "Journeys",
        health["journeys"],
    )

    ############################################################
    # Service Information
    ############################################################

    print_heading("Service Information")

    information = (
        dashboard_service.service_information()
    )

    print_kv(
        "Service",
        information["service"],
    )

    print_kv(
        "Module",
        information["module"],
    )

    print_kv(
        "Version",
        information["version"],
    )

    print_kv(
        "Status",
        information["status"],
    )

    ############################################################
    # Service Summary
    ############################################################

    print_heading("Service Summary")

    summary = (
        dashboard_service.service_summary()
    )

    print(summary)

    ############################################################
    # Readiness
    ############################################################

    print_heading("Readiness")

    print_kv(
        "Service Ready",
        dashboard_service.is_ready(),
    )

    ############################################################
    # Demo Complete
    ############################################################

    print()
    print("=" * 70)
    print(
        "Customer Intelligence Dashboard Demo Completed Successfully"
    )
    print("=" * 70)


if __name__ == "__main__":
    main()
