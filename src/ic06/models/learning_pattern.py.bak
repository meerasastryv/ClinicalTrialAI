"""
learning_pattern.py

Adaptive Learning Engine - Learning Pattern Model

This module defines the LearningPattern model used by the Adaptive
Learning Engine (IC-06).

A LearningPattern represents recurring knowledge discovered by analyzing
multiple LearningEvent instances over time.

Learning patterns help identify:

    * Frequently failing modules
    * Recurring defects
    * Runtime bottlenecks
    * Performance degradation
    * Requirement volatility
    * Stable execution trends
    * Risk hotspots
    * Code hotspots

Author: Meera Sastry
Project: ClinicalTrialAI
"""

from __future__ import annotations

import copy
import json
import uuid

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List


# ==============================================================================
# Enumerations
# ==============================================================================


class PatternType(Enum):
    """
    Type of learning pattern.
    """

    FAILURE = "failure"
    SUCCESS = "success"
    CHANGE = "change"
    PERFORMANCE = "performance"
    QUALITY = "quality"
    RISK = "risk"
    DEPENDENCY = "dependency"
    EXECUTION = "execution"
    USAGE = "usage"
    SECURITY = "security"
    CUSTOM = "custom"


class PatternStatus(Enum):
    """
    Current lifecycle state of the pattern.
    """

    NEW = "new"
    ACTIVE = "active"
    STABLE = "stable"
    DECLINING = "declining"
    RESOLVED = "resolved"
    ARCHIVED = "archived"


# ==============================================================================
# Constants
# ==============================================================================

DEFAULT_CONFIDENCE = 1.0

MIN_CONFIDENCE = 0.0

MAX_CONFIDENCE = 1.0


# ==============================================================================
# Learning Pattern
# ==============================================================================


