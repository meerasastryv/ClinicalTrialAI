"""
feedback_repository.py

Repository for managing Feedback objects.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from src.ic08.models.feedback import Feedback


class FeedbackRepository:
    """
    Repository for storing and analyzing customer feedback.
    """

    def __init__(self) -> None:
        """
        Initialize the repository.
        """
        self._feedback: Dict[str, Feedback] = {}

    def add_feedback(
        self,
        feedback: Feedback,
    ) -> None:
        """
        Adds or replaces a feedback record.
        """
        self._feedback[feedback.feedback_id] = feedback

    def get_feedback(
        self,
        feedback_id: str,
    ) -> Optional[Feedback]:
        """
        Returns feedback by ID.
        """
        return self._feedback.get(feedback_id)

    def update_feedback(
        self,
        feedback: Feedback,
    ) -> None:
        """
        Updates an existing feedback record.
        """
        self._feedback[feedback.feedback_id] = feedback

    def remove_feedback(
        self,
        feedback_id: str,
    ) -> bool:
        """
        Removes a feedback record.
        """
        return self._feedback.pop(feedback_id, None) is not None

    def get_all_feedback(self) -> List[Feedback]:
        """
        Returns all feedback.
        """
        return list(self._feedback.values())

    def get_feedback_by_customer(
        self,
        customer_id: str,
    ) -> List[Feedback]:
        """
        Returns all feedback for a customer.
        """
        return [
            feedback
            for feedback in self._feedback.values()
            if feedback.customer_id == customer_id
        ]

    def get_feedback_by_feature(
        self,
        feature_name: str,
    ) -> List[Feedback]:
        """
        Returns all feedback for a feature.
        """
        return [
            feedback
            for feedback in self._feedback.values()
            if feedback.feature_name.lower() == feature_name.lower()
        ]

    def get_feedback_by_category(
        self,
        category: str,
    ) -> List[Feedback]:
        """
        Returns feedback belonging to a category.
        """
        return [
            feedback
            for feedback in self._feedback.values()
            if feedback.category.lower() == category.lower()
        ]

    def get_unresolved_feedback(self) -> List[Feedback]:
        """
        Returns unresolved feedback.
        """
        return [
            feedback
            for feedback in self._feedback.values()
            if not feedback.resolved
        ]

    def get_positive_feedback(self) -> List[Feedback]:
        """
        Returns positive feedback.
        """
        return [
            feedback
            for feedback in self._feedback.values()
            if feedback.is_positive
        ]

    def get_negative_feedback(self) -> List[Feedback]:
        """
        Returns negative feedback.
        """
        return [
            feedback
            for feedback in self._feedback.values()
            if feedback.is_negative
        ]

    def average_rating(self) -> float:
        """
        Returns the average customer rating.
        """
        if not self._feedback:
            return 0.0

        return (
            sum(feedback.rating for feedback in self._feedback.values())
            / len(self._feedback)
        )

    def feedback_exists(
        self,
        feedback_id: str,
    ) -> bool:
        """
        Checks whether a feedback record exists.
        """
        return feedback_id in self._feedback

    def total_feedback(self) -> int:
        """
        Returns the total number of feedback records.
        """
        return len(self._feedback)

    def clear(self) -> None:
        """
        Removes all feedback records.
        """
        self._feedback.clear()
