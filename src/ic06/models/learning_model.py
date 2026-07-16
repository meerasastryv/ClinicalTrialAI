"""
learning_model.py

Adaptive Learning Engine - Learning Model

Represents the complete learned state of the Adaptive Learning Engine.

The LearningModel aggregates:

    * Learning Events
    * Learning Patterns
    * Knowledge Snapshots
    * Feedback Records

It serves as the root domain model for IC-06 and provides a unified
view of the platform's adaptive learning state.

Author: Meera Sastry
Project: ClinicalTrialAI
"""

from __future__ import annotations

import copy
import json
import uuid

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List

from src.ic06.models.feedback_record import FeedbackRecord
from src.ic06.models.knowledge_snapshot import KnowledgeSnapshot
from src.ic06.models.learning_event import LearningEvent
from src.ic06.models.learning_pattern import LearningPattern


# ==============================================================================
# Constants
# ==============================================================================

DEFAULT_MODEL_VERSION = "1.0"

DEFAULT_CONFIDENCE = 1.0


# ==============================================================================
# Learning Model
# ==============================================================================


@dataclass
class LearningModel:
    """
    Root aggregate for the Adaptive Learning Engine.
    """

    model_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    name: str = "Adaptive Learning Model"

    description: str = ""

    version: str = DEFAULT_MODEL_VERSION

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    last_updated: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    learning_events: List[LearningEvent] = field(
        default_factory=list
    )

    learning_patterns: List[LearningPattern] = field(
        default_factory=list
    )

    knowledge_snapshots: List[KnowledgeSnapshot] = field(
        default_factory=list
    )

    feedback_records: List[FeedbackRecord] = field(
        default_factory=list
    )

    overall_confidence: float = DEFAULT_CONFIDENCE

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

        if not self.name.strip():
            raise ValueError(
                "Model name cannot be empty."
            )

        if self.overall_confidence < 0:
            raise ValueError(
                "Confidence cannot be negative."
            )

    # ------------------------------------------------------------------
    # Learning Events
    # ------------------------------------------------------------------

    def add_learning_event(
        self,
        event: LearningEvent,
    ) -> None:
        """
        Adds a learning event.
        """
        self.learning_events.append(event)
        self.touch()

    def remove_learning_event(
        self,
        event_id: str,
    ) -> None:
        """
        Removes a learning event by ID.
        """
        self.learning_events = [
            event
            for event in self.learning_events
            if event.event_id != event_id
        ]
        self.touch()

    # ------------------------------------------------------------------
    # Learning Patterns
    # ------------------------------------------------------------------

    def add_learning_pattern(
        self,
        pattern: LearningPattern,
    ) -> None:
        """
        Adds a learning pattern.
        """
        self.learning_patterns.append(pattern)
        self.touch()

    def remove_learning_pattern(
        self,
        pattern_id: str,
    ) -> None:
        """
        Removes a learning pattern by ID.
        """
        self.learning_patterns = [
            pattern
            for pattern in self.learning_patterns
            if pattern.pattern_id != pattern_id
        ]
        self.touch()

    # ------------------------------------------------------------------
    # Knowledge Snapshots
    # ------------------------------------------------------------------

    def add_snapshot(
        self,
        snapshot: KnowledgeSnapshot,
    ) -> None:
        """
        Adds a knowledge snapshot.
        """
        self.knowledge_snapshots.append(snapshot)
        self.touch()

    def remove_snapshot(
        self,
        snapshot_id: str,
    ) -> None:
        """
        Removes a knowledge snapshot by ID.
        """
        self.knowledge_snapshots = [
            snapshot
            for snapshot in self.knowledge_snapshots
            if snapshot.snapshot_id != snapshot_id
        ]
        self.touch()

    # ------------------------------------------------------------------
    # Feedback Records
    # ------------------------------------------------------------------

    def add_feedback(
        self,
        feedback: FeedbackRecord,
    ) -> None:
        """
        Adds a feedback record.
        """
        self.feedback_records.append(feedback)
        self.touch()

    def remove_feedback(
        self,
        feedback_id: str,
    ) -> None:
        """
        Removes a feedback record by ID.
        """
        self.feedback_records = [
            feedback
            for feedback in self.feedback_records
            if feedback.feedback_id != feedback_id
        ]
        self.touch()

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def event_count(self) -> int:
        """
        Returns the number of learning events.
        """
        return len(self.learning_events)

    def pattern_count(self) -> int:
        """
        Returns the number of learning patterns.
        """
        return len(self.learning_patterns)

    def snapshot_count(self) -> int:
        """
        Returns the number of knowledge snapshots.
        """
        return len(self.knowledge_snapshots)

    def feedback_count(self) -> int:
        """
        Returns the number of feedback records.
        """
        return len(self.feedback_records)

    # ------------------------------------------------------------------
    # Learning Metrics
    # ------------------------------------------------------------------

    def update_confidence(
        self,
        confidence: float,
    ) -> None:
        """
        Updates overall confidence.
        """
        if confidence < 0:
            raise ValueError(
                "Confidence cannot be negative."
            )

        self.overall_confidence = confidence
        self.touch()

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
        self.touch()

    def remove_metadata(
        self,
        key: str,
    ) -> None:
        """
        Removes metadata.
        """
        self.metadata.pop(key, None)
        self.touch()

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
            self.touch()

    def remove_tag(
        self,
        tag: str,
    ) -> None:
        """
        Removes a tag.
        """
        if tag in self.tags:
            self.tags.remove(tag)
            self.touch()

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------

    def touch(self) -> None:
        """
        Updates the last modified timestamp.
        """
        self.last_updated = datetime.now(
            timezone.utc
        )

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the learning model into a dictionary.
        """
        return {
            "model_id": self.model_id,
            "name": self.name,
            "description": self.description,
            "version": self.version,
            "created_at": self.created_at.isoformat(),
            "last_updated": self.last_updated.isoformat(),
            "learning_events": [
                event.to_dict()
                for event in self.learning_events
            ],
            "learning_patterns": [
                pattern.to_dict()
                for pattern in self.learning_patterns
            ],
            "knowledge_snapshots": [
                snapshot.to_dict()
                for snapshot in self.knowledge_snapshots
            ],
            "feedback_records": [
                feedback.to_dict()
                for feedback in self.feedback_records
            ],
            "overall_confidence": self.overall_confidence,
            "metadata": self.metadata,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(
        cls,
        data: Dict[str, Any],
    ) -> "LearningModel":
        """
        Creates a LearningModel from a dictionary.
        """
        return cls(
            model_id=data.get(
                "model_id",
                str(uuid.uuid4()),
            ),
            name=data.get(
                "name",
                "Adaptive Learning Model",
            ),
            description=data.get(
                "description",
                "",
            ),
            version=data.get(
                "version",
                DEFAULT_MODEL_VERSION,
            ),
            created_at=datetime.fromisoformat(
                data.get(
                    "created_at",
                    datetime.now(
                        timezone.utc
                    ).isoformat(),
                )
            ),
            last_updated=datetime.fromisoformat(
                data.get(
                    "last_updated",
                    datetime.now(
                        timezone.utc
                    ).isoformat(),
                )
            ),
            learning_events=[
                LearningEvent.from_dict(event)
                for event in data.get(
                    "learning_events",
                    [],
                )
            ],
            learning_patterns=[
                LearningPattern.from_dict(pattern)
                for pattern in data.get(
                    "learning_patterns",
                    [],
                )
            ],
            knowledge_snapshots=[
                KnowledgeSnapshot.from_dict(snapshot)
                for snapshot in data.get(
                    "knowledge_snapshots",
                    [],
                )
            ],
            feedback_records=[
                FeedbackRecord.from_dict(feedback)
                for feedback in data.get(
                    "feedback_records",
                    [],
                )
            ],
            overall_confidence=data.get(
                "overall_confidence",
                DEFAULT_CONFIDENCE,
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
        Converts the learning model to JSON.
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
    ) -> "LearningModel":
        """
        Creates a LearningModel from JSON.
        """
        return cls.from_dict(
            json.loads(json_string)
        )

    # ------------------------------------------------------------------
    # Copy Utilities
    # ------------------------------------------------------------------

    def copy(self) -> "LearningModel":
        """
        Returns a deep copy of the learning model.
        """
        return copy.deepcopy(self)

    def clone_with_updates(
        self,
        **updates: Any,
    ) -> "LearningModel":
        """
        Creates a cloned learning model with updated fields.
        """
        cloned = self.copy()

        for key, value in updates.items():
            if hasattr(cloned, key):
                setattr(cloned, key, value)

        cloned.touch()

        return cloned

    # ------------------------------------------------------------------
    # String Representation
    # ------------------------------------------------------------------

    def __str__(self) -> str:
        """
        Human-readable representation.
        """
        return (
            f"LearningModel("
            f"name='{self.name}', "
            f"version='{self.version}', "
            f"events={self.event_count()}, "
            f"patterns={self.pattern_count()}, "
            f"snapshots={self.snapshot_count()}, "
            f"feedback={self.feedback_count()}, "
            f"confidence={self.overall_confidence:.2f})"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """
        return self.__str__()


