"""
customer_usage_service.py

Central orchestration service for customer usage collection.
"""

from __future__ import annotations

from typing import List

from src.ic08.models.customer import Customer
from src.ic08.models.customer_session import CustomerSession
from src.ic08.models.usage_event import UsageEvent
from src.ic08.repositories.customer_repository import CustomerRepository
from src.ic08.repositories.session_repository import SessionRepository
from src.ic08.repositories.usage_repository import UsageRepository


class CustomerUsageService:
    """
    Coordinates customer usage collection.
    """

    def __init__(
        self,
        customer_repository: CustomerRepository,
        session_repository: SessionRepository,
        usage_repository: UsageRepository,
    ) -> None:
        self._customer_repository = customer_repository
        self._session_repository = session_repository
        self._usage_repository = usage_repository

    def register_customer(
        self,
        customer: Customer,
    ) -> None:
        """
        Registers a customer.
        """
        self._customer_repository.add_customer(customer)

    def start_session(
        self,
        session: CustomerSession,
    ) -> None:
        """
        Starts a customer session.
        """
        self._session_repository.add_session(session)

    def end_session(
        self,
        session: CustomerSession,
    ) -> None:
        """
        Ends a customer session.
        """
        self._session_repository.update_session(session)

    def record_usage_event(
        self,
        event: UsageEvent,
    ) -> None:
        """
        Records a usage event.
        """
        self._usage_repository.add_event(event)

    def get_customer_sessions(
        self,
        customer_id: str,
    ) -> List[CustomerSession]:
        """
        Returns all sessions for a customer.
        """
        return self._session_repository.get_sessions_by_customer(
            customer_id
        )

    def get_customer_usage(
        self,
        customer_id: str,
    ) -> List[UsageEvent]:
        """
        Returns all usage events for a customer.
        """
        return self._usage_repository.get_events_by_customer(
            customer_id
        )

    def total_customers(self) -> int:
        """
        Returns the total number of customers.
        """
        return self._customer_repository.total_customers()

    def total_sessions(self) -> int:
        """
        Returns the total number of sessions.
        """
        return self._session_repository.total_sessions()

    def total_usage_events(self) -> int:
        """
        Returns the total number of usage events.
        """
        return self._usage_repository.total_events()
