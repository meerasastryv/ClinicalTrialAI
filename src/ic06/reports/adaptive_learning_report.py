"""
adaptive_learning_report.py

Executive reporting module for the Adaptive Learning Engine.
Aggregates all reporting modules into a unified dashboard.
"""

from __future__ import annotations

from typing import Dict, Optional

from src.ic06.reports.feedback_report import FeedbackReport
from src.ic06.reports.knowledge_report import KnowledgeReport
from src.ic06.reports.learning_report import LearningReport
from src.ic06.reports.pattern_report import PatternReport
from src.ic06.services.adaptive_learning_service import (
    AdaptiveLearningService,
)


class AdaptiveLearningReport:
    """
    Executive dashboard for the Adaptive Learning Engine.
    """

    def __init__(
        self,
        adaptive_service: Optional[
            AdaptiveLearningService
        ] = None,
        learning_report: Optional[
            LearningReport
        ] = None,
        pattern_report: Optional[
            PatternReport
        ] = None,
        knowledge_report: Optional[
            KnowledgeReport
        ] = None,
        feedback_report: Optional[
            FeedbackReport
        ] = None,
    ):
        self._adaptive_service = (
            adaptive_service
            or AdaptiveLearningService()
        )

        self._learning_report = (
            learning_report
            or LearningReport()
        )

        self._pattern_report = (
            pattern_report
            or PatternReport()
        )

        self._knowledge_report = (
            knowledge_report
            or KnowledgeReport()
        )

        self._feedback_report = (
            feedback_report
            or FeedbackReport()
        )

    # ------------------------------------------------------------------
    # Report Sections
    # ------------------------------------------------------------------

    def learning(self) -> Dict:
        """
        Learning report.
        """
        return self._learning_report.generate()

    def patterns(self) -> Dict:
        """
        Pattern report.
        """
        return self._pattern_report.generate()

    def knowledge(self) -> Dict:
        """
        Knowledge report.
        """
        return self._knowledge_report.generate()

    def feedback(self) -> Dict:
        """
        Feedback report.
        """
        return self._feedback_report.generate()

    def recommendations(self):
        """
        Adaptive recommendations.
        """
        return self._adaptive_service.recommendations()

    def health(self) -> Dict:
        """
        Overall adaptive learning health.
        """
        return self._adaptive_service.health()

    # ------------------------------------------------------------------
    # Executive Summary
    # ------------------------------------------------------------------

    def executive_summary(self) -> Dict:
        """
        High-level executive summary.
        """

        health = self.health()

        if health["healthy"]:
            overall_status = "Healthy"
        else:
            overall_status = "Needs Improvement"

        return {
            "overall_status": overall_status,
            "success_rate": health["success_rate"],
            "knowledge_maturity": (
                health["knowledge_maturity"]
            ),
            "recommendations": (
                self.recommendations()
            ),
        }

    # ------------------------------------------------------------------
    # Complete Dashboard
    # ------------------------------------------------------------------

    def generate(self) -> Dict:
        """
        Generate the complete adaptive learning dashboard.
        """

        return {
            "learning": self.learning(),
            "patterns": self.patterns(),
            "knowledge": self.knowledge(),
            "feedback": self.feedback(),
            "health": self.health(),
            "recommendations": (
                self.recommendations()
            ),
            "executive_summary": (
                self.executive_summary()
            ),
        }
