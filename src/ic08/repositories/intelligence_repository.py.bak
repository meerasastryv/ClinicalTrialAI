from typing import Dict, List, Optional

from src.ic08.models.customer_intelligence import CustomerIntelligence


class IntelligenceRepository:
    """
    Repository for storing consolidated customer/study intelligence.
    """

    def __init__(self):
        self._dashboards: Dict[str, CustomerIntelligence] = {}

    def save(self, dashboard: CustomerIntelligence) -> None:
        """
        Save or update a dashboard.
        """
        self._dashboards[dashboard.customer_id] = dashboard

    def get_by_customer_id(
        self,
        customer_id: str
    ) -> Optional[CustomerIntelligence]:
        """
        Retrieve dashboard by customer ID.
        """
        return self._dashboards.get(customer_id)

    def get_all(self) -> List[CustomerIntelligence]:
        """
        Return all dashboards.
        """
        return list(self._dashboards.values())

    def delete(self, customer_id: str) -> bool:
        """
        Delete dashboard for a customer.
        """
        if customer_id in self._dashboards:
            del self._dashboards[customer_id]
            return True
        return False

    def exists(self, customer_id: str) -> bool:
        """
        Check whether a dashboard exists.
        """
        return customer_id in self._dashboards

    def count(self) -> int:
        """
        Return total number of dashboards.
        """
        return len(self._dashboards)

    def clear(self) -> None:
        """
        Remove all dashboards.
        """
        self._dashboards.clear()
