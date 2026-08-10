"""
main_m10.py

IC-08
Milestone 10

Customer AI Insights Demo
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

from src.ic08.services.customer_ai_insights_service import (
    CustomerAIInsightsService,
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
    # Customer AI Insights Service
    ############################################################

    ai_service = CustomerAIInsightsService(
        journey_builder=journey_builder,
    )

    ############################################################
    # Customer Insights
    ############################################################

    print_heading("Customer Insights")

    customer = ai_service.customer_insights()

    print_kv(
        "Customers",
        customer["customers"],
    )

    print_kv(
        "Journeys",
        customer["journeys"],
    )

    print_kv(
        "Completed Journeys",
        customer["completed_journeys"],
    )

    print_kv(
        "Completion Rate",
        f'{customer["completion_rate"]}%',
    )

    print_kv(
        "Usage Events",
        customer["usage_events"],
    )

    print_kv(
        "Average Events / Journey",
        customer[
            "average_events_per_journey"
        ],
    )

    ############################################################
    # Workflow Insights
    ############################################################

    print_heading("Workflow Insights")

    workflow = ai_service.workflow_insights()

    print_kv(
        "Workflow Count",
        workflow["workflow_count"],
    )

    if workflow["workflows"]:

        for name, count in workflow[
            "workflows"
        ].items():

            print_kv(
                name,
                count,
            )

    else:

        print("No workflow usage available.")

    ############################################################
    # Feature Insights
    ############################################################

    print_heading("Feature Insights")

    feature = ai_service.feature_insights()

    print_kv(
        "Feature Count",
        feature["feature_count"],
    )

    if feature["features"]:

        for name, count in feature[
            "features"
        ].items():

            print_kv(
                name,
                count,
            )

    else:

        print("No feature adoption available.")



         ############################################################
    # Recommendations
    ############################################################

    print_heading("Recommendations")

    recommendations = (
        ai_service.recommendations()
    )

    if recommendations:

        for index, recommendation in enumerate(
            recommendations,
            start=1,
        ):

            print_kv(
                f"Recommendation {index}",
                recommendation,
            )

    else:

        print("No recommendations available.")

    ############################################################
    # Executive Summary
    ############################################################

    print_heading("Executive Summary")

    executive = (
        ai_service.executive_summary()
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
        "Recommendation Count",
        executive["recommendation_count"],
    )

    print_kv(
        "Ready",
        executive["ready"],
    )

    ############################################################
    # Export Insights
    ############################################################

    print_heading("Export Insights")

    export_data = (
        ai_service.export_insights()
    )

    print(export_data)

    ############################################################
    # Health Check
    ############################################################

    print_heading("Health Check")

    health = (
        ai_service.health_check()
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
        ai_service.service_information()
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
        ai_service.service_summary()
    )

    print(summary)

    ############################################################
    # Readiness
    ############################################################

    print_heading("Readiness")

    print_kv(
        "Service Ready",
        ai_service.is_ready(),
    )

    ############################################################
    # Demo Complete
    ############################################################

    print()
    print("=" * 70)
    print(
        "Customer AI Insights Demo Completed Successfully"
    )
    print("=" * 70)


if __name__ == "__main__":
    main()
