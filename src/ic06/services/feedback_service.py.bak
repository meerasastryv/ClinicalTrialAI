"""
feedback_service.py

Business service responsible for processing feedback records
and reinforcement signals.
"""

from __future__ import annotations

from datetime import datetime
from typing import Dict, List, Optional

from src.ic06.models.feedback_record import FeedbackRecord
from src.ic06.repositories.learning_repository import LearningRepository


class FeedbackService:
    """
    Service responsible for processing learning feedback.
    """

    def __init__(
        self,
        repository: Optional[LearningRepository] = None,
    ):
        self._repository = repository or LearningRepository()

    # ------------------------------------------------------------------
    # CRUD Operations
    # ------------------------------------------------------------------

    def record_feedback(
        self,
        feedback: FeedbackRecord,
    ) -> FeedbackRecord:
        """
        Store a feedback record.
        """
        self._repository.add(feedback)
        return feedback

    def get_feedback(
        self,
        feedback_id: str,
    ) -> Optional[FeedbackRecord]:
        """
        Retrieve feedback by ID.
        """
        return self._repository.get(feedback_id)

    def get_all_feedback(self) -> List[FeedbackRecord]:
        """
        Return all feedback records.
        """
        return self._repository.get_all()

    def delete_feedback(
        self,
        feedback_id: str,
    ) -> bool:
        """
        Delete a feedback record.
        """
        return self._repository.delete(feedback_id)

    # ------------------------------------------------------------------
    # Reinforcement
    # ------------------------------------------------------------------

    def reward_score(
        self,
        feedback: FeedbackRecord,
    ) -> float:
        """
        Compute reward score based on sentiment.
        """

        score = getattr(feedback, "score", 0.0)

        sentiment = getattr(
            feedback,
            "sentiment",
            "neutral",
        ).lower()

        if sentiment == "positive":
            score += 1.0

        elif sentiment == "negative":
            score -= 1.0

        return round(score, 3)

    def reinforce(
        self,
        confidence: float,
        feedback: FeedbackRecord,
    ) -> float:
        """
        Adjust confidence based on feedback.
        """

        sentiment = getattr(
            feedback,
            "sentiment",
            "neutral",
        ).lower()

        adjustment = 0.0

        if sentiment == "positive":
            adjustment = 0.05

        elif sentiment == "negative":
            adjustment = -0.05

        updated = confidence + adjustment

        return max(
            0.0,
            min(1.0, round(updated, 3)),
        )

    # ------------------------------------------------------------------
    # Feedback Analytics
    # ------------------------------------------------------------------

    def feedback_statistics(self) -> Dict:
        """
        Overall feedback statistics.
        """

        records = self.get_all_feedback()

        total = len(records)

        positive = sum(
            1
            for r in records
            if getattr(
                r,
                "sentiment",
                "",
            ).lower() == "positive"
        )

        negative = sum(
            1
            for r in records
            if getattr(
                r,
                "sentiment",
                "",
            ).lower() == "negative"
        )

        neutral = total - positive - negative

        average_reward = (
            sum(
                self.reward_score(r)
                for r in records
            )
            / total
            if total
            else 0.0
        )

        return {
            "total_feedback": total,
            "positive": positive,
            "negative": negative,
            "neutral": neutral,
            "average_reward": round(
                average_reward,
                3,
            ),
        }

    # ------------------------------------------------------------------
    # Feedback History
    # ------------------------------------------------------------------

    def feedback_history(self) -> List[Dict]:
        """
        Return chronological feedback history.
        """

        records = sorted(
            self.get_all_feedback(),
            key=lambda r: getattr(
                r,
                "timestamp",
                datetime.min,
            ),
        )

        history = []

        for record in records:

            history.append(
                {
                    "feedback_id": getattr(
                        record,
                        "feedback_id",
                        None,
                    ),
                    "timestamp": getattr(
                        record,
                        "timestamp",
                        None,
                    ),
                    "sentiment": getattr(
                        record,
                        "sentiment",
                        None,
                    ),
                    "score": self.reward_score(
                        record
                    ),
                }
            )

        return history

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(self) -> Dict:
        """
        Consolidated feedback summary.
        """

        return {
            "statistics": self.feedback_statistics(),
            "history": self.feedback_history(),
        }
