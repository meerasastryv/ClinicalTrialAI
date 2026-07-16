"""
adaptive_learning_service.py

Central orchestration service for the Adaptive Learning Engine.
Coordinates learning, pattern discovery, knowledge management,
and feedback processing.
"""

from __future__ import annotations

from typing import Dict, List, Optional

from src.ic06.models.feedback_record import FeedbackRecord
from src.ic06.models.knowledge_snapshot import KnowledgeSnapshot
from src.ic06.models.learning_event import LearningEvent

from src.ic06.services.feedback_service import FeedbackService
from src.ic06.services.knowledge_service import KnowledgeService
from src.ic06.services.learning_pattern_service import (
    LearningPatternService,
)
from src.ic06.services.learning_service import LearningService


class AdaptiveLearningService:
    """
    Central orchestration service.
    """

    def __init__(
        self,
        learning_service: Optional[LearningService] = None,
        pattern_service: Optional[LearningPatternService] = None,
        knowledge_service: Optional[KnowledgeService] = None,
        feedback_service: Optional[FeedbackService] = None,
    ):
        self.learning_service = (
            learning_service or LearningService()
        )

        self.pattern_service = (
            pattern_service or LearningPatternService()
        )

        self.knowledge_service = (
            knowledge_service or KnowledgeService()
        )

        self.feedback_service = (
            feedback_service or FeedbackService()
        )

    # ------------------------------------------------------------------
    # Learning
    # ------------------------------------------------------------------

    def learn(
        self,
        event: LearningEvent,
    ) -> LearningEvent:
        """
        Record a learning event.
        """
        return self.learning_service.record_event(event)

    # ------------------------------------------------------------------
    # Feedback
    # ------------------------------------------------------------------

    def process_feedback(
        self,
        feedback: FeedbackRecord,
    ) -> FeedbackRecord:
        """
        Store a feedback record.
        """
        return self.feedback_service.record_feedback(feedback)

    # ------------------------------------------------------------------
    # Knowledge
    # ------------------------------------------------------------------

    def update_knowledge(
        self,
        snapshot: KnowledgeSnapshot,
    ) -> KnowledgeSnapshot:
        """
        Save a knowledge snapshot.
        """
        return self.knowledge_service.save_snapshot(snapshot)

    # ------------------------------------------------------------------
    # Pattern Discovery
    # ------------------------------------------------------------------

    def discover_patterns(self):
        """
        Discover recurring learning patterns.
        """
        return self.pattern_service.rank_patterns()

    # ------------------------------------------------------------------
    # Recommendations
    # ------------------------------------------------------------------

    def recommendations(self) -> List[str]:
        """
        Generate adaptive recommendations.
        """

        recommendations: List[str] = []

        learning_stats = (
            self.learning_service.learning_statistics()
        )

        if learning_stats["success_rate"] < 0.60:
            recommendations.append(
                "Increase training on unsuccessful learning events."
            )

        weak_patterns = (
            self.pattern_service.weak_patterns()
        )

        if weak_patterns:
            recommendations.append(
                "Review weak learning patterns."
            )

        maturity = (
            self.knowledge_service.maturity_score()
        )

        if maturity < 0.70:
            recommendations.append(
                "Expand knowledge base."
            )

        feedback = (
            self.feedback_service.feedback_statistics()
        )

        if feedback["negative"] > feedback["positive"]:
            recommendations.append(
                "Investigate repeated negative feedback."
            )

        if not recommendations:
            recommendations.append(
                "Learning engine operating optimally."
            )

        return recommendations

    # ------------------------------------------------------------------
    # Dashboard
    # ------------------------------------------------------------------

    def dashboard(self) -> Dict:
        """
        Consolidated adaptive learning dashboard.
        """

        return {
            "learning": self.learning_service.summary(),
            "patterns": self.pattern_service.summary(),
            "knowledge": self.knowledge_service.summary(),
            "feedback": self.feedback_service.summary(),
            "recommendations": self.recommendations(),
        }

    # ------------------------------------------------------------------
    # Health Check
    # ------------------------------------------------------------------

    def health(self) -> Dict:
        """
        Overall health indicators.
        """

        learning = (
            self.learning_service.learning_statistics()
        )

        knowledge = (
            self.knowledge_service.maturity_score()
        )

        return {
            "healthy": (
                learning["success_rate"] >= 0.70
                and knowledge >= 0.70
            ),
            "success_rate": learning["success_rate"],
            "knowledge_maturity": knowledge,
        }
