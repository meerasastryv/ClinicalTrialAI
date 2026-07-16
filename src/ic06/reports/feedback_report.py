"""
feedback_report.py

Reporting module for adaptive learning feedback.
Generates formatted reports from the FeedbackService.
"""

from __future__ import annotations

from typing import Dict, Optional

from src.ic06.services.feedback_service import FeedbackService


class FeedbackReport:
    """
    Generates reports for learning feedback and reinforcement.
    """

    def __init__(
        self,
        feedback_service: Optional[FeedbackService] = None,
    ):
        self._feedback_service = (
            feedback_service or FeedbackService()
        )

    # ------------------------------------------------------------------
    # Report Sections
    # ------------------------------------------------------------------

    def statistics(self) -> Dict:
        """
        Overall feedback statistics.
        """
        return self._feedback_service.feedback_statistics()

    def history(self) -> Dict:
        """
        Chronological feedback history.
        """
        return {
            "records": self._feedback_service.feedback_history()
        }

    def reinforcement_summary(self) -> Dict:
        """
        Reinforcement analysis.
        """
        stats = self._feedback_service.feedback_statistics()

        positive = stats["positive"]
        negative = stats["negative"]

        if positive > negative:
            trend = "Positive Reinforcement"

        elif negative > positive:
            trend = "Negative Reinforcement"

        else:
            trend = "Balanced"

        return {
            "trend": trend,
            "average_reward": stats["average_reward"],
            "positive_feedback": positive,
            "negative_feedback": negative,
        }

    # ------------------------------------------------------------------
    # Executive Summary
    # ------------------------------------------------------------------

    def executive_summary(self) -> Dict:
        """
        Executive summary for feedback.
        """

        stats = self.statistics()

        positive = stats["positive"]
        negative = stats["negative"]

        if positive > negative:
            status = "Healthy"

        elif negative > positive:
            status = "Needs Improvement"

        else:
            status = "Stable"

        return {
            "status": status,
            "total_feedback": stats["total_feedback"],
            "average_reward": stats["average_reward"],
        }

    # ------------------------------------------------------------------
    # Complete Report
    # ------------------------------------------------------------------

    def generate(self) -> Dict:
        """
        Generate complete feedback report.
        """

        return {
            "statistics": self.statistics(),
            "history": self.history(),
            "reinforcement": (
                self.reinforcement_summary()
            ),
            "executive_summary": (
                self.executive_summary()
            ),
        }
