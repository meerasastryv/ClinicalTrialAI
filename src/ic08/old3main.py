"""
main.py

IC-08 Customer Usage Intelligence Engine

Milestone 1-6 Demo
"""

from __future__ import annotations

import logging
from datetime import datetime, timedelta

from src.ic08.models.usage_event import UsageEvent
from src.ic08.repositories.session_repository import (
    SessionRepository,
)

from src.ic08.repositories.usage_repository import (
    UsageRepository,
)

from src.ic08.repositories.feature_repository import (
    FeatureRepository,
)

from src.ic08.repositories.workflow_repository import (
    WorkflowRepository,
)

from src.ic08.repositories.feature_adoption_repository import (
    FeatureAdoptionRepository,
)
from src.ic08.services.session_tracking_service import (
    SessionTrackingService,
)
from src.ic08.services.usage_event_service import (
    UsageEventService,
)
from src.ic08.services.feature_tracking_service import (
    FeatureTrackingService,
)
from src.ic08.services.workflow_tracking_service import (
    WorkflowTrackingService,
)
from src.ic08.services.usage_ingestion_service import (
    UsageIngestionService,
)
from src.ic08.services.usage_validation_service import (
    UsageValidationService,
)
from src.ic08.services.feature_adoption_service import (
    FeatureAdoptionService,
)

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s - %(message)s",
)

logger = logging.getLogger(__name__)


# ---------------------------------------------------------
# Demo Data
# ---------------------------------------------------------

def create_usage_events():
    """
    Creates sample usage events.
    """

    now = datetime.utcnow()

    events = [

        UsageEvent(
            event_id="EV001",
            session_id="S001",
            customer_id="C001",
            feature_name="Login",
            event_type="CLICK",
            page_name="Login",
            action_name="Submit",
            duration_ms=300,
            timestamp=now,
        ),

        UsageEvent(
            event_id="EV002",
            session_id="S001",
            customer_id="C001",
            feature_name="Dashboard",
            event_type="VIEW",
            page_name="Dashboard",
            action_name="Open",
            duration_ms=1200,
            timestamp=now + timedelta(seconds=5),
        ),

        UsageEvent(
            event_id="EV003",
            session_id="S001",
            customer_id="C001",
            feature_name="Reports",
            event_type="CLICK",
            page_name="Reports",
            action_name="Generate",
            duration_ms=2200,
            timestamp=now + timedelta(seconds=10),
        ),

        UsageEvent(
            event_id="EV004",
            session_id="S002",
            customer_id="C002",
            feature_name="Dashboard",
            event_type="VIEW",
            page_name="Dashboard",
            action_name="Open",
            duration_ms=1500,
            timestamp=now + timedelta(minutes=1),
        ),

        UsageEvent(
            event_id="EV005",
            session_id="S002",
            customer_id="C002",
            feature_name="Dashboard",
            event_type="CLICK",
            page_name="Dashboard",
            action_name="Refresh",
            duration_ms=500,
            timestamp=now + timedelta(minutes=1, seconds=10),
        ),

        UsageEvent(
            event_id="EV006",
            session_id="S002",
            customer_id="C002",
            feature_name="Reports",
            event_type="VIEW",
            page_name="Reports",
            action_name="Open",
            duration_ms=1800,
            timestamp=now + timedelta(minutes=1, seconds=20),
        ),

        UsageEvent(
            event_id="EV007",
            session_id="S003",
            customer_id="C003",
            feature_name="Dashboard",
            event_type="VIEW",
            page_name="Dashboard",
            action_name="Open",
            duration_ms=900,
            timestamp=now + timedelta(minutes=2),
        ),

        UsageEvent(
            event_id="EV008",
            session_id="S003",
            customer_id="C003",
            feature_name="Settings",
            event_type="CLICK",
            page_name="Settings",
            action_name="Save",
            duration_ms=700,
            timestamp=now + timedelta(minutes=2, seconds=20),
        ),

        UsageEvent(
            event_id="EV009",
            session_id="S004",
            customer_id="C004",
            feature_name="Dashboard",
            event_type="VIEW",
            page_name="Dashboard",
            action_name="Open",
            duration_ms=1000,
            timestamp=now + timedelta(minutes=3),
        ),

        UsageEvent(
            event_id="EV010",
            session_id="S004",
            customer_id="C004",
            feature_name="Reports",
            event_type="CLICK",
            page_name="Reports",
            action_name="Export",
            duration_ms=2600,
            timestamp=now + timedelta(minutes=3, seconds=15),
        ),

    ]

    return events


     # ---------------------------------------------------------
# Main Demo
# ---------------------------------------------------------

