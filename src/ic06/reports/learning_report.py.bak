"""
learning_report.py

Reporting module for adaptive learning analytics.
Generates formatted reports from the LearningService.
"""

from __future__ import annotations

from typing import Dict, Optional

from src.ic06.services.learning_service import LearningService


class LearningReport:
    """
    Generates reports for learning analytics.
    """

    def __init__(
        self,
        learning_service: Optional[LearningService] = None,
    ):
        self._learning_service = (
            learning_service or LearningService()
        )

    # ------------------------------------------------------------------
    # Report Sections
    # ------------------------------------------------------------------

    def statistics(self) -> Dict:
        """
        Learning statistics.
        """
        return self._learning_service.learning_statistics()

    def confidence_trend(self) -> Dict:
        """
        Confidence progression.
        """
        return {
            "confidence_growth":
                self._learning_service.confidence_growth()
        }

    def learning_velocity(self) -> Dict:
        """
        Learning velocity.
        """
        return {
            "learning_velocity":
                self._learning_service.learning_velocity()
        }

    def success_trend(self) -> Dict:
        """
        Success vs failure counts.
        """
        return self._learning_service.success_trend()

    def event_summary(self) -> Dict:
        """
        Event summary.
        """
        events = self._learning_service.get_all_events()

        return {
            "total_events": len(events),
            "successful_events": len(
                self._learning_service.get_successful_events()
            ),
            "failed_events": len(
                self._learning_service.get_failed_events()
            ),
        }

    # ------------------------------------------------------------------
    # Executive Summary
    # ------------------------------------------------------------------

    def executive_summary(self) -> Dict:
        """
        Executive summary of learning performance.
        """
        stats = self.statistics()

        return {
            "status": (
                "Healthy"
                if stats["success_rate"] >= 0.70
                else "Needs Improvement"
            ),
            "success_rate": stats["success_rate"],
            "average_confidence":
                stats["average_confidence"],
            "learning_velocity":
                self._learning_service.learning_velocity(),
        }

    # ------------------------------------------------------------------
    # Complete Report
    # ------------------------------------------------------------------

    def generate(self) -> Dict:
        """
        Generate complete learning report.
        """
        return {
            "statistics": self.statistics(),
            "event_summary": self.event_summary(),
            "success_trend": self.success_trend(),
            "confidence_trend": self.confidence_trend(),
            "learning_velocity": self.learning_velocity(),
            "executive_summary": self.executive_summary(),
        }
