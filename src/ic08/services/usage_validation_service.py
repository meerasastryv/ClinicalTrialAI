"""
usage_validation_service.py

Service responsible for validating customer usage events.
"""

from __future__ import annotations

from typing import List

from src.ic08.models.usage_event import UsageEvent


class UsageValidationService:
    """
    Validates usage events before ingestion.
    """

    VALID_EVENT_TYPES = {
        "LOGIN",
        "LOGOUT",
        "VIEW",
        "CLICK",
        "SEARCH",
        "CREATE",
        "UPDATE",
        "DELETE",
        "EXPORT",
        "IMPORT",
        "UPLOAD",
        "DOWNLOAD",
        "ERROR",
    }

    def validate(
        self,
        event: UsageEvent,
    ) -> List[str]:
        """
        Validates a usage event.

        Returns
        -------
        List[str]
            Validation error messages.
            Empty list indicates a valid event.
        """
        errors: List[str] = []

        if not event.event_id.strip():
            errors.append("Event ID is required.")

        if not event.customer_id.strip():
            errors.append("Customer ID is required.")

        if not event.session_id.strip():
            errors.append("Session ID is required.")

        if not event.feature_name.strip():
            errors.append("Feature name is required.")

        if not event.event_type.strip():
            errors.append("Event type is required.")

        elif event.event_type.upper() not in self.VALID_EVENT_TYPES:
            errors.append(
                f"Unsupported event type: {event.event_type}"
            )

        if event.duration_ms < 0:
            errors.append(
                "Duration cannot be negative."
            )

        if event.timestamp is None:
            errors.append(
                "Timestamp is required."
            )

        return errors

    def is_valid(
        self,
        event: UsageEvent,
    ) -> bool:
        """
        Returns True if the event is valid.
        """
        return len(self.validate(event)) == 0
