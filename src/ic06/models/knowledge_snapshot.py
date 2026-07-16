"""
knowledge_snapshot.py

Adaptive Learning Engine - Knowledge Snapshot Model

Represents the learned state of the platform at a specific point in time.

Snapshots are used for:

    * Learning history
    * Trend analysis
    * Growth measurement
    * Recommendation improvement
    * Knowledge evolution
    * Release comparison

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


class SnapshotType(Enum):
    """
    Type of knowledge snapshot.
    """

    MANUAL = "manual"

    SCHEDULED = "scheduled"

    LEARNING = "learning"

    TRAINING = "training"

    RELEASE = "release"

    SYSTEM = "system"

    CUSTOM = "custom"


class SnapshotStatus(Enum):
    """
    Lifecycle status.
    """

    ACTIVE = "active"

    ARCHIVED = "archived"

    LOCKED = "locked"

    DELETED = "deleted"


# ==============================================================================
# Constants
# ==============================================================================

DEFAULT_LEARNING_SCORE = 0.0

DEFAULT_CONFIDENCE = 1.0


# ==============================================================================
# Knowledge Snapshot
# ==============================================================================


@dataclass
class KnowledgeSnapshot:
    """
    Represents a snapshot of learned platform knowledge.
    """

    snapshot_id: str = field(
        default_factory=lambda: str(uuid.uuid4())
    )

    name: str = ""

    description: str = ""

    snapshot_type: SnapshotType = SnapshotType.MANUAL

    status: SnapshotStatus = SnapshotStatus.ACTIVE

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    created_by: str = "System"

    version: str = "1.0"

    learning_model_version: str = "1.0"

    event_count: int = 0

    pattern_count: int = 0

    feedback_count: int = 0

    recommendation_count: int = 0

    knowledge_graph_nodes: int = 0

    knowledge_graph_edges: int = 0

    average_confidence: float = DEFAULT_CONFIDENCE

    learning_score: float = DEFAULT_LEARNING_SCORE

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
                "Snapshot name cannot be empty."
            )

        if self.average_confidence < 0:
            raise ValueError(
                "Average confidence cannot be negative."
            )

        if self.learning_score < 0:
            raise ValueError(
                "Learning score cannot be negative."
            )

    # ------------------------------------------------------------------
    # Statistics
    # ------------------------------------------------------------------

    def increment_event_count(self, count: int = 1) -> None:
        """
        Increments the learning event count.
        """
        if count < 0:
            raise ValueError("Count cannot be negative.")

        self.event_count += count

    def increment_pattern_count(self, count: int = 1) -> None:
        """
        Increments the learning pattern count.
        """
        if count < 0:
            raise ValueError("Count cannot be negative.")

        self.pattern_count += count

    def increment_feedback_count(self, count: int = 1) -> None:
        """
        Increments the feedback count.
        """
        if count < 0:
            raise ValueError("Count cannot be negative.")

        self.feedback_count += count

    def increment_recommendation_count(
        self,
        count: int = 1,
    ) -> None:
        """
        Increments the recommendation count.
        """
        if count < 0:
            raise ValueError("Count cannot be negative.")

        self.recommendation_count += count

    # ------------------------------------------------------------------
    # Knowledge Graph Metrics
    # ------------------------------------------------------------------

    def update_graph_metrics(
        self,
        nodes: int,
        edges: int,
    ) -> None:
        """
        Updates Knowledge Graph statistics.
        """
        if nodes < 0 or edges < 0:
            raise ValueError(
                "Graph metrics cannot be negative."
            )

        self.knowledge_graph_nodes = nodes
        self.knowledge_graph_edges = edges

    # ------------------------------------------------------------------
    # Learning Metrics
    # ------------------------------------------------------------------

    def update_learning_score(
        self,
        score: float,
    ) -> None:
        """
        Updates the learning score.
        """
        if score < 0:
            raise ValueError(
                "Learning score cannot be negative."
            )

        self.learning_score = score

    def update_average_confidence(
        self,
        confidence: float,
    ) -> None:
        """
        Updates the average confidence.
        """
        if confidence < 0:
            raise ValueError(
                "Confidence cannot be negative."
            )

        self.average_confidence = confidence

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
    # Status
    # ------------------------------------------------------------------

    def archive(self) -> None:
        """
        Archives the snapshot.
        """
        self.status = SnapshotStatus.ARCHIVED

    def lock(self) -> None:
        """
        Locks the snapshot.
        """
        self.status = SnapshotStatus.LOCKED

    def activate(self) -> None:
        """
        Activates the snapshot.
        """
        self.status = SnapshotStatus.ACTIVE

    def delete(self) -> None:
        """
        Marks the snapshot as deleted.
        """
        self.status = SnapshotStatus.DELETED

    # ------------------------------------------------------------------
    # Utilities
    # ------------------------------------------------------------------

    def age_in_days(self) -> int:
        """
        Returns the age of the snapshot in days.
        """
        return (
            datetime.now(timezone.utc) - self.created_at
        ).days

    def calculate_growth(
        self,
        previous_snapshot: "KnowledgeSnapshot",
    ) -> Dict[str, float]:
        """
        Calculates growth compared to a previous snapshot.
        """
        return {
            "event_growth":
                self.event_count
                - previous_snapshot.event_count,

            "pattern_growth":
                self.pattern_count
                - previous_snapshot.pattern_count,

            "feedback_growth":
                self.feedback_count
                - previous_snapshot.feedback_count,

            "recommendation_growth":
                self.recommendation_count
                - previous_snapshot.recommendation_count,

            "node_growth":
                self.knowledge_graph_nodes
                - previous_snapshot.knowledge_graph_nodes,

            "edge_growth":
                self.knowledge_graph_edges
                - previous_snapshot.knowledge_graph_edges,
        }

    # ------------------------------------------------------------------
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the snapshot into a dictionary.
        """
        return {
            "snapshot_id": self.snapshot_id,
            "name": self.name,
            "description": self.description,
            "snapshot_type": self.snapshot_type.value,
            "status": self.status.value,
            "created_at": self.created_at.isoformat(),
            "created_by": self.created_by,
            "version": self.version,
            "learning_model_version": self.learning_model_version,
            "event_count": self.event_count,
            "pattern_count": self.pattern_count,
            "feedback_count": self.feedback_count,
            "recommendation_count": self.recommendation_count,
            "knowledge_graph_nodes": self.knowledge_graph_nodes,
            "knowledge_graph_edges": self.knowledge_graph_edges,
            "average_confidence": self.average_confidence,
            "learning_score": self.learning_score,
            "metadata": self.metadata,
            "tags": self.tags,
        }

    @classmethod
    def from_dict(
        cls,
        data: Dict[str, Any],
    ) -> "KnowledgeSnapshot":
        """
        Creates a KnowledgeSnapshot from a dictionary.
        """
        return cls(
            snapshot_id=data.get(
                "snapshot_id",
                str(uuid.uuid4()),
            ),
            name=data.get("name", ""),
            description=data.get("description", ""),
            snapshot_type=SnapshotType(
                data.get(
                    "snapshot_type",
                    SnapshotType.MANUAL.value,
                )
            ),
            status=SnapshotStatus(
                data.get(
                    "status",
                    SnapshotStatus.ACTIVE.value,
                )
            ),
            created_at=datetime.fromisoformat(
                data.get(
                    "created_at",
                    datetime.now(
                        timezone.utc
                    ).isoformat(),
                )
            ),
            created_by=data.get(
                "created_by",
                "System",
            ),
            version=data.get("version", "1.0"),
            learning_model_version=data.get(
                "learning_model_version",
                "1.0",
            ),
            event_count=data.get("event_count", 0),
            pattern_count=data.get("pattern_count", 0),
            feedback_count=data.get("feedback_count", 0),
            recommendation_count=data.get(
                "recommendation_count",
                0,
            ),
            knowledge_graph_nodes=data.get(
                "knowledge_graph_nodes",
                0,
            ),
            knowledge_graph_edges=data.get(
                "knowledge_graph_edges",
                0,
            ),
            average_confidence=data.get(
                "average_confidence",
                DEFAULT_CONFIDENCE,
            ),
            learning_score=data.get(
                "learning_score",
                DEFAULT_LEARNING_SCORE,
            ),
            metadata=data.get("metadata", {}),
            tags=data.get("tags", []),
        )

    def to_json(
        self,
        indent: int = 4,
    ) -> str:
        """
        Converts the snapshot to JSON.
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
    ) -> "KnowledgeSnapshot":
        """
        Creates a snapshot from JSON.
        """
        return cls.from_dict(
            json.loads(json_string)
        )

    # ------------------------------------------------------------------
    # Copy Utilities
    # ------------------------------------------------------------------

    def copy(self) -> "KnowledgeSnapshot":
        """
        Returns a deep copy of the snapshot.
        """
        return copy.deepcopy(self)

    def clone_with_updates(
        self,
        **updates: Any,
    ) -> "KnowledgeSnapshot":
        """
        Creates a cloned snapshot with updated fields.
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
            f"KnowledgeSnapshot("
            f"name='{self.name}', "
            f"version='{self.version}', "
            f"events={self.event_count}, "
            f"patterns={self.pattern_count}, "
            f"score={self.learning_score:.2f})"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """
        return self.__str__()


