"""
IC-08 - Customer Usage Intelligence

Milestone 3
Customer Journey Analytics

main_m03.py
"""

from __future__ import annotations

import logging
from datetime import UTC, datetime, timedelta

from src.ic08.models.customer import Customer
from src.ic08.models.customer_session import CustomerSession
from src.ic08.models.usage_event import UsageEvent

from src.ic08.repositories.customer_repository import CustomerRepository
from src.ic08.repositories.session_repository import SessionRepository
from src.ic08.repositories.usage_repository import UsageRepository
from src.ic08.repositories.feature_repository import FeatureRepository
from src.ic08.repositories.workflow_repository import WorkflowRepository

from src.ic08.services.session_tracking_service import (
    SessionTrackingService,
)

from src.ic08.services.workflow_tracking_service import (
    WorkflowTrackingService,
)

from src.ic08.services.feature_tracking_service import (
    FeatureTrackingService,
)

from src.ic08.services.usage_event_service import (
    UsageEventService,
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

from src.ic08.services.journey_reporting_service import (
    JourneyReportingService,
)

from src.ic08.services.customer_journey_analytics_service import (
    CustomerJourneyAnalyticsService,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
)

logger = logging.getLogger(__name__)

LINE = "=" * 90
SUB_LINE = "-" * 90


def print_banner() -> None:

    print("\n" + LINE)
    print("ClinicalTrialAI")
    print("IC-08 : Customer Usage Intelligence")
    print("Milestone 3 : Customer Journey Analytics")
    print(LINE)


def print_section(title: str) -> None:

    print(f"\n{SUB_LINE}")
    print(title)
    print(SUB_LINE)


class CustomerJourneyAnalyticsDemo:
    """
    Milestone 3 demonstration.
    """

    def __init__(self) -> None:

        logger.info(
            "Initializing Customer Journey Analytics Demo..."
        )

        #
        # Repositories
        #

        self.customer_repository = CustomerRepository()

        self.session_repository = SessionRepository()

        self.usage_repository = UsageRepository()

        self.feature_repository = FeatureRepository()

        self.workflow_repository = WorkflowRepository()

        #
        # Core Services
        #

        self.session_service = SessionTrackingService(
            self.session_repository
        )

        self.workflow_service = WorkflowTrackingService(
            self.workflow_repository
        )

        self.feature_service = FeatureTrackingService(
            self.feature_repository
        )

        self.usage_service = UsageEventService(
            self.usage_repository
        )

        #
        # Journey Builder
        #

        self.journey_builder = CustomerJourneyBuilder(
            usage_event_service=self.usage_service,
            session_tracking_service=self.session_service,
            workflow_tracking_service=self.workflow_service,
        )

        #
        # Analytics Services
        #

        self.navigation_service = NavigationAnalyticsService(
            self.journey_builder
        )

        self.funnel_service = FunnelAnalysisService(
            self.journey_builder,
            self.navigation_service,
        )

        self.dropoff_service = DropoffAnalysisService(
            self.journey_builder,
            self.navigation_service,
            self.funnel_service,
        )

        self.statistics_service = JourneyStatisticsService(
            self.journey_builder,
            self.navigation_service,
            self.funnel_service,
            self.dropoff_service,
        )

        self.reporting_service = JourneyReportingService(
            self.journey_builder,
            self.navigation_service,
            self.funnel_service,
            self.dropoff_service,
            self.statistics_service,
        )

        self.analytics_service = (
            CustomerJourneyAnalyticsService(
                journey_builder=self.journey_builder,
                navigation_service=self.navigation_service,
                funnel_service=self.funnel_service,
                dropoff_service=self.dropoff_service,
                statistics_service=self.statistics_service,
                reporting_service=self.reporting_service,
            )
        )

        #
        # Demo Funnel
        #

        self.demo_funnel = [
            "Dashboard",
            "Requirement Search",
            "Test Design",
            "Execution",
            "Reports",
        ]

        logger.info(
            "Repositories initialized successfully."
        )

        logger.info(
            "Services initialized successfully."
        )

     ####################################################################
# Demo Customers
####################################################################

def build_customers(
    self,
) -> list[Customer]:
    """
    Creates demo customers.
    """

    return [

        Customer(
            customer_id="CUS-001",
            customer_name="John Smith",
            organization="Pfizer",
            industry="Pharmaceutical",
            subscription_plan="Enterprise",
            region="USA",
        ),

        Customer(
            customer_id="CUS-002",
            customer_name="Anita Rao",
            organization="Novartis",
            industry="Pharmaceutical",
            subscription_plan="Enterprise",
            region="India",
        ),

        Customer(
            customer_id="CUS-003",
            customer_name="David Miller",
            organization="Roche",
            industry="Healthcare",
            subscription_plan="Professional",
            region="Switzerland",
        ),
    ]


####################################################################
# Demo Sessions
####################################################################
def build_sessions(
    self,
) -> list[CustomerSession]:
    """
    Creates demo sessions.
    """

    now = datetime.now(UTC)

    return [

        CustomerSession(
            session_id="SES-001",
            customer_id="CUS-001",
            user_id="USR-001",
            user_name="John Smith",
            start_time=now - timedelta(minutes=45),
            device="MacBook Pro",
            browser="Chrome",
            operating_system="macOS",
            location="New York",
        ),

        CustomerSession(
            session_id="SES-002",
            customer_id="CUS-002",
            user_id="USR-002",
            user_name="Anita Rao",
            start_time=now - timedelta(minutes=30),
            device="Windows Laptop",
            browser="Edge",
            operating_system="Windows 11",
            location="Bangalore",
        ),

        CustomerSession(
            session_id="SES-003",
            customer_id="CUS-003",
            user_id="USR-003",
            user_name="David Miller",
            start_time=now - timedelta(minutes=15),
            device="MacBook Air",
            browser="Safari",
            operating_system="macOS",
            location="Basel",
        ),
    ]

     ####################################################################
# Load Customers
####################################################################

def load_customers(self) -> None:
    """
    Load demo customers.
    """

    print_section("Loading Customers")

    for customer in self.build_customers():
        self.customer_repository.add_customer(customer)
        print(
            f"Loaded Customer : "
            f"{customer.customer_id} - "
            f"{customer.customer_name}"
        )


####################################################################
# Load Sessions
####################################################################

def load_sessions(self) -> None:
    """
    Load demo sessions.
    """

    print_section("Loading Sessions")

    for session in self.build_sessions():

        self.session_repository.add_session(session)

        print(
            f"Loaded Session : "
            f"{session.session_id}"
        )


####################################################################
# Load Usage Events
####################################################################

def load_usage_events(self) -> None:
    """
    Record usage events.
    """

    print_section("Recording Usage Events")

    for event in self.build_usage_events():

        self.usage_service.record_event(event)

        #
        # Update feature statistics
        #

        self.feature_service.record_feature_usage(
            feature_name=event.feature_name,
            duration_ms=event.duration_ms,
            success=event.success,
        )

        print(
            f"{event.session_id}"
            f" -> "
            f"{event.page_name}"
        )


####################################################################
# Journey Builder
####################################################################

def build_customer_journeys(self) -> None:
    """
    Build all customer journeys.
    """

    print_section("Building Customer Journeys")

    journeys = self.journey_builder.build_all_journeys()

    print(
        f"Total Journeys : {len(journeys)}"
    )

    for journey in journeys:

        print(
            f"{journey['session_id']}  "
            f"{journey['customer_id']}  "
            f"{journey['workflow']}"
        )


     ####################################################################
# Journey Analytics
####################################################################

def print_journey_analytics(self) -> None:

    print_section(
        "Journey Analytics"
    )

    analytics = (
        self.analytics_service
        .journey_analytics()
    )

    for key, value in analytics.items():
        print(f"{key}: {value}")


####################################################################
# Navigation Analytics
####################################################################

def print_navigation_analytics(self) -> None:

    print_section(
        "Navigation Analytics"
    )

    analytics = (
        self.analytics_service
        .navigation_analytics()
    )

    for key, value in analytics.items():
        print(f"{key}: {value}")


####################################################################
# Funnel Analytics
####################################################################

def print_funnel_analytics(self) -> None:

    print_section(
        "Funnel Analytics"
    )

    analytics = (
        self.analytics_service
        .funnel_analytics(
            self.demo_funnel
        )
    )

    for key, value in analytics.items():
        print(f"{key}: {value}")


####################################################################
# Drop-off Analytics
####################################################################

def print_dropoff_analytics(self) -> None:

    print_section(
        "Drop-off Analytics"
    )

    analytics = (
        self.analytics_service
        .dropoff_analytics()
    )

    for key, value in analytics.items():
        print(f"{key}: {value}")


     ####################################################################
# Dashboard
####################################################################

def print_dashboard(self) -> None:
    """
    Displays the dashboard report.
    """

    print_section("Dashboard")

    dashboard = self.analytics_service.dashboard_report(
        self.demo_funnel
    )

    for key, value in dashboard.items():
        print(f"{key}: {value}")


####################################################################
# Executive Summary
####################################################################

def print_executive_summary(self) -> None:
    """
    Displays the executive summary.
    """

    print_section("Executive Summary")

    summary = self.analytics_service.executive_summary(
        self.demo_funnel
    )

    for key, value in summary.items():
        print(f"{key}: {value}")


####################################################################
# Platform Summary
####################################################################

def print_platform_summary(self) -> None:
    """
    Displays the platform summary.
    """

    print_section("Platform Summary")

    summary = self.analytics_service.platform_summary(
        self.demo_funnel
    )

    for key, value in summary.items():
        print(f"{key}: {value}")


####################################################################
# Health Check
####################################################################

def print_health_check(self) -> None:
    """
    Displays the service health.
    """

    print_section("Health Check")

    health = self.analytics_service.health_check()

    for key, value in health.items():
        print(f"{key}: {value}")



     ####################################################################
# Run Demo
####################################################################

def run(self) -> None:
    """
    Executes the Milestone 3 demo.
    """
    print_banner()
    self.load_customers()
    self.load_sessions()
    self.load_usage_events()
    self.build_customer_journeys()
    self.print_journey_analytics()
    self.print_navigation_analytics()
    self.print_funnel_analytics()
    self.print_dropoff_analytics()
    self.print_dashboard()
    self.print_executive_summary()
    self.print_platform_summary()
    self.print_health_check()
    print("\n" + LINE)
    print("IC-08 Milestone 3 completed successfully.")
    print(LINE)

     ####################################################################
# Main
####################################################################

def main() -> None:
    demo = CustomerJourneyAnalyticsDemo()
    demo.run()
if __name__ == "__main__":
    main()
