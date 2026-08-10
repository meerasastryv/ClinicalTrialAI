"""
base_model.py

Platform Foundation (PF-01)

Defines the abstract base model used throughout the ClinicalTrialAI
platform. All domain models should inherit from BaseModel to obtain
consistent functionality for identification, timestamps, metadata,
serialization, cloning, and validation.

Author: Meera Sastry
Project: ClinicalTrialAI
"""

from __future__ import annotations

import copy
import json
import uuid

from abc import ABC
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from typing import Any, Dict, List


@dataclass
class BaseModel(ABC):
    """
    Abstract base class for all platform domain models.

    Provides:

    - Unique identifier
    - Creation timestamp
    - Last updated timestamp
    - Metadata support
    - Tag support
    - Serialization
    - Cloning
    - Validation hook
    """

    id: str = field(default_factory=lambda: str(uuid.uuid4()))

    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    updated_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc)
    )

    metadata: Dict[str, Any] = field(default_factory=dict)

    tags: List[str] = field(default_factory=list)

    # ------------------------------------------------------------------
    # Lifecycle
    # ------------------------------------------------------------------

    def __post_init__(self) -> None:
        """
        Performs initialization after dataclass construction.
        """
        self.validate()

    # ------------------------------------------------------------------
    # Validation
    # ------------------------------------------------------------------

    def validate(self) -> None:
        """
        Validation hook.

        Derived classes should override this method when business
        validation rules are required.
        """
        return

    # ------------------------------------------------------------------
    # Timestamp Helpers
    # ------------------------------------------------------------------

    def touch(self) -> None:
        """
        Updates the modification timestamp.
        """
        self.updated_at = datetime.now(timezone.utc)

    # ------------------------------------------------------------------
    # Metadata
    # ------------------------------------------------------------------

    def add_metadata(
        self,
        key: str,
        value: Any,
    ) -> None:
        """
        Adds or updates metadata.
        """
        self.metadata[key] = value
        self.touch()

    def remove_metadata(
        self,
        key: str,
    ) -> None:
        """
        Removes metadata if present.
        """
        self.metadata.pop(key, None)
        self.touch()

    # ------------------------------------------------------------------
    # Tag Helpers
    # ------------------------------------------------------------------

    def add_tag(
        self,
        tag: str,
    ) -> None:
        """
        Adds a tag if not already present.
        """
        if tag not in self.tags:
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
    # Serialization
    # ------------------------------------------------------------------

    def to_dict(self) -> Dict[str, Any]:
        """
        Converts the model into a serializable dictionary.

        Returns:
            Dictionary representation of the model.
        """
        data = asdict(self)

        for key, value in data.items():
            if isinstance(value, datetime):
                data[key] = value.isoformat()

        return data

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "BaseModel":
        """
        Creates an instance from a dictionary.

        Args:
            data: Dictionary representation.

        Returns:
            Instance of the model.
        """
        values = dict(data)

        if "created_at" in values and isinstance(values["created_at"], str):
            values["created_at"] = datetime.fromisoformat(values["created_at"])

        if "updated_at" in values and isinstance(values["updated_at"], str):
            values["updated_at"] = datetime.fromisoformat(values["updated_at"])

        return cls(**values)

    def to_json(self, indent: int = 4) -> str:
        """
        Serializes the model to JSON.

        Args:
            indent:
                JSON indentation.

        Returns:
            JSON string.
        """
        return json.dumps(
            self.to_dict(),
            indent=indent,
            ensure_ascii=False,
        )

    @classmethod
    def from_json(cls, json_string: str) -> "BaseModel":
        """
        Creates an instance from JSON.

        Args:
            json_string:
                JSON representation.

        Returns:
            Model instance.
        """
        return cls.from_dict(json.loads(json_string))

    # ------------------------------------------------------------------
    # Copy Utilities
    # ------------------------------------------------------------------

    def copy(self) -> "BaseModel":
        """
        Returns a deep copy of the model.
        """
        return copy.deepcopy(self)

    def clone_with_updates(self, **updates: Any) -> "BaseModel":
        """
        Creates a cloned object with updated fields.

        Example:
            cloned = event.clone_with_updates(
                confidence=0.95,
                success=False
            )
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
            f"{self.__class__.__name__}"
            f"(id={self.id})"
        )

    def __repr__(self) -> str:
        """
        Developer representation.
        """
        return self.__str__()
