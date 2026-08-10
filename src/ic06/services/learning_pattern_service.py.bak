"""
learning_pattern_service.py

Business service responsible for discovering and managing learning
patterns from historical learning events.
"""

from __future__ import annotations

from collections import Counter
from typing import Dict, List, Optional

from src.ic06.models.learning_event import LearningEvent
from src.ic06.models.learning_pattern import LearningPattern
from src.ic06.repositories.learning_repository import LearningRepository


class LearningPatternService:
    """
    Discovers recurring learning patterns from learning events.
    """

    def __init__(self,
                 repository: Optional[LearningRepository] = None):
        self._repository = repository or LearningRepository()

    # ------------------------------------------------------------------
    # Event Retrieval
    # ------------------------------------------------------------------

    def get_events(self) -> List[LearningEvent]:
        """
        Return all learning events.
        """
        return self._repository.get_all()

    # ------------------------------------------------------------------
    # Pattern Discovery
    # ------------------------------------------------------------------

    def discover_patterns(self) -> List[LearningPattern]:
        """
        Build learning patterns based on event type.
        """

        events = self.get_events()

        grouped: Dict[str, List[LearningEvent]] = {}

        for event in events:

            event_type = getattr(
                event,
                "event_type",
                "UNKNOWN",
            )

            grouped.setdefault(
                event_type,
                [],
            ).append(event)

        patterns: List[LearningPattern] = []

        for event_type, event_list in grouped.items():

            successful = sum(
                1
                for e in event_list
                if getattr(e, "success", False)
            )

            confidence = (
                successful / len(event_list)
                if event_list
                else 0.0
            )

            pattern = LearningPattern(
                pattern_name=event_type,
                occurrence_count=len(event_list),
                confidence=round(confidence, 3),
                successful_occurrences=successful,
                failed_occurrences=len(event_list) - successful,
            )

            patterns.append(pattern)

        return patterns

    # ------------------------------------------------------------------
    # Ranking
    # ------------------------------------------------------------------

    def rank_patterns(self) -> List[LearningPattern]:
        """
        Rank patterns by occurrence frequency.
        """

        return sorted(
            self.discover_patterns(),
            key=lambda p: p.occurrence_count,
            reverse=True,
        )

    # ------------------------------------------------------------------
    # Successful Strategies
    # ------------------------------------------------------------------

    def successful_patterns(self) -> List[LearningPattern]:

        return [
            pattern
            for pattern in self.discover_patterns()
            if pattern.confidence >= 0.75
        ]

    # ------------------------------------------------------------------
    # Weak Patterns
    # ------------------------------------------------------------------

    def weak_patterns(self) -> List[LearningPattern]:

        return [
            pattern
            for pattern in self.discover_patterns()
            if pattern.confidence < 0.50
        ]

    # ------------------------------------------------------------------
    # Event Frequency
    # ------------------------------------------------------------------

    def event_frequency(self) -> Dict[str, int]:
        """
        Frequency of event types.
        """

        events = self.get_events()

        counter = Counter()

        for event in events:
            counter[
                getattr(
                    event,
                    "event_type",
                    "UNKNOWN",
                )
            ] += 1

        return dict(counter)

    # ------------------------------------------------------------------
    # Pattern Statistics
    # ------------------------------------------------------------------

    def statistics(self) -> Dict:

        patterns = self.discover_patterns()

        if not patterns:

            return {
                "total_patterns": 0,
                "average_confidence": 0.0,
                "highest_confidence": 0.0,
            }

        average = sum(
            p.confidence
            for p in patterns
        ) / len(patterns)

        highest = max(
            p.confidence
            for p in patterns
        )

        return {
            "total_patterns": len(patterns),
            "average_confidence": round(
                average,
                3,
            ),
            "highest_confidence": highest,
        }

    # ------------------------------------------------------------------
    # Summary
    # ------------------------------------------------------------------

    def summary(self) -> Dict:

        return {
            "statistics": self.statistics(),
            "event_frequency": self.event_frequency(),
            "top_patterns": self.rank_patterns()[:5],
            "successful_patterns": self.successful_patterns(),
            "weak_patterns": self.weak_patterns(),
        }