def main():

    logger.info("=" * 70)
    logger.info("IC-08 CUSTOMER USAGE INTELLIGENCE ENGINE")
    logger.info("=" * 70)

    # -----------------------------------------------------
    # Create Sample Events
    # -----------------------------------------------------

    usage_events = create_usage_events()

    logger.info(
        "Created %d sample usage events.",
        len(usage_events),
    )

    # -----------------------------------------------------
    # Initialize Services
    # -----------------------------------------------------

    session_tracking_service = SessionTrackingService()

    usage_event_service = UsageEventService()

    feature_tracking_service = (
        FeatureTrackingService()
    )

    workflow_tracking_service = (
        WorkflowTrackingService()
    )

    usage_ingestion_service = (
        UsageIngestionService()
    )

    usage_validation_service = (
        UsageValidationService()
    )


    feature_adoption_service = (
        FeatureAdoptionService()
    )

    logger.info("All services initialized.")

    # -----------------------------------------------------
    # Usage Validation
    # -----------------------------------------------------

    logger.info("")
    logger.info("Running Usage Validation...")

    valid_events = []

    for event in usage_events:

        try:

            if usage_validation_service.validate(event):
                valid_events.append(event)

        except Exception as ex:
            logger.warning(
                "Validation failed: %s",
                ex,
            )

    logger.info(
        "%d valid events found.",
        len(valid_events),
    )

    # -----------------------------------------------------
    # Usage Event Tracking
    # -----------------------------------------------------

    logger.info("")
    logger.info("Tracking Usage Events...")

    for event in valid_events:
        usage_event_service.track_event(event)

    logger.info("Usage events tracked.")

    # -----------------------------------------------------
    # Session Tracking
    # -----------------------------------------------------

    logger.info("")
    logger.info("Tracking Sessions...")

    for event in valid_events:
        session_tracking_service.track_event(event)

    logger.info("Session tracking completed.")

    # -----------------------------------------------------
    # Feature Tracking
    # -----------------------------------------------------

    logger.info("")
    logger.info("Tracking Features...")

    for event in valid_events:
        feature_tracking_service.track_feature(event)

    logger.info("Feature tracking completed.")

    # -----------------------------------------------------
    # Workflow Tracking
    # -----------------------------------------------------

    logger.info("")
    logger.info("Tracking Workflows...")

    for event in valid_events:
        workflow_tracking_service.track_event(event)

    logger.info("Workflow tracking completed.")

    # -----------------------------------------------------
    # Usage Ingestion
    # -----------------------------------------------------

    logger.info("")
    logger.info("Running Usage Ingestion...")

    try:

        usage_ingestion_service.ingest_events(
            valid_events
        )

    except Exception as ex:

        logger.warning(
            "Usage ingestion skipped: %s",
            ex,
        )

    logger.info("Usage ingestion completed.")

    # -----------------------------------------------------
    # Session Analytics
    # -----------------------------------------------------

    logger.info("")
    logger.info("=" * 70)
    logger.info("SESSION ANALYTICS")
    logger.info("=" * 70)

    try:

        sessions = (
            session_analytics_service.analyze_sessions(
                valid_events
            )
        )

        logger.info(
            "Sessions analyzed : %d",
            len(sessions),
        )

    except Exception as ex:

        logger.warning(
            "Session analytics unavailable: %s",
            ex,
        )

    # -----------------------------------------------------
    # Usage Analytics
    # -----------------------------------------------------

    logger.info("")
    logger.info("=" * 70)
    logger.info("USAGE ANALYTICS")
    logger.info("=" * 70)

    try:

        usage_summary = (
            usage_analytics_service.analyze_usage(
                valid_events
            )
        )

        logger.info(
            "Usage analytics completed."
        )

        logger.info("%s", usage_summary)

    except Exception as ex:

        logger.warning(
            "Usage analytics unavailable: %s",
            ex,
        )


         # -----------------------------------------------------
    # Feature Adoption Analytics
    # -----------------------------------------------------

    logger.info("")
    logger.info("=" * 70)
    logger.info("FEATURE ADOPTION ANALYTICS")
    logger.info("=" * 70)

    try:

        adoption_results = (
            feature_adoption_service.analyze_all_features(
                valid_events
            )
        )

        logger.info(
            "Features analyzed : %d",
            len(adoption_results),
        )

        for feature in adoption_results:

            logger.info("-----------------------------------")
            logger.info(
                "Feature            : %s",
                feature.feature_name,
            )
            logger.info(
                "Adoption Rate      : %.2f%%",
                feature.adoption_rate,
            )
            logger.info(
                "Repeat Usage Rate  : %.2f%%",
                feature.repeat_usage_rate,
            )
            logger.info(
                "Average Usage      : %.2f",
                feature.average_usage,
            )
            logger.info(
                "Power Users        : %d",
                feature.power_users,
            )
            logger.info(
                "Casual Users       : %d",
                feature.casual_users,
            )
            logger.info(
                "Inactive Users     : %d",
                feature.inactive_users,
            )
            logger.info(
                "Trend              : %s",
                feature.trend,
            )
            logger.info(
                "Score              : %.2f",
                feature.score,
            )

    except Exception as ex:

        logger.warning(
            "Feature adoption analytics unavailable: %s",
            ex,
        )

    # -----------------------------------------------------
    # Repository Summary
    # -----------------------------------------------------

    logger.info("")
    logger.info("=" * 70)
    logger.info("FEATURE SUMMARY")
    logger.info("=" * 70)

    try:

        summary = (
            feature_adoption_service.generate_summary()
        )

        for key, value in summary.items():

            logger.info(
                "%-25s : %s",
                key,
                value,
            )

    except Exception as ex:

        logger.warning(
            "Summary unavailable: %s",
            ex,
        )

    logger.info("")
    logger.info("=" * 70)
    logger.info("IC-08 MILESTONE 6 COMPLETED SUCCESSFULLY")
    logger.info("=" * 70)


# ---------------------------------------------------------
# Entry Point
# ---------------------------------------------------------

if __name__ == "__main__":
    main()
