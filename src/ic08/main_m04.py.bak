"""
IC-08 Customer Usage Intelligence Engine

PART 4
Milestone 4

Navigation Analytics Demo
"""

from __future__ import annotations

from pprint import pprint

from src.ic08.repositories.customer_repository import CustomerRepository
from src.ic08.repositories.feature_repository import FeatureRepository
from src.ic08.repositories.session_repository import SessionRepository
from src.ic08.repositories.usage_repository import UsageRepository

from src.ic08.services.customer_journey_builder import (
    CustomerJourneyBuilder,
)
from src.ic08.services.navigation_analytics_service import (
    NavigationAnalyticsService,
)


def print_header(title: str) -> None:
    print("\n" + "=" * 80)
    print(title)
    print("=" * 80)


def main() -> None:
    # Repository Initialization
    usage_repository = UsageRepository()
    session_repository = SessionRepository()
    from src.ic08.repositories.workflow_repository import (WorkflowRepository,)
    workflow_repository = WorkflowRepository()
    # Service Initialization
    from src.ic08.services.usage_event_service import (
        UsageEventService,)
    from src.ic08.services.session_tracking_service import (
        SessionTrackingService,)
    from src.ic08.services.workflow_tracking_service import (
        WorkflowTrackingService,)
    usage_event_service = UsageEventService(
        usage_repository)
    session_tracking_service = SessionTrackingService(
        session_repository)
    workflow_tracking_service = WorkflowTrackingService(
        workflow_repository)
    # Journey Builder
    journey_builder = CustomerJourneyBuilder(
    usage_event_service=usage_event_service,
    session_tracking_service=session_tracking_service,
    workflow_tracking_service=workflow_tracking_service,)
    # Navigation Analytics Service
    navigation = NavigationAnalyticsService(
        journey_builder=journey_builder,)
    # Navigation Statistics
    ####################################################################

    print_header("2. NAVIGATION STATISTICS")

    pprint(navigation.navigation_statistics())

    ####################################################################
    # Transition Matrix
    ####################################################################

    print_header("3. TRANSITION MATRIX")

    pprint(navigation.transition_matrix())

    ####################################################################
    # Entry / Exit Analytics
    ####################################################################

    print_header("4. ENTRY / EXIT ANALYTICS")

    pprint(navigation.entry_exit_statistics())

    ####################################################################
    # Bounce Analytics
    ####################################################################

    print_header("5. BOUNCE ANALYTICS")

    pprint(navigation.bounce_statistics())

    ####################################################################
    # Dashboard Summary
    ####################################################################

    print_header("6. DASHBOARD SUMMARY")

    pprint(navigation.dashboard_summary())

    ####################################################################
    # Export APIs
    ####################################################################

    print_header("7. EXPORT NAVIGATION STATISTICS")

    pprint(navigation.export_navigation_statistics())

    ####################################################################
    # Health Check
    ####################################################################

    print_header("8. HEALTH CHECK")

    pprint(navigation.health_check())

    ####################################################################
    # Service Information
    ####################################################################

    print_header("9. SERVICE INFORMATION")

    pprint(navigation.service_information())

    print("\nNavigation Analytics Demo Completed Successfully.")


if __name__ == "__main__":
    main()