@dataclass
class LearningPattern:
    """
    Represents a recurring learning pattern discovered by the
    Adaptive Learning Engine.
    """

    pattern_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    name: str = ""

    description: str = ""

    pattern_type: PatternType = PatternType.CUSTOM

    status: PatternStatus = PatternStatus.NEW

    confidence: float = DEFAULT_CONFIDENCE

    support: int = 0

    frequency: float = 0.0

    occurrences: int = 0

    first_seen: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    last_seen: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    related_event_ids: List[str] = field(
        default_factory=list
    )

    affected_components: List[str] = field(
        default_factory=list
    )

    metadata: Dict[str, Any] = field(
        default_factory=dict
    )

    tags: List[str] = field(
        default_factory=list
    )

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def __post_init__(self) -> None:
        """
        Performs validation after object creation.
        """
        self.validate()

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def validate(self) -> None:
        """
        Validates the learning pattern.
        """

        if not self.name.strip():
            raise ValueError(
                "Pattern name cannot be empty."
            )

        if not (
            MIN_CONFIDENCE
            <= self.confidence
            <= MAX_CONFIDENCE
        ):
            raise ValueError(
                "Confidence must be between 0 and 1."
            )

        if self.support < 0:
            raise ValueError(
                "Support cannot be negative."
            )

        if self.frequency < 0:
            raise ValueError(
                "Frequency cannot be negative."
            )

        if self.occurrences < 0:
            raise ValueError(
                "Occurrences cannot be negative."
            )

        if self.last_seen < self.first_seen:
            raise ValueError(
                "last_seen cannot be earlier than first_seen."
            )

    # ------------------------------------------------------------------
    # Pattern Statistics
    # ------------------------------------------------------------------

    def increment_occurrence(self, count: int = 1) -> None:
        """
        Increments the occurrence count.

        Args:
            count:
                Number of occurrences to add.
        """
        if count < 1:
            raise ValueError("Count must be greater than zero.")

        self.occurrences += count
        self.last_seen = datetime.now(timezone.utc)

    def update_confidence(self, confidence: float) -> None:
        """
        Updates the confidence score.

        Args:
            confidence:
                Confidence value between 0 and 1.
        """
        if not MIN_CONFIDENCE <= confidence <= MAX_CONFIDENCE:
            raise ValueError(
                "Confidence must be between 0 and 1."
            )

        self.confidence = confidence
        self.last_seen = datetime.now(timezone.utc)

    def update_support(self, support: int) -> None:
        """
        Updates support count.
        """
        if support < 0:
            raise ValueError(
                "Support cannot be negative."
            )

        self.support = support

    def update_frequency(self, frequency: float) -> None:
        """
        Updates pattern frequency.
        """
        if frequency < 0:
            raise ValueError(
                "Frequency cannot be negative."
            )

        self.frequency = frequency

    # ------------------------------------------------------------------
    # Related Events
    # ------------------------------------------------------------------

    def add_event(self, event_id: str) -> None:
        """
        Adds a related learning event.
        """
        if event_id and event_id not in self.related_event_ids:
            self.related_event_ids.append(event_id)

    def remove_event(self, event_id: str) -> None:
        """
        Removes a related learning event.
        """
        if event_id in self.related_event_ids:
            self.related_event_ids.remove(event_id)

    # ------------------------------------------------------------------
    # Components
    # ------------------------------------------------------------------

    def add_component(self, component: str) -> None:
        """
        Adds an affected component.
        """
        if component and component not in self.affected_components:
            self.affected_components.append(component)

    def remove_component(self, component: str) -> None:
        """
        Removes an affected component.
        """
        if component in self.affected_components:
            self.affected_components.remove(component)

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    def add_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Adds metadata.
        """
        self.metadata[key] = value

    def remove_metadata(self, key: str) -> None:
        """
        Removes metadata.
        """
        self.metadata.pop(key, None)

    # ------------------------------------------------------------------
    # Tags
    # ------------------------------------------------------------------

    def add_tag(self, tag: str) -> None:
        """
        Adds a tag.
        """
        if tag and tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str) -> None:
        """
        Removes a tag.
        """
        if tag in self.tags:
            self.tags.remove(tag)

    # ------------------------------------------------------------------
    # Status
    # ------------------------------------------------------------------

    def mark_active(self) -> None:
        """
        Marks the pattern as active.
        """
        self.status = PatternStatus.ACTIVE

    def mark_stable(self) -> None:
        """
        Marks the pattern as stable.
        """
        self.status = PatternStatus.STABLE

    def mark_declining(self) -> None:
        """
        Marks the pattern as declining.
        """
        self.status = PatternStatus.DECLINING

    def mark_resolved(self) -> None:
        """
        Marks the pattern as resolved.
        """
        self.status = PatternStatus.RESOLVED

    def archive(self) -> None:
        """
        Archives the pattern.
        """
        self.status = PatternStatus.ARCHIVED

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------

    def age_in_days(self) -> int:
        """
        Returns the age of the pattern in days.
        """
        return (
            datetime.now(timezone.utc) - self.first_seen
        ).days

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the learning pattern into a dictionary.
        """
        return {
            "pattern_id": self.pattern_id,
            "name": self.name,
            "description": self.description,
            "pattern_type": self.pattern_type.value,
            "status": self.status.value,
            "confidence": self.confidence,
            "support": self.support,
            "frequency": self.frequency,
            "occurrences": self.occurrences,
            "first_seen": self.first_seen.isoformat(),
            "last_seen": self.last_seen.isoformat(),
            "related_event_ids": self.related_event_ids,
            "affected_components": self.affected_components,
            "metadata": self.metadata,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(
        cls,
        data: Dict[str, Any],
    ) -> "LearningPattern":
        """
        Creates a LearningPattern from a dictionary.
        """
        return cls(
            pattern_id=data.get(
                "pattern_id",
                str(uuid.uuid4()),
            ),
            name=data.get("name", ""),
            description=data.get(
                "description",
                "",
            ),
            pattern_type=PatternType(
                data.get(
                    "pattern_type",
                    PatternType.CUSTOM.value,
                )
            ),
            status=PatternStatus(
                data.get(
                    "status",
                    PatternStatus.NEW.value,
                )
            ),
            confidence=data.get(
                "confidence",
                DEFAULT_CONFIDENCE,
            ),
            support=data.get("support", 0),
            frequency=data.get("frequency", 0.0),
            occurrences=data.get(
                "occurrences",
                0,
            ),
            first_seen=datetime.fromisoformat(
                data.get(
                    "first_seen",
                    datetime.now(
                        timezone.utc
                    ).isoformat(),
                )
            ),
            last_seen=datetime.fromisoformat(
                data.get(
                    "last_seen",
                    datetime.now(
                        timezone.utc
                    ).isoformat(),
                )
            ),
            related_event_ids=data.get(
                "related_event_ids",
                [],
            ),
            affected_components=data.get(
                "affected_components",
                [],
            ),
            metadata=data.get(
                "metadata",
                {},
            ),
            tags=data.get(
                "tags",
                [],
            ),
        )

    def to_json(
        self,
        indent: int = 4,
    ) -> str:
        """
        Converts the pattern to JSON.
        """
        return json.dumps(
            self.to_dict(),
            indent=indent,
            ensure_ascii=False,
        )

    @classmethod
    def from_json(
        cls,
        json_string: str,
    ) -> "LearningPattern":
        """
        Creates a pattern from JSON.
        """
        return cls.from_dict(
            json.loads(json_string)
        )

    # ------------------------------------------------------------------
    # Copy Utilities
    # ------------------------------------------------------------------

    def copy(self) -> "LearningPattern":
        """
        Returns a deep copy of the pattern.
        """
        return copy.deepcopy(self)

    def clone_with_updates(
        self,
        **updates: Any,
    ) -> "LearningPattern":
        """
        Creates a cloned pattern with updated fields.
        """
        cloned = self.copy()

        for key, value in updates.items():
            if hasattr(cloned, key):
                setattr(cloned, key, value)

        cloned.last_seen = datetime.now(
            timezone.utc
        )

        return cloned

    # ------------------------------------------------------------------
    # String Representation
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """
        Human-readable representation.
        """
        return (
            f"LearningPattern("
            f"name='{self.name}', "
            f"type='{self.pattern_type.value}', "
            f"status='{self.status.value}', "
            f"confidence={self.confidence:.2f}, "
            f"occurrences={self.occurrences})"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """
        return self.__str__()
