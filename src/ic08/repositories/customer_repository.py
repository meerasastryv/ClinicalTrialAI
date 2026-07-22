"""
customer_repository.py

Repository for managing Customer objects.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from src.ic08.models.customer import Customer


class CustomerRepository:
    """
    Repository for storing and retrieving Customer objects.
    """

    def __init__(self) -> None:
        """
        Initialize the repository.
        """
        self._customers: Dict[str, Customer] = {}

    def add_customer(self, customer: Customer) -> None:
        """
        Adds a customer.
        """
        self._customers[customer.customer_id] = customer

    def get_customer(
        self,
        customer_id: str,
    ) -> Optional[Customer]:
        """
        Returns a customer by ID.
        """
        return self._customers.get(customer_id)

    def update_customer(
        self,
        customer: Customer,
    ) -> None:
        """
        Updates an existing customer.
        """
        self._customers[customer.customer_id] = customer

    def remove_customer(
        self,
        customer_id: str,
    ) -> bool:
        """
        Removes a customer.

        Returns
        -------
        bool
            True if removed successfully.
        """
        return self._customers.pop(customer_id, None) is not None

    def get_all_customers(self) -> List[Customer]:
        """
        Returns all customers.
        """
        return list(self._customers.values())

    def get_active_customers(self) -> List[Customer]:
        """
        Returns active customers.
        """
        return [
            customer
            for customer in self._customers.values()
            if customer.is_active
        ]

    def get_customers_by_region(
        self,
        region: str,
    ) -> List[Customer]:
        """
        Returns customers belonging to a region.
        """
        return [
            customer
            for customer in self._customers.values()
            if customer.region.lower() == region.lower()
        ]

    def get_customers_by_subscription(
        self,
        subscription_plan: str,
    ) -> List[Customer]:
        """
        Returns customers for a subscription plan.
        """
        return [
            customer
            for customer in self._customers.values()
            if customer.subscription_plan.lower()
            == subscription_plan.lower()
        ]

    def customer_exists(
        self,
        customer_id: str,
    ) -> bool:
        """
        Checks whether a customer exists.
        """
        return customer_id in self._customers

    def total_customers(self) -> int:
        """
        Returns total number of customers.
        """
        return len(self._customers)

    def clear(self) -> None:
        """
        Removes all customers.
        """
        self._customers.clear()
