"""
IC-08 - Customer Usage Intelligence

Milestone 2 - Feature Usage Analytics

main_m02.py

Demonstrates:

- Feature usage analytics
- Feature statistics
- Feature adoption
- Customer distribution
- Workflow distribution
- Usage trends
- Dashboard summary
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta

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

from src.ic08.services.feature_tracking_service import (
    FeatureTrackingService,
)

from src.ic08.services.usage_event_service import (
    UsageEventService,
)

from src.ic08.services.workflow_tracking_service import (
    WorkflowTrackingService,
)

from src.ic08.services.feature_usage_analytics_service import (
    FeatureUsageAnalyticsService,
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
    print("Milestone 2 : Feature Usage Analytics")
    print(LINE)


def print_section(title: str) -> None:

    print(f"\n{SUB_LINE}")
    print(title)
    print(SUB_LINE)


class FeatureUsageAnalyticsDemo:
    """
    Demonstrates Feature Usage Analytics.
    """

    def __init__(self) -> None:

        logger.info(
            "Initializing Feature Usage Analytics Demo..."
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
        # Services
        #

        self.session_service = SessionTrackingService(
            self.session_repository
        )

        self.feature_service = FeatureTrackingService(
            self.feature_repository
        )

        self.workflow_service = WorkflowTrackingService(
            self.workflow_repository
        )

        self.usage_service = UsageEventService(
            self.usage_repository
        )

        self.analytics_service = (
            FeatureUsageAnalyticsService(
                usage_event_service=self.usage_service,
                feature_tracking_service=self.feature_service,
                workflow_tracking_service=self.workflow_service,
                session_tracking_service=self.session_service,
            )
        )

        logger.info(
            "Repositories initialized successfully."
        )

        logger.info(
            "Services initialized successfully."
        )


      ####################################################################
# Demo Data Builders
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
        Creates demo customer sessions.
        """

        from datetime import UTC
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
    # Demo Usage Events
    ####################################################################

    def build_usage_events(
        self,
    ) -> list[UsageEvent]:
        """
        Creates demo usage events for analytics.
        """

       # now = datetime.utcnow()

        from datetime import UTC
        now = datetime.now(UTC)
        return [

        UsageEvent(
            event_id="EVT-001",
            session_id="SES-001",
            customer_id="CUS-001",
            feature_name="Dashboard",
            event_type="OPEN",
            timestamp=now,
            duration_ms=250,
        ),

        UsageEvent(
            event_id="EVT-002",
            session_id="SES-001",
            customer_id="CUS-001",
            feature_name="Requirement Search",
            event_type="SEARCH",
            timestamp=now,
            duration_ms=430,
        ),

        UsageEvent(
            event_id="EVT-003",
            session_id="SES-001",
            customer_id="CUS-001",
            feature_name="Dashboard",
            event_type="REFRESH",
            timestamp=now,
            duration_ms=210,
        ),

        UsageEvent(
            event_id="EVT-004",
            session_id="SES-002",
            customer_id="CUS-002",
            feature_name="Test Design",
            event_type="CREATE",
            timestamp=now,
            duration_ms=760,
        ),

        UsageEvent(
            event_id="EVT-005",
            session_id="SES-002",
            customer_id="CUS-002",
            feature_name="Execution",
            event_type="RUN",
            timestamp=now,
            duration_ms=1820,
        ),

        UsageEvent(
            event_id="EVT-006",
            session_id="SES-002",
            customer_id="CUS-002",
            feature_name="Execution",
            event_type="RUN",
            timestamp=now,
            duration_ms=1740,
        ),

        UsageEvent(
            event_id="EVT-007",
            session_id="SES-003",
            customer_id="CUS-003",
            feature_name="Reports",
            event_type="VIEW",
            timestamp=now,
            duration_ms=390,
        ),

        UsageEvent(
            event_id="EVT-008",
            session_id="SES-003",
            customer_id="CUS-003",
            feature_name="Analytics",
            event_type="VIEW",
            timestamp=now,
            duration_ms=540,
        ),

        UsageEvent(
            event_id="EVT-009",
            session_id="SES-003",
            customer_id="CUS-003",
            feature_name="Traceability",
            event_type="SEARCH",
            timestamp=now,
            duration_ms=470,
        ),

        UsageEvent(
            event_id="EVT-010",
            session_id="SES-003",
            customer_id="CUS-003",
            feature_name="Reports",
            event_type="EXPORT",
            timestamp=now,
            duration_ms=620,
        ),
        ]

    ####################################################################
    # Load Customers
    ####################################################################

    def load_customers(
        self,
    ) -> None:
        """
        Load demo customers.
        """
        print_section("Loading Customers")
        customers = self.build_customers()
        for customer in customers:
            self.customer_repository.add_customer(customer)
            print(f"Customer Loaded : "
                  f"{customer.customer_id} - "
                  f"{customer.customer_name}"
                 )
            print(
                f"\nTotal Customers : "
                f"{len(customers)}"
                )
    ####################################################################
    # Load Sessions
    ####################################################################

    def load_sessions(
        self,
    ) -> None:
        """
        Load demo sessions.
        """
        print_section("Loading Sessions")
        sessions = self.build_sessions()
        for session in sessions:
            self.session_repository.add_session(session)
            print(f"Session Loaded : "
		  f"{session.session_id}"
		 )
            print(f"\nTotal Sessions : "
                f"{len(sessions)}"
		)
    ####################################################################
    # Load Usage Events
    ####################################################################

    def load_usage_events(
        self,
    ) -> None:
        """
        Record usage events.
        """
        print_section("Recording Usage Events")
        events = self.build_usage_events()
        for event in events:
            self.usage_service.record_event(event)
            print(
                f"Recorded : "
                f"{event.feature_name}")
            print(f"\nTotal Usage Events : "
                  f"{len(events)}")
    ####################################################################
    # Update Feature Repository
    ####################################################################
    def run_feature_tracking(
        self,
    ) -> None:
        """
        Populate feature statistics.
        """

        print_section(
        "Updating Feature Repository"
        )

        events = self.usage_service.get_all_events()

        for event in events:
            self.feature_service.record_feature_usage(
                feature_name=event.feature_name,
                duration_ms=event.duration_ms,
                success=event.success,
            )
            print(
                "Feature repository updated successfully."
            )


    ####################################################################
    # Analytics Summary
    ####################################################################

    def print_usage_summary(
        self,
    ) -> None:
        """
        Print overall summary.
        """

        print_section(
        "Usage Summary"
        )

        summary = (
        self.analytics_service
        .feature_usage_summary()
        )

        for key, value in summary.items():
            print(
                f"{key:25} : {value}"
            )


    ####################################################################
    # Top Features
    ####################################################################

    def print_top_features(
        self,
    ) -> None:
        """
        Display top features.
        """
        print_section(
        "Top Features"
        )
        features = (
        self.analytics_service
        .top_features()
        )
        for feature in features:
            print(
                f"{feature['feature']:25}"
                f"{feature['total_usage']:>8}"
            )


    ####################################################################
    # Power Users
    ####################################################################

    def print_power_users(
        self,
    ) -> None:
        """
        Display power users.
        """

        print_section(
        "Power Users"
        )

        users = (
        self.analytics_service
        .power_users()
        )

        for user in users:
            print(
                f"{user['customer_id']:15}"
                f"{user['usage_count']:>6}")
         ####################################################################
    # Dashboard
    ####################################################################
    def print_dashboard(
        self,
    ) -> None:
        """
        Display dashboard summary.
        """
        print_section(
        "Dashboard Summary"
        )
        dashboard = (
        self.analytics_service
        .analytics_dashboard_summary()
        )
        for key, value in dashboard.items():
           print(f"{key:25} : {value}")
    ####################################################################
    # Health Check
    ####################################################################

    def print_health_check(
        self,
    ) -> None:
        """
        Display analytics health.
        """
        print_section("Health Check")
        health = (self.analytics_service.health_check())
        for key, value in health.items():
            print(f"{key:25} : {value}")

    ####################################################################
    # Run Demo
    ####################################################################

    def run(
        self,
    ) -> None:
        """
        Execute Milestone 2 demonstration.
        """
        print_banner()
        self.load_customers()
        self.load_sessions()
        self.load_usage_events()
        self.run_feature_tracking()
        self.print_usage_summary()
        self.print_top_features()
        self.print_power_users()
        self.print_dashboard()
        self.print_health_check()
        print("\n" + "=" * 90)
        print("IC-08 Milestone 2 completed successfully.")
        print("=" * 90)


####################################################################
# Main
####################################################################

def main() -> None:

    demo = FeatureUsageAnalyticsDemo()

    demo.run()


if __name__ == "__main__":
    main()
