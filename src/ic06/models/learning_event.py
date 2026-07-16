"""
learning_event.py

NOTE:
This file is a replacement skeleton for the missing LearningEvent model.
It is compatible with the IC-06 services created during this chat.
"""

from __future__ import annotations

import copy
import json
import uuid

from dataclasses import dataclass, field
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, List


class LearningEventType(Enum):
    REQUIREMENT_CHANGED = "requirement_changed"
    TEST_EXECUTED = "test_executed"
    TEST_FAILED = "test_failed"
    TEST_PASSED = "test_passed"
    PREDICTION_CREATED = "prediction_created"
    PREDICTION_FAILED = "prediction_failed"
    MODEL_UPDATED = "model_updated"
    KNOWLEDGE_UPDATED = "knowledge_updated"
    FEEDBACK_RECEIVED = "feedback_received"
    CUSTOM = "custom"

class LearningSource(Enum):
    IC01 = "IC01"
    IC02 = "IC02"
    IC03 = "IC03"
    IC04 = "IC04"
    IC05 = "IC05"
    IC06 = "IC06"
    IC07 = "IC07"
    IC08 = "IC08"
    IC09 = "IC09"
    IC10 = "IC10"
    IC11 = "IC11"
    IC12 = "IC12"
    USER = "USER"
    SYSTEM = "SYSTEM"
    UNKNOWN = "UNKNOWN"
class LearningSeverity(Enum):
    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


DEFAULT_CONFIDENCE = 1.0


@dataclass
class LearningEvent:
    event_id: str = field(default_factory=lambda: str(uuid.uuid4()))
    title: str = ""
    description: str = ""
    event_type: LearningEventType = LearningEventType.CUSTOM
    source: LearningSource = LearningSource.UNKNOWN
    severity: LearningSeverity = LearningSeverity.INFO
    timestamp: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    success: bool = True
    confidence: float = DEFAULT_CONFIDENCE
    reference_id: str = ""
    component: str = ""
    user: str = ""
    session_id: str = ""
    predicted_value: Any = None
    actual_value: Any = None
    learning_delta: float = 0.0
    reward: float = 0.0
    processing_time: float = 0.0
    metadata: Dict[str, Any] = field(default_factory=dict)
    tags: List[str] = field(default_factory=list)
    related_entities: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.validate()

    def validate(self):
        if not self.title.strip():
            raise ValueError("Event title cannot be empty.")
        if not 0.0 <= self.confidence <= 1.0:
            raise ValueError("Confidence must be between 0 and 1.")

    def update_confidence(self, confidence: float):
        if not 0.0 <= confidence <= 1.0:
            raise ValueError("Confidence must be between 0 and 1.")
        self.confidence = confidence

    def mark_success(self):
        self.success = True

    def mark_failure(self):
        self.success = False

    def apply_reward(self, reward: float):
        self.reward = reward

    def update_learning_delta(self, delta: float):
        self.learning_delta = delta

    def add_metadata(self, key: str, value: Any):
        self.metadata[key] = value

    def remove_metadata(self, key: str):
        self.metadata.pop(key, None)

    def add_tag(self, tag: str):
        if tag and tag not in self.tags:
            self.tags.append(tag)

    def remove_tag(self, tag: str):
        if tag in self.tags:
            self.tags.remove(tag)

    def add_related_entity(self, entity: str):
        if entity and entity not in self.related_entities:
            self.related_entities.append(entity)

    def remove_related_entity(self, entity: str):
        if entity in self.related_entities:
            self.related_entities.remove(entity)

    def to_dict(self):
        return {
            "event_id": self.event_id,
            "title": self.title,
            "description": self.description,
            "event_type": self.event_type.value,
            "source": self.source.value,
            "severity": self.severity.value,
            "timestamp": self.timestamp.isoformat(),
            "success": self.success,
            "confidence": self.confidence,
            "reference_id": self.reference_id,
            "component": self.component,
            "user": self.user,
            "session_id": self.session_id,
            "predicted_value": self.predicted_value,
            "actual_value": self.actual_value,
            "learning_delta": self.learning_delta,
            "reward": self.reward,
            "processing_time": self.processing_time,
            "metadata": self.metadata,
            "tags": self.tags,
            "related_entities": self.related_entities,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            event_id=data.get("event_id", str(uuid.uuid4())),
            title=data.get("title",""),
            description=data.get("description",""),
            event_type=LearningEventType(data.get("event_type","custom")),
            source=LearningSource(data.get("source","UNKNOWN")),
            severity=LearningSeverity(data.get("severity","info")),
            timestamp=datetime.fromisoformat(data.get("timestamp", datetime.now(timezone.utc).isoformat())),
            success=data.get("success",True),
            confidence=data.get("confidence",1.0),
            reference_id=data.get("reference_id",""),
            component=data.get("component",""),
            user=data.get("user",""),
            session_id=data.get("session_id",""),
            predicted_value=data.get("predicted_value"),
            actual_value=data.get("actual_value"),
            learning_delta=data.get("learning_delta",0.0),
            reward=data.get("reward",0.0),
            processing_time=data.get("processing_time",0.0),
            metadata=data.get("metadata",{}),
            tags=data.get("tags",[]),
            related_entities=data.get("related_entities",[]),
        )

    def to_json(self, indent=4):
        return json.dumps(self.to_dict(), indent=indent)

    @classmethod
    def from_json(cls, s):
        return cls.from_dict(json.loads(s))

    def copy(self):
        return copy.deepcopy(self)

    def clone_with_updates(self, **updates):
        c = self.copy()
        for k,v in updates.items():
            if hasattr(c,k):
                setattr(c,k,v)
        return c

    def __str__(self):
        return f"LearningEvent(title='{self.title}', success={self.success}, confidence={self.confidence:.2f})"

    __repr__ = __str__
