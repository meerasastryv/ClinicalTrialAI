"""
session_repository.py

Repository for managing CustomerSession objects.
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from src.ic08.models.customer_session import CustomerSession


class SessionRepository:
    """
    Repository for storing and retrieving customer sessions.
    """

    def __init__(self) -> None:
        """
        Initialize the repository.
        """
        self._sessions: Dict[str, CustomerSession] = {}

    def add_session(
        self,
        session: CustomerSession,
    ) -> None:
        """
        Adds a customer session.
        """
        self._sessions[session.session_id] = session

    def get_session(
        self,
        session_id: str,
    ) -> Optional[CustomerSession]:
        """
        Returns a session by ID.
        """
        return self._sessions.get(session_id)

    def update_session(
        self,
        session: CustomerSession,
    ) -> None:
        """
        Updates an existing session.
        """
        self._sessions[session.session_id] = session

    def remove_session(
        self,
        session_id: str,
    ) -> bool:
        """
        Removes a session.

        Returns
        -------
        bool
            True if removed successfully.
        """
        return self._sessions.pop(session_id, None) is not None

    def get_all_sessions(self) -> List[CustomerSession]:
        """
        Returns all sessions.
        """
        return list(self._sessions.values())

    def get_sessions_by_customer(
        self,
        customer_id: str,
    ) -> List[CustomerSession]:
        """
        Returns all sessions for a customer.
        """
        return [
            session
            for session in self._sessions.values()
            if session.customer_id == customer_id
        ]

    def get_active_sessions(self) -> List[CustomerSession]:
        """
        Returns all active sessions.
        """
        return [
            session
            for session in self._sessions.values()
            if session.end_time is None
        ]

    def get_sessions_started_on(
        self,
        date: datetime,
    ) -> List[CustomerSession]:
        """
        Returns sessions started on the specified date.
        """
        return [
            session
            for session in self._sessions.values()
            if session.start_time.date() == date.date()
        ]

    def session_exists(
        self,
        session_id: str,
    ) -> bool:
        """
        Checks whether a session exists.
        """
        return session_id in self._sessions

    def total_sessions(self) -> int:
        """
        Returns the total number of sessions.
        """
        return len(self._sessions)

    def average_session_duration_seconds(self) -> float:
        """
        Returns the average duration of completed sessions.
        """
        completed_sessions = [
            session
            for session in self._sessions.values()
            if session.end_time is not None
        ]

        if not completed_sessions:
            return 0.0

        total_duration = sum(
            session.duration_seconds
            for session in completed_sessions
        )

        return total_duration / len(completed_sessions)

    def clear(self) -> None:
        """
        Removes all sessions.
        """
        self._sessions.clear()
