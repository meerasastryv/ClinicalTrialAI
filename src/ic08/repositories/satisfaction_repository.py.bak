"""
IC-08 - Customer Usage Intelligence
Milestone 14 - Satisfaction Prediction Repository
"""

from typing import Dict, List, Optional

from src.ic08.models.satisfaction_prediction import SatisfactionPrediction


class SatisfactionRepository:
    """
    Repository for storing and retrieving satisfaction predictions.
    """

    def __init__(self):
        self._predictions: Dict[str, SatisfactionPrediction] = {}

    def save(self, prediction: SatisfactionPrediction) -> None:
        """
        Save or update a customer's satisfaction prediction.
        """
        self._predictions[prediction.customer_id] = prediction

    def find_by_customer(
        self, customer_id: str
    ) -> Optional[SatisfactionPrediction]:
        """
        Retrieve prediction for a customer.
        """
        return self._predictions.get(customer_id)

    def find_all(self) -> List[SatisfactionPrediction]:
        """
        Return all satisfaction predictions.
        """
        return list(self._predictions.values())

    def average_score(self) -> float:
        """
        Calculate average satisfaction score.
        """
        if not self._predictions:
            return 0.0

        total = sum(
            prediction.score
            for prediction in self._predictions.values()
        )

        return total / len(self._predictions)

    def top_customers(
        self,
        limit: int = 5
    ) -> List[SatisfactionPrediction]:
        """
        Return customers with the highest satisfaction scores.
        """
        return sorted(
            self._predictions.values(),
            key=lambda prediction: prediction.score,
            reverse=True
        )[:limit]

    def count(self) -> int:
        """
        Return number of stored predictions.
        """
        return len(self._predictions)

    def clear(self) -> None:
        """
        Remove all stored predictions.
        """
        self._predictions.clear()

    def exists(self, customer_id: str) -> bool:
        """
        Check whether a prediction exists for a customer.
        """
        return customer_id in self._predictions

    def remove(self, customer_id: str) -> bool:
        """
        Remove a customer's prediction.

        Returns True if removed, otherwise False.
        """
        if customer_id in self._predictions:
            del self._predictions[customer_id]
            return True

        return False
