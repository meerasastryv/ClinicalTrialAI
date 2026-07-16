"""
learning_event.py

Adaptive Learning Engine - Learning Event Model

This module defines the core domain model used by the Adaptive Learning
Engine (IC-06). A LearningEvent represents a single observation or
experience generated anywhere within the AI-Enabled Quality Engineering
Platform.

Learning events are produced by all Intelligence Components (IC-01 to
IC-12) and are used to:

    * Capture platform experiences
    * Discover recurring patterns
    * Measure prediction accuracy
    * Update the Knowledge Graph
    * Improve future recommendations
    * Drive adaptive learning

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
from typing import Any, Dict, List, Optional


# ============================================================================
# Enumerations
# ============================================================================


class LearningEventType(Enum):
    """
    Represents the type of learning event.
    """

    REQUIREMENT_CHANGED = "requirement_changed"
    TEST_EXECUTED = "test_executed"
    TEST_FAILED = "test_failed"
    TEST_PASSED = "test_passed"

    CODE_CHANGED = "code_changed"
    CODE_ANALYZED = "code_analyzed"

    RUNTIME_EVENT = "runtime_event"
    PERFORMANCE_EVENT = "performance_event"

    KNOWLEDGE_UPDATED = "knowledge_updated"
    PATTERN_DISCOVERED = "pattern_discovered"

    PREDICTION_GENERATED = "prediction_generated"
    PREDICTION_CONFIRMED = "prediction_confirmed"
    PREDICTION_FAILED = "prediction_failed"

    USER_FEEDBACK = "user_feedback"
    SYSTEM_FEEDBACK = "system_feedback"

    MODEL_UPDATED = "model_updated"

    RECOMMENDATION_ACCEPTED = "recommendation_accepted"
    RECOMMENDATION_REJECTED = "recommendation_rejected"

    CUSTOM = "custom"


class LearningSource(Enum):
    """
    Component that generated the learning event.
    """

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

    SYSTEM = "SYSTEM"
    USER = "USER"
    API = "API"
    UNKNOWN = "UNKNOWN"


class LearningSeverity(Enum):
    """
    Severity associated with a learning event.
    """

    INFO = "info"
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


# ============================================================================
# Default Constants
# ============================================================================

DEFAULT_CONFIDENCE: float = 1.0
DEFAULT_SUCCESS: bool = True

MAX_TITLE_LENGTH = 200
MAX_DESCRIPTION_LENGTH = 5000
