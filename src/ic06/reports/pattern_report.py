"""
pattern_report.py

Reporting module for learning pattern analytics.
Generates formatted reports from the LearningPatternService.
"""

from __future__ import annotations

from typing import Dict, Optional

from src.ic06.services.learning_pattern_service import (
    LearningPatternService,
)


class PatternReport:
    """
    Generates reports for discovered learning patterns.
    """

    def __init__(
        self,
        pattern_service: Optional[LearningPatternService] = None,
    ):
        self._pattern_service = (
            pattern_service or LearningPatternService()
        )

    # ------------------------------------------------------------------
    # Report Sections
    # ------------------------------------------------------------------

    def statistics(self) -> Dict:
        """
        Pattern statistics.
        """
        return self._pattern_service.statistics()

    def frequency(self) -> Dict:
        """
        Event frequency by pattern.
        """
        return self._pattern_service.event_frequency()

    def top_patterns(self) -> Dict:
        """
        Top ranked learning patterns.
        """
        patterns = self._pattern_service.rank_patterns()

        return {
            "count": len(patterns),
            "patterns": patterns,
        }

    def successful_patterns(self) -> Dict:
        """
        High-confidence learning patterns.
        """
        patterns = self._pattern_service.successful_patterns()

        return {
            "count": len(patterns),
            "patterns": patterns,
        }

    def weak_patterns(self) -> Dict:
        """
        Low-confidence learning patterns.
        """
        patterns = self._pattern_service.weak_patterns()

        return {
            "count": len(patterns),
            "patterns": patterns,
        }

    # ------------------------------------------------------------------
    # Executive Summary
    # ------------------------------------------------------------------

    def executive_summary(self) -> Dict:
        """
        Executive summary of discovered patterns.
        """

        stats = self.statistics()

        if stats["total_patterns"] == 0:
            status = "No Patterns Available"
        elif stats["average_confidence"] >= 0.70:
            status = "Healthy"
        else:
            status = "Needs Improvement"

        return {
            "status": status,
            "total_patterns": stats["total_patterns"],
            "average_confidence": (
                stats["average_confidence"]
            ),
            "highest_confidence": (
                stats["highest_confidence"]
            ),
        }

    # ------------------------------------------------------------------
    # Complete Report
    # ------------------------------------------------------------------

    def generate(self) -> Dict:
        """
        Generate complete pattern report.
        """

        return {
            "statistics": self.statistics(),
            "frequency": self.frequency(),
            "top_patterns": self.top_patterns(),
            "successful_patterns": (
                self.successful_patterns()
            ),
            "weak_patterns": self.weak_patterns(),
            "executive_summary": (
                self.executive_summary()
            ),
        }
