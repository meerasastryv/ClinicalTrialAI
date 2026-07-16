"""
feedback_record.py

Adaptive Learning Engine - Feedback Record Model

Represents feedback received from users, automated systems,
predictions and recommendations.

Feedback is the reinforcement signal used by the Adaptive
Learning Engine to continuously improve prediction accuracy.

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


class FeedbackType(Enum):
    """
    Type of feedback.
    """

    USER = "user"

    SYSTEM = "system"

    AUTOMATED = "automated"

    PREDICTION = "prediction"

    RECOMMENDATION = "recommendation"

    EXECUTION = "execution"

    QUALITY = "quality"

    CUSTOM = "custom"


class FeedbackOutcome(Enum):
    """
    Outcome of the feedback.
    """

    POSITIVE = "positive"

    NEGATIVE = "negative"

    NEUTRAL = "neutral"

    PARTIAL = "partial"

    UNKNOWN = "unknown"


class FeedbackStatus(Enum):
    """
    Lifecycle status.
    """

    NEW = "new"

    PROCESSED = "processed"

    LEARNING_APPLIED = "learning_applied"

    ARCHIVED = "archived"


# ==============================================================================
# Constants
# ==============================================================================

DEFAULT_RATING = 0.0

DEFAULT_CONFIDENCE = 1.0


# ==============================================================================
# Feedback Record
# ==============================================================================


@dataclass
class FeedbackRecord:
    """
    Represents a feedback record used by the Adaptive Learning Engine.
    """

    feedback_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    feedback_type: FeedbackType = FeedbackType.SYSTEM

    status: FeedbackStatus = FeedbackStatus.NEW

    outcome: FeedbackOutcome = FeedbackOutcome.UNKNOWN

    source: str = ""

    reference_id: str = ""

    title: str = ""

    description: str = ""

    rating: float = DEFAULT_RATING

    confidence_before: float = DEFAULT_CONFIDENCE

    confidence_after: float = DEFAULT_CONFIDENCE

    learning_delta: float = 0.0

    timestamp: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    reviewed_by: str = ""

    processed_at: datetime | None = None

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
        self.validate()

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def validate(self) -> None:

        if not self.title.strip():
            raise ValueError(
                "Feedback title cannot be empty."
            )

        if self.rating < 0:
            raise ValueError(
                "Rating cannot be negative."
            )

        if self.confidence_before < 0:
            raise ValueError(
                "Confidence cannot be negative."
            )

        if self.confidence_after < 0:
            raise ValueError(
                "Confidence cannot be negative."
            )

    # ------------------------------------------------------------------
    # Feedback Analysis
    # ------------------------------------------------------------------

    def is_positive(self) -> bool:
        """
        Returns True if the feedback outcome is positive.
        """
        return self.outcome == FeedbackOutcome.POSITIVE

    def is_negative(self) -> bool:
        """
        Returns True if the feedback outcome is negative.
        """
        return self.outcome == FeedbackOutcome.NEGATIVE

    def is_neutral(self) -> bool:
        """
        Returns True if the feedback outcome is neutral.
        """
        return self.outcome == FeedbackOutcome.NEUTRAL

    # ------------------------------------------------------------------
    # Learning
    # ------------------------------------------------------------------

    def apply_learning_delta(self, delta: float) -> None:
        """
        Applies a learning delta and updates confidence.
        """
        self.learning_delta = delta
        self.confidence_after = max(
            0.0,
            self.confidence_before + delta
        )

    def update_confidence(
        self,
        before: float,
        after: float,
    ) -> None:
        """
        Updates confidence values.
        """
        if before < 0 or after < 0:
            raise ValueError(
                "Confidence values cannot be negative."
            )

        self.confidence_before = before
        self.confidence_after = after

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

    def remove_metadata(
        self,
        key: str,
    ) -> None:
        """
        Removes metadata.
        """
        self.metadata.pop(key, None)

    # ------------------------------------------------------------------
    # Tags
    # ------------------------------------------------------------------

    def add_tag(
        self,
        tag: str,
    ) -> None:
        """
        Adds a tag.
        """
        if tag and tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(
        self,
        tag: str,
    ) -> None:
        """
        Removes a tag.
        """
        if tag in self.tags:
            self.tags.remove(tag)

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def mark_processed(
        self,
        reviewer: str = "",
    ) -> None:
        """
        Marks feedback as processed.
        """
        self.status = FeedbackStatus.PROCESSED
        self.reviewed_by = reviewer
        self.processed_at = datetime.now(
            timezone.utc
        )

    def mark_learning_applied(self) -> None:
        """
        Marks learning as applied.
        """
        self.status = FeedbackStatus.LEARNING_APPLIED

    def archive(self) -> None:
        """
        Archives the feedback record.
        """
        self.status = FeedbackStatus.ARCHIVED

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------

    def age_in_days(self) -> int:
        """
        Returns the age of the feedback record in days.
        """
        return (
            datetime.now(timezone.utc) - self.timestamp
        ).days


    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the feedback record into a dictionary.
        """
        return {
            "feedback_id": self.feedback_id,
            "feedback_type": self.feedback_type.value,
            "status": self.status.value,
            "outcome": self.outcome.value,
            "source": self.source,
            "reference_id": self.reference_id,
            "title": self.title,
            "description": self.description,
            "rating": self.rating,
            "confidence_before": self.confidence_before,
            "confidence_after": self.confidence_after,
            "learning_delta": self.learning_delta,
            "timestamp": self.timestamp.isoformat(),
            "reviewed_by": self.reviewed_by,
            "processed_at": (
                self.processed_at.isoformat()
                if self.processed_at
                else None
            ),
            "metadata": self.metadata,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(
        cls,
        data: Dict[str, Any],
    ) -> "FeedbackRecord":
        """
        Creates a FeedbackRecord from a dictionary.
        """
        return cls(
            feedback_id=data.get(
                "feedback_id",
                str(uuid.uuid4()),
            ),
            feedback_type=FeedbackType(
                data.get(
                    "feedback_type",
                    FeedbackType.SYSTEM.value,
                )
            ),
            status=FeedbackStatus(
                data.get(
                    "status",
                    FeedbackStatus.NEW.value,
                )
            ),
            outcome=FeedbackOutcome(
                data.get(
                    "outcome",
                    FeedbackOutcome.UNKNOWN.value,
                )
            ),
            source=data.get("source", ""),
            reference_id=data.get("reference_id", ""),
            title=data.get("title", ""),
            description=data.get("description", ""),
            rating=data.get("rating", DEFAULT_RATING),
            confidence_before=data.get(
                "confidence_before",
                DEFAULT_CONFIDENCE,
            ),
            confidence_after=data.get(
                "confidence_after",
                DEFAULT_CONFIDENCE,
            ),
            learning_delta=data.get(
                "learning_delta",
                0.0,
            ),
            timestamp=datetime.fromisoformat(
                data.get(
                    "timestamp",
                    datetime.now(
                        timezone.utc
                    ).isoformat(),
                )
            ),
            reviewed_by=data.get(
                "reviewed_by",
                "",
            ),
            processed_at=(
                datetime.fromisoformat(
                    data["processed_at"]
                )
                if data.get("processed_at")
                else None
            ),
            metadata=data.get("metadata", {}),
            tags=data.get("tags", []),
        )

    def to_json(
        self,
        indent: int = 4,
    ) -> str:
        """
        Converts the feedback record to JSON.
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
    ) -> "FeedbackRecord":
        """
        Creates a FeedbackRecord from JSON.
        """
        return cls.from_dict(
            json.loads(json_string)
        )

    # ------------------------------------------------------------------
    # Copy Utilities
    # ------------------------------------------------------------------

    def copy(self) -> "FeedbackRecord":
        """
        Returns a deep copy of the feedback record.
        """
        return copy.deepcopy(self)

    def clone_with_updates(
        self,
        **updates: Any,
    ) -> "FeedbackRecord":
        """
        Creates a cloned feedback record with updated fields.
        """
        cloned = self.copy()

        for key, value in updates.items():
            if hasattr(cloned, key):
                setattr(cloned, key, value)

        return cloned

    # ------------------------------------------------------------------
    # String Representation
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """
        Human-readable representation.
        """
        return (
            f"FeedbackRecord("
            f"title='{self.title}', "
            f"outcome='{self.outcome.value}', "
            f"status='{self.status.value}', "
            f"rating={self.rating:.2f})"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """
        return self.__str__()


