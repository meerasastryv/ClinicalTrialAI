"""
session_tracking_service.py

Service responsible for tracking customer sessions.
"""

from __future__ import annotations

from datetime import datetime
from typing import List, Optional

from src.ic08.models.customer_session import CustomerSession
from src.ic08.repositories.session_repository import SessionRepository


class SessionTrackingService:
    """
    Manages customer session lifecycle.
    """

    def __init__(
        self,
        session_repository: SessionRepository,
    ) -> None:
        self._repository = session_repository

    def start_session(
        self,
        session: CustomerSession,
    ) -> None:
        """
        Starts a customer session.
        """
        self._repository.add_session(session)

    def end_session(
        self,
        session_id: str,
    ) -> bool:
        """
        Ends a customer session.

        Returns
        -------
        bool
            True if the session was found and closed.
        """
        session = self._repository.get_session(session_id)

        if session is None:
            return False

        session.close_session()
        self._repository.update_session(session)

        return True

    def get_session(
        self,
        session_id: str,
    ) -> Optional[CustomerSession]:
        """
        Returns a session by ID.
        """
        return self._repository.get_session(session_id)

    def get_active_sessions(self) -> List[CustomerSession]:
        """
        Returns all active sessions.
        """
        return self._repository.get_active_sessions()

    def get_customer_sessions(
        self,
        customer_id: str,
    ) -> List[CustomerSession]:
        """
        Returns all sessions for a customer.
        """
        return self._repository.get_sessions_by_customer(customer_id)

    def update_activity(
        self,
        session_id: str,
    ) -> bool:
        """
        Updates session activity timestamp.
        """
        session = self._repository.get_session(session_id)

        if session is None:
            return False

        session.updated_at = datetime.utcnow()
        self._repository.update_session(session)

        return True

    def total_active_sessions(self) -> int:
        """
        Returns the number of active sessions.
        """
        return len(self._repository.get_active_sessions())

    def average_session_duration(self) -> float:
        """
        Returns the average session duration.
        """
        return self._repository.average_session_duration_seconds()
