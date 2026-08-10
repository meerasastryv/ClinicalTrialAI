"""
customer_journey_builder.py

Builds customer journeys from usage events.

This service is responsible only for constructing journey objects.
Analytics such as navigation trends, funnels, and drop-off analysis
are implemented in dedicated services.
"""

from __future__ import annotations

import logging
from collections import defaultdict
from typing import Any

from src.ic08.models.usage_event import UsageEvent
from src.ic08.services.usage_event_service import UsageEventService
from src.ic08.services.session_tracking_service import (
    SessionTrackingService,
)
from src.ic08.services.workflow_tracking_service import (
    WorkflowTrackingService,
)

logger = logging.getLogger(__name__)


class CustomerJourneyBuilder:
    """
    Builds customer journeys from recorded usage events.
    """

    def __init__(
        self,
        usage_event_service: UsageEventService,
        session_tracking_service: SessionTrackingService | None = None,
        workflow_tracking_service: WorkflowTrackingService | None = None,
    ) -> None:
        """
        Initialize the journey builder.
        """

        self._usage_service = usage_event_service
        self._session_service = session_tracking_service
        self._workflow_service = workflow_tracking_service

        #logger.info(
        #    "CustomerJourneyBuilder initialized."
        #)

    ####################################################################
    # Event Collection
    ####################################################################

    def _collect_events(
        self,
    ) -> list[UsageEvent]:
        """
        Returns all recorded usage events.
        """

        events = self._usage_service.get_all_events()

        logger.debug(
            "Collected %d usage events.",
            len(events),
        )

        return events

    ####################################################################
    # Validation Helpers
    ####################################################################

    def _validate_events(
        self,
        events: list[UsageEvent],
    ) -> bool:
        """
        Validates that the supplied event collection
        is suitable for journey construction.
        """

        return len(events) > 0

    ####################################################################
    # Grouping Helpers
    ####################################################################

    def _group_by_session(
        self,
        events: list[UsageEvent],
    ) -> dict[str, list[UsageEvent]]:
        """
        Groups events by session.
        """

        grouped = defaultdict(list)

        for event in events:
            grouped[event.session_id].append(event)

        return dict(grouped)

    def _group_by_customer(
        self,
        events: list[UsageEvent],
    ) -> dict[str, list[UsageEvent]]:
        """
        Groups events by customer.
        """

        grouped = defaultdict(list)

        for event in events:
            grouped[event.customer_id].append(event)

        return dict(grouped)

    def _group_by_workflow(
        self,
        events: list[UsageEvent],
    ) -> dict[str, list[UsageEvent]]:
        """
        Groups events by workflow.

        Workflow name is expected in event metadata.
        """

        grouped = defaultdict(list)

        for event in events:
            workflow = event.metadata.get(
                "workflow_name",
                "Unknown",
            )

            grouped[workflow].append(event)

        return dict(grouped)
         ####################################################################
    # Journey Processing Helpers
    ####################################################################

    def _order_events(
        self,
        events: list[UsageEvent],
    ) -> list[UsageEvent]:
        """
        Orders events chronologically.
        """

        return sorted(
            events,
            key=lambda event: event.timestamp,
        )

    def _navigation_path(
        self,
        events: list[UsageEvent],
    ) -> list[str]:
        """
        Returns the ordered navigation path.
        """

        return [
            event.page_name
            for event in self._order_events(events)
            if event.page_name
        ]

    def _feature_sequence(
        self,
        events: list[UsageEvent],
    ) -> list[str]:
        """
        Returns the ordered feature sequence.
        """

        return [
            event.feature_name
            for event in self._order_events(events)
        ]

    def _entry_page(
        self,
        events: list[UsageEvent],
    ) -> str | None:
        """
        Returns the first page visited.
        """

        ordered = self._order_events(events)

        for event in ordered:
            if event.page_name:
                return event.page_name

        return None

    def _exit_page(
        self,
        events: list[UsageEvent],
    ) -> str | None:
        """
        Returns the last page visited.
        """

        ordered = reversed(
            self._order_events(events)
        )

        for event in ordered:
            if event.page_name:
                return event.page_name

        return None

    def _journey_duration(
        self,
        events: list[UsageEvent],
    ) -> float:
        """
        Calculates journey duration in seconds.
        """

        ordered = self._order_events(events)

        if len(ordered) < 2:
            return 0.0

        return round(
            (
                ordered[-1].timestamp
                - ordered[0].timestamp
            ).total_seconds(),
            2,
        )

    def _event_count(
        self,
        events: list[UsageEvent],
    ) -> int:
        """
        Returns number of events.
        """

        return len(events)

    def _completed(
        self,
        events: list[UsageEvent],
    ) -> bool:
        """
        Returns True if every event completed successfully.
        """

        return all(
            event.success
            for event in events
        )

    def _workflow_name(
        self,
        events: list[UsageEvent],
    ) -> str:
        """
        Returns workflow name.
        """

        if not events:
            return "Unknown"

        return events[0].metadata.get(
            "workflow_name",
            "Unknown",
        )

         ####################################################################
    # Journey Builders
    ####################################################################

    def _build_session_journey(
        self,
        session_id: str,
        events: list[UsageEvent],
    ) -> dict[str, Any]:
        """
        Builds a journey for a single session.
        """

        ordered = self._order_events(events)

        if not ordered:
            return {}

        return {
            "session_id": session_id,
            "customer_id": ordered[0].customer_id,
            "workflow": self._workflow_name(ordered),
            "entry_page": self._entry_page(ordered),
            "exit_page": self._exit_page(ordered),
            "navigation_path": self._navigation_path(ordered),
            "feature_sequence": self._feature_sequence(ordered),
            "event_count": self._event_count(ordered),
            "duration_seconds": self._journey_duration(ordered),
            "completed": self._completed(ordered),
            "events": ordered,
        }

    ####################################################################
    # Public Journey APIs
    ####################################################################

    def build_all_journeys(
        self,
    ) -> list[dict[str, Any]]:
        """
        Builds journeys for every recorded session.
        """

        events = self._collect_events()

        if not self._validate_events(events):
            return []

        grouped = self._group_by_session(events)

        journeys = []

        for session_id, session_events in grouped.items():
            journeys.append(
                self._build_session_journey(
                    session_id,
                    session_events,
                )
            )

        #logger.info(
        #    "Built %d customer journeys.",
        #    len(journeys),
        #)

        return journeys

    def build_session_journey(
        self,
        session_id: str,
    ) -> dict[str, Any]:
        """
        Builds the journey for one session.
        """

        events = [
            event
            for event in self._collect_events()
            if event.session_id == session_id
        ]

        if not events:
            return {}

        return self._build_session_journey(
            session_id,
            events,
        )

    def build_customer_journeys(
        self,
        customer_id: str,
    ) -> list[dict[str, Any]]:
        """
        Builds all journeys for a customer.
        """

        customer_events = [
            event
            for event in self._collect_events()
            if event.customer_id == customer_id
        ]

        grouped = self._group_by_session(
            customer_events,
        )

        return [
            self._build_session_journey(
                session_id,
                events,
            )
            for session_id, events in grouped.items()
        ]

    def build_workflow_journeys(
        self,
        workflow_name: str,
    ) -> list[dict[str, Any]]:
        """
        Builds journeys belonging to a workflow.
        """

        workflow_events = [
            event
            for event in self._collect_events()
            if event.metadata.get(
                "workflow_name",
                "Unknown",
            ) == workflow_name
        ]

        grouped = self._group_by_session(
            workflow_events,
        )

        return [
            self._build_session_journey(
                session_id,
                events,
            )
            for session_id, events in grouped.items()
        ]

         ####################################################################
    # Journey Lookup APIs
    ####################################################################

    def session_events(
        self,
        session_id: str,
    ) -> list[UsageEvent]:
        """
        Returns all events for a session.
        """

        return [
            event
            for event in self._collect_events()
            if event.session_id == session_id
        ]

    def customer_events(
        self,
        customer_id: str,
    ) -> list[UsageEvent]:
        """
        Returns all events for a customer.
        """

        return [
            event
            for event in self._collect_events()
            if event.customer_id == customer_id
        ]

    def workflow_events(
        self,
        workflow_name: str,
    ) -> list[UsageEvent]:
        """
        Returns all events belonging to a workflow.
        """

        return [
            event
            for event in self._collect_events()
            if event.metadata.get(
                "workflow_name",
                "Unknown",
            ) == workflow_name
        ]

    ####################################################################
    # Journey Summary APIs
    ####################################################################

    def session_summary(
        self,
        session_id: str,
    ) -> dict[str, Any]:
        """
        Returns a summary for one session.
        """

        return self.build_session_journey(
            session_id,
        )

    def customer_summary(
        self,
        customer_id: str,
    ) -> dict[str, Any]:
        """
        Returns summary information for a customer.
        """

        journeys = self.build_customer_journeys(
            customer_id,
        )

        if not journeys:
            return {}

        return {
            "customer_id": customer_id,
            "total_sessions": len(journeys),
            "completed_sessions": sum(
                1
                for journey in journeys
                if journey["completed"]
            ),
            "failed_sessions": sum(
                1
                for journey in journeys
                if not journey["completed"]
            ),
            "total_events": sum(
                journey["event_count"]
                for journey in journeys
            ),
            "average_duration": round(
                sum(
                    journey["duration_seconds"]
                    for journey in journeys
                )
                / len(journeys),
                2,
            ),
            "journeys": journeys,
        }

    def workflow_summary(
        self,
        workflow_name: str,
    ) -> dict[str, Any]:
        """
        Returns summary information for a workflow.
        """

        journeys = self.build_workflow_journeys(
            workflow_name,
        )

        if not journeys:
            return {}

        return {
            "workflow": workflow_name,
            "total_sessions": len(journeys),
            "completed_sessions": sum(
                1
                for journey in journeys
                if journey["completed"]
            ),
            "failed_sessions": sum(
                1
                for journey in journeys
                if not journey["completed"]
            ),
            "total_events": sum(
                journey["event_count"]
                for journey in journeys
            ),
            "average_duration": round(
                sum(
                    journey["duration_seconds"]
                    for journey in journeys
                )
                / len(journeys),
                2,
            ),
            "journeys": journeys,
        }

    ####################################################################
    # Statistics
    ####################################################################

    def total_journeys(
        self,
    ) -> int:
        """
        Returns the total number of journeys.
        """

        return len(
            self.build_all_journeys()
        )

    def total_customers(
        self,
    ) -> int:
        """
        Returns the number of customers.
        """

        return len(
            {
                journey["customer_id"]
                for journey in self.build_all_journeys()
            }
        )

    def total_workflows(
        self,
    ) -> int:
        """
        Returns the number of workflows.
        """

        return len(
            {
                journey["workflow"]
                for journey in self.build_all_journeys()
            }
        )

         ####################################################################
    # Export APIs
    ####################################################################

    def export_all_journeys(
        self,
    ) -> dict[str, Any]:
        """
        Exports all customer journeys.
        """

        journeys = self.build_all_journeys()

        return {
            "total_journeys": len(journeys),
            "journeys": journeys,
        }

    def export_customer_journeys(
        self,
        customer_id: str,
    ) -> dict[str, Any]:
        """
        Exports journeys for a customer.
        """

        return self.customer_summary(
            customer_id,
        )

    def export_workflow_journeys(
        self,
        workflow_name: str,
    ) -> dict[str, Any]:
        """
        Exports journeys for a workflow.
        """

        return self.workflow_summary(
            workflow_name,
        )

    ####################################################################
    # Journey Statistics
    ####################################################################

    def average_journey_duration(
        self,
    ) -> float:
        """
        Returns average journey duration.
        """

        journeys = self.build_all_journeys()

        if not journeys:
            return 0.0

        return round(
            sum(
                journey["duration_seconds"]
                for journey in journeys
            )
            / len(journeys),
            2,
        )

    def completion_rate(
        self,
    ) -> float:
        """
        Returns overall completion percentage.
        """

        journeys = self.build_all_journeys()

        if not journeys:
            return 0.0

        completed = sum(
            1
            for journey in journeys
            if journey["completed"]
        )

        return round(
            completed * 100 / len(journeys),
            2,
        )

    def failed_journeys(
        self,
    ) -> list[dict[str, Any]]:
        """
        Returns all failed journeys.
        """

        return [
            journey
            for journey in self.build_all_journeys()
            if not journey["completed"]
        ]

    def completed_journeys(
        self,
    ) -> list[dict[str, Any]]:
        """
        Returns all completed journeys.
        """

        return [
            journey
            for journey in self.build_all_journeys()
            if journey["completed"]
        ]

    ####################################################################
    # Dashboard Summary
    ####################################################################

    def dashboard_summary(
        self,
    ) -> dict[str, Any]:
        """
        Returns dashboard information for Journey Analytics.
        """

        return {
            "total_journeys": self.total_journeys(),
            "total_customers": self.total_customers(),
            "total_workflows": self.total_workflows(),
            "completion_rate": self.completion_rate(),
            "average_duration": self.average_journey_duration(),
        }

         ####################################################################
    # Search APIs
    ####################################################################

    def journey_exists(
        self,
        session_id: str,
    ) -> bool:
        """
        Returns True if a journey exists for the session.
        """

        return bool(
            self.build_session_journey(
                session_id,
            )
        )

    def customer_exists(
        self,
        customer_id: str,
    ) -> bool:
        """
        Returns True if customer has journeys.
        """

        return len(
            self.build_customer_journeys(
                customer_id,
            )
        ) > 0

    def workflow_exists(
        self,
        workflow_name: str,
    ) -> bool:
        """
        Returns True if workflow journeys exist.
        """

        return len(
            self.build_workflow_journeys(
                workflow_name,
            )
        ) > 0

    ####################################################################
    # Convenience APIs
    ####################################################################

    def first_journey(
        self,
    ) -> dict[str, Any]:
        """
        Returns the first available journey.
        """

        journeys = self.build_all_journeys()

        if journeys:
            return journeys[0]

        return {}

    def last_journey(
        self,
    ) -> dict[str, Any]:
        """
        Returns the last available journey.
        """

        journeys = self.build_all_journeys()

        if journeys:
            return journeys[-1]

        return {}

    ####################################################################
    # Health Check
    ####################################################################

    def health_check(
        self,
    ) -> dict[str, Any]:
        """
        Returns builder health information.
        """

        return {
            "status": "healthy",
            "total_events": len(
                self._collect_events()
            ),
            "total_journeys": self.total_journeys(),
            "total_customers": self.total_customers(),
            "total_workflows": self.total_workflows(),
            "completion_rate": self.completion_rate(),
        }

    ####################################################################
    # Builder Information
    ####################################################################

    def builder_information(
        self,
    ) -> dict[str, Any]:
        """
        Returns metadata about the builder.
        """

        return {
            "service": "CustomerJourneyBuilder",
            "module": "IC-08 Customer Usage Intelligence",
            "version": "1.0",
            "status": "Ready",
            "supported_operations": [
                "Journey Construction",
                "Session Journey",
                "Customer Journey",
                "Workflow Journey",
                "Journey Export",
                "Dashboard Summary",
                "Health Check",
            ],
        }
