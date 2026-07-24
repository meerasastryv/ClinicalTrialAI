"""
main_m05.py

IC-08
Milestone 5

Journey Statistics Engine Demo
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

from src.ic08.services.navigation_analytics_service import (
    NavigationAnalyticsService,
)

from src.ic08.services.funnel_analysis_service import (
    FunnelAnalysisService,
)

from src.ic08.services.dropoff_analysis_service import (
    DropoffAnalysisService,
)

from src.ic08.services.journey_statistics_service import (
    JourneyStatisticsService,
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
    # Analytics Services
    ############################################################

    navigation_service = NavigationAnalyticsService(
        journey_builder,
    )

    funnel_service = FunnelAnalysisService(
        journey_builder,
        navigation_service,
    )
      
    dropoff_service = DropoffAnalysisService(
        journey_builder=journey_builder,
        navigation_service=navigation_service,
	funnel_service=funnel_service,
    )

    ############################################################
    # Journey Statistics Service
    ############################################################

    statistics_service = JourneyStatisticsService(
        journey_builder=journey_builder,
        navigation_service=navigation_service,
        funnel_service=funnel_service,
        dropoff_service=dropoff_service,
    )

         ############################################################
    # Journey Statistics
    ############################################################

    print_heading("Journey Statistics")
    journey = statistics_service.journey_statistics()
    print_kv("Total Journeys",
         journey["total_journeys"])
    print_kv("Completed Journeys",
         journey["completed_journeys"])
    print_kv("Abandoned Journeys",
         journey["abandoned_journeys"])
    print_kv("Completion Rate",
         f'{journey["completion_rate"]}%')
    print_kv("Abandonment Rate",
         f'{journey["abandonment_rate"]}%')
    ############################################################
    # Journey Duration Statistics
    ############################################################
    print_heading("Journey Duration Statistics")
    duration = statistics_service.journey_duration_statistics()
    print_kv("Average Duration (sec)",duration["average_duration_seconds"],)
    print_kv("Longest Journey",duration["longest_journey"],)
    print_kv("Shortest Journey",duration["shortest_journey"],) 
    ############################################################
    # Journey Summary
    ############################################################
    print_heading("Journey Summary")
    summary = statistics_service.journey_summary()
    print_kv("Total Customers",summary["total_customers"],)
    print_kv("Total Workflows",summary["total_workflows"],)
    ############################################################
    # Navigation Statistics
    ############################################################
    print_heading("Navigation Statistics")
    navigation = statistics_service.navigation_statistics()
    pages = navigation["page_statistics"]
    print_kv("Unique Pages",pages["total_unique_pages"],)
    print_kv("Page Visits",pages["total_page_visits"],)
    print_kv("Average Pages/Journey",pages["average_pages_per_journey"],)
    print_kv("Most Visited Pages",pages["most_visited_pages"],)
    ############################################################
    # Funnel Statistics
    ############################################################

    funnel = [
        "Home",
        "Search",
        "Details",
        "Checkout",
        "Confirmation",
    ]
    print_heading("Funnel Statistics")
    funnel_stats = statistics_service.funnel_statistics(funnel,)
    summary = funnel_stats["funnel_summary"]
    print_kv("Journeys Entering",summary["journeys_entering"],)
    print_kv("Journeys Completed",summary["journeys_completed"],)
    print_kv("Overall Conversion %",summary["overall_conversion_rate"],)

    ############################################################
    # Navigation + Funnel
    ############################################################
    """
    print_heading(
        "Navigation + Funnel Statistics"
    )

    print(
        statistics_service.navigation_funnel_statistics(
            funnel,
        )
    )
    """
    ############################################################
    # Customer Statistics
    ############################################################

    print_heading("Customer Statistics")
    customer = statistics_service.customer_statistics()
    print_kv("Total Customers",customer["total_customers"],)
    print_kv("Highest Dropoff Customer",customer["highest_dropoff_customer"],)
    ############################################################
    # Workflow Statistics
    ############################################################
    print_heading("Workflow Statistics")
    workflow = statistics_service.workflow_statistics()
    print_kv( "Total Workflows", workflow["total_workflows"],)
    print_kv( "Highest Dropoff Workflow",workflow["highest_dropoff_workflow"],)
    ############################################################
    # Drop-off Statistics
    ############################################################

    print_heading("Drop-off Statistics")
    dropoff = statistics_service.dropoff_statistics()
    page_stats = dropoff["page_statistics"]
    print_kv("Total Exit Pages",page_stats["total_exit_pages"],)
    print_kv("Total Dropoffs",page_stats["total_dropoffs"],)
    print_kv("Highest Dropoff Pages",page_stats["highest_dropoff_pages"],)


    ############################################################
    # Dashboard Summary
    ############################################################
    """
    print_heading(
        "Dashboard Summary"
    )

    print(
        statistics_service.dashboard_summary(
            funnel,
        )
    )
    """
    ############################################################
    # Export Statistics
    ############################################################
    """
    print_heading(
        "Export Statistics"
    )

    print(
        statistics_service.export_statistics(
            funnel,
        )
    )
    """
    ############################################################
    # Platform KPIs
    ############################################################
    """
    print_heading(
        "Platform KPIs"
    )

    print(
        statistics_service.platform_kpis(
            funnel,
        )
    )
    """
    ############################################################
    # Overall Statistics
    ############################################################
    """
    print_heading(
        "Overall Statistics"
    )

    print(
        statistics_service.overall_statistics(
            funnel,
        )
    )
    """
    ############################################################
    # Analytics Summary
    ############################################################
    """
    print_heading(
        "Analytics Summary"
    )

    print(
        statistics_service.analytics_summary(
            funnel,
        )
    )
    """
    ############################################################
    # Health Check
    ############################################################

    print_heading("Health Check")
    health = statistics_service.health_check()
    print_kv("Status",health["status"],)
    print_kv("Journeys Processed",health["journeys_processed"],)
    print_kv("Customers",health["customers"],)
    print_kv("Workflows",health["workflows"],)
    ############################################################
    # Service Information
    ############################################################
    print_heading("Service Information")
    info = statistics_service.service_information()
    print_kv("Service",info["service"],)
    print_kv("Version",info["version"],)
    print_kv("Status",info["status"],)
    print_kv("Module",info["module"],)

    ############################################################
    # Service Summary
    ############################################################
    """
    print_heading(
        "Service Summary"
    )
    print(
        statistics_service.service_summary()
    )
    """
    print("\n")
    print("=" * 70)
    print("Journey Statistics Demo Completed Successfully")
    print("=" * 70)


if __name__ == "__main__":
    main()
