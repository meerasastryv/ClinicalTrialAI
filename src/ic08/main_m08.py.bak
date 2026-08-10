"""
main_m08.py

IC-08
Milestone 8

Customer Segmentation Engine Demo
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

from src.ic08.services.customer_segmentation_service import (
    CustomerSegmentationService,
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
    # Customer Segmentation Service
    ############################################################

    segmentation_service = CustomerSegmentationService(
        journey_builder=journey_builder,
    )

    ############################################################
    # Customer Profiles
    ############################################################

    print_heading("Customer Profiles")

    profiles = (
        segmentation_service.all_customer_profiles()
    )

    if profiles:

        for profile in profiles:
            print(profile)

    else:

        print("No customer profiles available.")

    ############################################################
    # Customer Segments
    ############################################################

    print_heading("Customer Segments")

    segments = (
        segmentation_service.all_segments()
    )

    if segments:

        for customer, segment in segments.items():

            print_kv(
                customer,
                segment,
            )

    else:

        print("No customer segments available.")

    ############################################################
    # Segment Statistics
    ############################################################

    print_heading("Segment Statistics")

    statistics = (
        segmentation_service.segment_statistics()
    )

    print_kv(
        "Total Customers",
        statistics["total_customers"],
    )

    print()

    print("Segment Counts")

    for segment, count in (
        statistics["segment_counts"].items()
    ):

        print_kv(
            segment,
            count,
        )

    print()

    print("Segment Percentages")

    for segment, percentage in (
        statistics[
            "segment_percentages"
        ].items()
    ):

        print_kv(
            segment,
            f"{percentage}%",
        )

    ############################################################
    # Segment Summary
    ############################################################

    print_heading("Segment Summary")

    summary = (
        segmentation_service.segment_summary()
    )

    print_kv(
        "Total Customers",
        summary["total_customers"],
    )

    print_kv(
        "Largest Segment",
        summary["largest_segment"],
    )

    print_kv(
        "Smallest Segment",
        summary["smallest_segment"],
    )



         ############################################################
    # Customer Segment Report
    ############################################################

    print_heading("Customer Segment Report")

    report = (
        segmentation_service.customer_segment_report()
    )

    if report:

        for customer in report:
            print(customer)

    else:

        print("No customer segment report available.")

    ############################################################
    # Dashboard Summary
    ############################################################

    print_heading("Dashboard Summary")

    dashboard = (
        segmentation_service.dashboard_summary()
    )

    print(dashboard)

    ############################################################
    # Export Statistics
    ############################################################

    print_heading("Export Statistics")

    export_statistics = (
        segmentation_service.export_statistics()
    )

    print(export_statistics)

    ############################################################
    # Health Check
    ############################################################

    print_heading("Health Check")

    health = (
        segmentation_service.health_check()
    )

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

    info = (
        segmentation_service.service_information()
    )

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

    service_summary = (
        segmentation_service.service_summary()
    )

    print(service_summary)

    ############################################################
    # Readiness
    ############################################################

    print_heading("Readiness")

    print_kv(
        "Service Ready",
        segmentation_service.is_ready(),
    )

    ############################################################
    # Demo Complete
    ############################################################

    print()
    print("=" * 70)
    print(
        "Customer Segmentation Demo Completed Successfully"
    )
    print("=" * 70)


if __name__ == "__main__":
    main()
