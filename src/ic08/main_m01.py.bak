"""
IC-08 - Customer Usage Intelligence
Milestone 1 - Customer Usage Tracking

main_m01.py

This module demonstrates the end-to-end execution of the Customer Usage
Tracking milestone. It initializes repositories and services, creates
sample customers, sessions, and usage events, validates and ingests
usage data, and displays summary statistics.

Project : ClinicalTrialAI
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta ,UTC 
from typing import List
# ---------------------------------------------------------------------
# Models
# ---------------------------------------------------------------------

from src.ic08.models.customer import Customer
from src.ic08.models.customer_session import CustomerSession
from src.ic08.models.usage_event import UsageEvent
from src.ic08.models.workflow import Workflow

# ---------------------------------------------------------------------
# Repositories
# ---------------------------------------------------------------------

from src.ic08.repositories.customer_repository import CustomerRepository
from src.ic08.repositories.session_repository import SessionRepository
from src.ic08.repositories.usage_repository import UsageRepository
from src.ic08.repositories.feature_repository import FeatureRepository
from src.ic08.repositories.workflow_repository import WorkflowRepository

# ---------------------------------------------------------------------
# Services
# ---------------------------------------------------------------------

from src.ic08.services.session_tracking_service import (
    SessionTrackingService,
)
from src.ic08.services.feature_tracking_service import (
    FeatureTrackingService,
)
from src.ic08.services.workflow_tracking_service import (
    WorkflowTrackingService,
)
from src.ic08.services.usage_event_service import (
    UsageEventService,
)
from src.ic08.services.usage_validation_service import (
    UsageValidationService,
)
from src.ic08.services.usage_ingestion_service import (
    UsageIngestionService,
)

# ---------------------------------------------------------------------
# Logging Configuration
# ---------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(message)s",
)

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------
# Console Helpers
# ---------------------------------------------------------------------

LINE = "=" * 90
SUB_LINE = "-" * 90


def print_banner() -> None:
    """
    Displays the application banner.
    """

    print("\n" + LINE)
    print("ClinicalTrialAI")
    print("IC-08 : Customer Usage Intelligence")
    print("Milestone 1 : Customer Usage Tracking")
    print(LINE)


def print_section(title: str) -> None:
    """
    Displays a section heading.
    """

    print(f"\n{SUB_LINE}")
    print(title)
    print(SUB_LINE)


# ---------------------------------------------------------------------
# Customer Usage Tracking Demo
# ---------------------------------------------------------------------


class CustomerUsageTrackingDemo:
    """
    Demonstrates the Customer Usage Tracking milestone.
    """

    ####################################################################
    # Constructor
    ####################################################################

    def __init__(self) -> None:

        logger.info(
            "Initializing Customer Usage Tracking Demo..."
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

        self.validation_service = UsageValidationService()

        self.usage_service = UsageEventService(
            self.usage_repository
        )

        self.ingestion_service = UsageIngestionService(
            self.usage_repository,
        )
        logger.info(
            "Repositories initialized successfully."
        )

        logger.info(
            "Services initialized successfully."
        )

    ####################################################################
    # Demo Customer Builder
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
                subscription_plan="Professional",
                region="India",
            ),

            Customer(
                customer_id="CUS-003",
                customer_name="David Miller",
                organization="Roche",
                industry="Healthcare",
                subscription_plan="Enterprise",
                region="Switzerland",
            ),

            Customer(
                customer_id="CUS-004",
                customer_name="Maria Garcia",
                organization="IQVIA",
                industry="Clinical Research",
                subscription_plan="Standard",
                region="Spain",
            ),

            Customer(
                customer_id="CUS-005",
                customer_name="Keiko Tanaka",
                organization="Takeda",
                industry="Pharmaceutical",
                subscription_plan="Enterprise",
                region="Japan",
            ),
        ]

    ####################################################################
    # Demo Session Builder
    ####################################################################

    def build_sessions(
        self,
    ) -> list[CustomerSession]:
        """
        Creates sample customer sessions.
        """
        now = datetime.now(UTC)

        return [

            CustomerSession(
                session_id="SES-001",
                customer_id="CUS-001",
                user_id="USR-001",
                user_name="John Smith",
                start_time=now - timedelta(minutes=60),
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
                start_time=now - timedelta(minutes=45),
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
                start_time=now - timedelta(minutes=30),
                device="MacBook Air",
                browser="Safari",
                operating_system="macOS",
                location="Basel",
            ),
        ]


    ####################################################################
    # Demo Usage Event Builder
    ####################################################################

    def build_usage_events(
        self,
    ) -> list[UsageEvent]:
        """
        Creates sample usage events.
        """
        now = datetime.now(UTC)

        return [

            UsageEvent(
                event_id="EVT-001",
                session_id="SES-001",
                customer_id="CUS-001",
                feature_name="Dashboard",
                event_type="OPEN",
                timestamp=now,
                page_name="Dashboard",
                action_name="Open Dashboard",
                duration_ms=250,
            ),

            UsageEvent(
                event_id="EVT-002",
                session_id="SES-001",
                customer_id="CUS-001",
                feature_name="Requirement Search",
                event_type="SEARCH",
                timestamp=now,
                page_name="Requirements",
                action_name="Search Requirement",
                duration_ms=480,
            ),

            UsageEvent(
                event_id="EVT-003",
                session_id="SES-002",
                customer_id="CUS-002",
                feature_name="Test Design",
                event_type="CREATE",
                timestamp=now,
                page_name="Test Cases",
                action_name="Create Test Case",
                duration_ms=620,
            ),

            UsageEvent(
                event_id="EVT-004",
                session_id="SES-002",
                customer_id="CUS-002",
                feature_name="Execution",
                event_type="RUN",
                timestamp=now,
                page_name="Execution",
                action_name="Execute Test Suite",
                duration_ms=1800,
            ),

            UsageEvent(
                event_id="EVT-005",
                session_id="SES-003",
                customer_id="CUS-003",
                feature_name="Reports",
                event_type="VIEW",
                timestamp=now,
                page_name="Reports",
                action_name="View Dashboard",
                duration_ms=340,
            ),
        ]

    ####################################################################
    # Repository Population
    ####################################################################

    def register_customers(
        self,
        customers: list[Customer],
    ) -> None:
        """
        Registers demo customers.
        """

        print_section("Registering Customers")

        for customer in customers:
            self.customer_repository.add_customer(customer)

            logger.info(
                "Registered customer %s (%s)",
                customer.customer_id,
                customer.organization,
            )

        print(
            f"Customers Registered : {len(customers)}"
        )

    def register_sessions(
        self,
        sessions: list[CustomerSession],
    ) -> None:
        """
        Registers demo sessions.
        """

        print_section("Registering Customer Sessions")

        for session in sessions:
            self.session_repository.add_session(session)

            logger.info(
                "Registered session %s",
                session.session_id,
            )

        print(
            f"Sessions Registered : {len(sessions)}"
        )

    def record_usage_events(
        self,
        events: list[UsageEvent],
    ) -> None:
        """
        Records demo usage events.
        """

        print_section("Recording Usage Events")

        ingested = self.ingestion_service.ingest_events(
            events
        )

        logger.info(
            "Successfully ingested %d usage events.",
            ingested,
        )

        print(
            f"Usage Events Recorded : {ingested}"
        )


         ####################################################################
    # Summary
    ####################################################################

    def display_summary(self) -> None:
        """
        Displays milestone execution summary.
        """

        print_section("Customer Usage Tracking Summary")

        print(
            f"Total Customers      : "
            f"{self.customer_repository.total_customers()}"
        )

        print(
            f"Total Sessions       : "
            f"{self.session_repository.total_sessions()}"
        )

        print(
            f"Total Usage Events   : "
            f"{self.usage_service.total_events()}"
        )

        print()

        print("Milestone Status")

        print("------------------------------")

        print("✓ Customer registration completed")

        print("✓ Session tracking completed")

        print("✓ Usage event ingestion completed")

        print("✓ Repository population completed")

        print("✓ Customer Usage Tracking successful")

    ####################################################################
    # Execute Demo
    ####################################################################

    def run(self) -> None:
        """
        Executes the complete Customer Usage Tracking demo.
        """

        print_banner()

        logger.info("Building demo data...")

        customers = self.build_customers()

        sessions = self.build_sessions()

        events = self.build_usage_events()

        self.register_customers(customers)

        self.register_sessions(sessions)

        self.record_usage_events(events)

        self.display_summary()

        logger.info(
            "Milestone 1 completed successfully."
        )


########################################################################
# Main Entry Point
########################################################################

def main() -> None:
    """
    Application entry point.
    """

    try:

        demo = CustomerUsageTrackingDemo()

        demo.run()

    except KeyboardInterrupt:

        logger.warning(
            "Execution interrupted by user."
        )

    except Exception as ex:

        logger.exception(
            "Unexpected error: %s",
            ex,
        )


if __name__ == "__main__":
    main()

